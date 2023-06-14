  # program.spec

  # ...

  a = Analysis(['program.py'],
               pathex=['path/to/program'],
               binaries=[],
               datas=[],
               hiddenimports=['yaml'],
               hookspath=[],
               runtime_hooks=[],
               excludes=[],
               win_no_prefer_redirects=False,
               win_private_assemblies=False,
               cipher=None,
               noarchive=False)
  # ...
