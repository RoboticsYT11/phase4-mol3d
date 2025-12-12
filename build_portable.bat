@echo off
echo 🧬 Phase4-Mol3D Portable Builder
echo ================================

echo 📦 Installing required packages...
pip install pyinstaller rdkit flask requests gunicorn

echo 🏗️  Building portable executable...
echo This may take 5-10 minutes, please wait...

pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" --hidden-import rdkit --hidden-import rdkit.Chem --hidden-import rdkit.Chem.AllChem --name "Phase4-Mol3D-Portable" launcher.py

echo ✅ Build complete!
echo 📁 Your portable app is in: dist\Phase4-Mol3D-Portable.exe
echo 💡 Share this .exe file - no installation needed!

pause