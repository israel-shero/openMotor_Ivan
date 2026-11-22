"""Offline tests. No network or GitHub permissions required."""
import importlib.util
import pathlib
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("claim", pathlib.Path(__file__).with_name("claim.py"))
claim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(claim)

class ClaimTests(unittest.TestCase):
    def test_valid_claim(self):
        sha = "a"*40
        with patch.object(claim,"request",return_value=(201,{"ref":"refs/heads/claims/UQ-01","object":{"sha":sha}})) as call:
            r=claim.run("owner/repo","UQ-01",sha,"token","https://api.github.com","acquire")
            self.assertEqual(r["status"],"ACQUIRED")
            self.assertEqual(call.call_args.args[0],"POST")
            self.assertEqual(call.call_args.args[3],{"ref":"refs/heads/claims/UQ-01","sha":sha})
    def test_conflict_fails_closed(self):
        with patch.object(claim,"request",side_effect=claim.ClaimError("GitHub HTTP 422")):
            with self.assertRaises(claim.ClaimError):
                claim.run("owner/repo","UQ-01","a"*40,"token","https://api.github.com","acquire")
    def test_ambiguous_fails_closed(self):
        with patch.object(claim,"request",side_effect=claim.ClaimError("timeout")):
            with self.assertRaises(claim.ClaimError):
                claim.run("owner/repo","UQ-01","a"*40,"token","https://api.github.com","acquire")
    def test_invalid_task_rejected(self):
        with self.assertRaises(claim.ClaimError):
            claim.run("owner/repo","../escape","a"*40,"token","https://api.github.com","acquire")
    def test_no_base_rejected(self):
        with self.assertRaises(claim.ClaimError):
            claim.run("owner/repo","UQ-01",None,"token","https://api.github.com","acquire")
    def test_wrong_response_rejected(self):
        with patch.object(claim,"request",return_value=(201,{"ref":"refs/heads/claims/OTHER","object":{"sha":"a"*40}})):
            with self.assertRaises(claim.ClaimError):
                claim.run("owner/repo","UQ-01","a"*40,"token","https://api.github.com","acquire")

    def test_inspect_only_reports_exact_ref_with_valid_commit_sha(self):
        ref = "refs/heads/claims/INF-01"
        sha = "a" * 40
        with patch.object(claim, "request", return_value=(200, {"ref": ref, "object": {"sha": sha}})) as call:
            result = claim.run("owner/repo", "INF-01", None, "token", "https://api.github.com", "inspect")
        self.assertEqual(result, {"status": "EXISTS", "ref": ref, "sha": sha})
        call.assert_called_once_with("GET", "https://api.github.com/repos/owner/repo/git/ref/heads/claims/INF-01", "token")

    def test_inspect_rejects_inconclusive_response(self):
        ref = "refs/heads/claims/INF-01"
        sha = "a" * 40
        responses = (
            (201, {"ref": ref, "object": {"sha": sha}}),
            (200, {"ref": ref + "-old", "object": {"sha": sha}}),
            (200, {"ref": ref, "object": {"sha": "abc"}}),
            (200, {"ref": ref, "object": None}),
            (200, []),
        )
        for response in responses:
            with self.subTest(response=response), patch.object(claim, "request", return_value=response):
                with self.assertRaisesRegex(claim.ClaimError, "STOP"):
                    claim.run("owner/repo", "INF-01", None, "token", "https://api.github.com", "inspect")

    def test_acquire_rejects_malformed_success_without_retry(self):
        for payload in ([], {"ref": "refs/heads/claims/INF-01", "object": None}):
            with self.subTest(payload=payload), patch.object(claim, "request", return_value=(201, payload)) as call:
                with self.assertRaisesRegex(claim.ClaimError, "STOP"):
                    claim.run("owner/repo", "INF-01", "a" * 40, "token", "https://api.github.com", "acquire")
                call.assert_called_once()

    def test_transport_timeout_after_create_attempt_is_ambiguous_and_never_retried(self):
        with patch.object(claim.urllib.request, "urlopen", side_effect=TimeoutError("response lost")) as call:
            with self.assertRaisesRegex(claim.ClaimError, "Ambiguous.*STOP"):
                claim.run("owner/repo", "INF-01", "a" * 40, "token", "https://api.github.com", "acquire")
            call.assert_called_once()
            self.assertEqual(call.call_args.args[0].get_method(), "POST")

if __name__=="__main__":
    unittest.main()
