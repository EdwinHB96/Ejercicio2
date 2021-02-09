# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['parametros_vuelo_drone.py'],
             pathex=['D:\\Usuario\\OneDrive - Universidad Nacional Autónoma de Honduras\\I Periodo 2021\\CTE-334 Desarrollo de aplicaciones sistemas de información geográfica\\1 Unidad\\tareas\\hechas\\Ejercicio_2'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='parametros_vuelo_drone',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
