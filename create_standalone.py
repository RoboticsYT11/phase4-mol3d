"""
Create standalone executable for Phase4-Mol3D
This script packages the Flask app into a single .exe file
"""

import os
import sys
import subprocess

def create_standalone():
    print("🔧 Creating standalone Phase4-Mol3D application...")
    
    # Install PyInstaller if not present
    try:
        import PyInstaller
    except ImportError:
        print("📦 Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Create spec file for PyInstaller
    spec_content = '''
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('templates', 'templates'),
        ('static', 'static'),
    ],
    hiddenimports=[
        'rdkit',
        'rdkit.Chem',
        'rdkit.Chem.AllChem',
        'flask',
        'requests',
        'converter'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Phase4-Mol3D',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    coerce_archive=True,
    icon=None,
)
'''
    
    # Write spec file
    with open('Phase4-Mol3D.spec', 'w') as f:
        f.write(spec_content)
    
    print("📝 Created PyInstaller spec file")
    
    # Build executable
    print("🏗️  Building executable (this may take 5-10 minutes)...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "PyInstaller", 
            "--clean", 
            "Phase4-Mol3D.spec"
        ])
        print("✅ Standalone executable created successfully!")
        print("📁 Find your app in: dist/Phase4-Mol3D.exe")
        print("💡 You can now share this .exe file - no Python installation needed!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    create_standalone()