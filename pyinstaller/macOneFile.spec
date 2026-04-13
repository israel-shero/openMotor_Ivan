# -*- mode: python -*-

# Run with `pyinstaller --windowed --onedir`

import os

SPEC_DIR = os.path.abspath(globals().get('specpath', os.path.join(os.getcwd(), 'pyinstaller')))
cwd_main = os.path.join(os.getcwd(), 'main.py')
if os.path.isfile(cwd_main):
    PROJECT_DIR = os.path.abspath(os.getcwd())
else:
    PROJECT_DIR = os.path.abspath(os.path.join(SPEC_DIR, '..'))
appVersionStr = '0.6.1'

block_cipher = None

a = Analysis([os.path.join(PROJECT_DIR, 'main.py')],
             pathex=[PROJECT_DIR],
             binaries=[],
             datas=[],
             hiddenimports=['pywt._extensions._cwt'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False,
             target_arch=['x86_64', 'arm64'])
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='openMotor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False)
coll = COLLECT(exe,
              a.binaries,
              a.zipfiles,
              a.datas,
              strip=False,
              upx=True,
              name='openMotor')
app = BUNDLE(coll,
             name='openMotor.app',
             icon=os.path.join(PROJECT_DIR, 'resources', 'oMIconCycles.icns'),
             version=appVersionStr,
             info_plist={
              'NSHighResolutionCapable': True,
             },
             bundle_identifier=None)
