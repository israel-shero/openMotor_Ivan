"""Exercise configuration dispatch without running a simulation backend."""
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

from motorlib import solvers
from motorlib.motor import Motor
from uilib.simulationManager import SimulationManager


class TestSolverConfigBaseline(unittest.TestCase):
    def test_dispatch_precedence_for_selected_solver(self):
        cases = [
            ("motor override", {"marker": "local"}, {"marker": "global"}, {"marker": "local"}),
            ("global default", {}, {"marker": "global"}, {"marker": "global"}),
            ("unset", {}, {}, None),
        ]
        for label, local, global_config, expected in cases:
            with self.subTest(label=label):
                preferences = SimpleNamespace(
                    activeSolver="test-stub",
                    getSolverConfig=Mock(return_value=global_config),
                )
                backend = Mock()
                backend.simulate.return_value = SimpleNamespace(success=False)
                manager = self.make_manager(preferences, {"test-stub": local})
                with patch.object(solvers, "get_solver", return_value=backend):
                    SimulationManager._simThread(manager, show=False)
                backend.simulate.assert_called_once_with(
                    manager.motor, config=expected, callback=manager.updateProgressBar,
                )
                manager.motor.runSimulation.assert_not_called()

    def test_unregistered_selection_falls_back_to_quasi_steady(self):
        backend = Mock()
        backend.simulate.return_value = SimpleNamespace(success=False)
        preferences = SimpleNamespace(activeSolver="unregistered", getSolverConfig=Mock(return_value={}))
        for prefs, available in [(preferences, backend), (None, None)]:
            with self.subTest(preferences=prefs, registered=available is not None):
                manager = self.make_manager(prefs, {})
                registry = {solvers.QUASI_STEADY: available}
                with patch.object(solvers, "get_solver", side_effect=registry.get):
                    self.assertEqual(manager.activeSolverName(), solvers.QUASI_STEADY)
                    SimulationManager._simThread(manager, show=False)
                if available is None:
                    manager.motor.runSimulation.assert_called_once_with(manager.updateProgressBar)
                else:
                    available.simulate.assert_called_once_with(
                        manager.motor, config=None, callback=manager.updateProgressBar,
                    )
                    manager.motor.runSimulation.assert_not_called()

    def test_motor_round_trip_preserves_unregistered_config(self):
        data = Motor().getDict()
        original = {"unregistered-test-solver": {"custom": ["value"]}}
        data["solverConfigs"] = original
        self.assertEqual(Motor(data).getDict()["solverConfigs"], original)
        del data["solverConfigs"]
        self.assertEqual(Motor(data).getDict()["solverConfigs"], {})

    @staticmethod
    def make_manager(preferences, configs):
        manager = SimpleNamespace(
            preferences=preferences,
            motor=SimpleNamespace(
                solverConfigs=configs,
                runSimulation=Mock(return_value=SimpleNamespace(success=False)),
            ),
            updateProgressBar=Mock(),
            simulationDone=Mock(),
        )
        manager.activeSolverName = lambda: SimulationManager.activeSolverName(manager)
        return manager
