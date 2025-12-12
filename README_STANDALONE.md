# 🧬 Phase4-Mol3D Standalone Distribution

## 📦 Two Distribution Options

### Option A: Portable Executable (Recommended)
**Single .exe file that runs anywhere - no installation needed!**

#### To Create Portable Version:
1. **Double-click** `build_portable.bat`
2. **Wait 5-10 minutes** for build to complete
3. **Find your app** in `dist\Phase4-Mol3D-Portable.exe`
4. **Share this .exe file** - works on any Windows PC!

#### To Use Portable Version:
1. **Double-click** `Phase4-Mol3D-Portable.exe`
2. **App opens automatically** in your browser
3. **Start visualizing molecules!**

### Option B: Python Distribution (Requires Python)
**For users who have Python installed**

#### Files to Share:
```
📁 phase4-mol3d/
├── 📄 app.py
├── 📄 converter.py
├── 📄 launcher.py
├── 📄 requirements.txt
├── 📁 templates/
│   └── 📄 index.html
└── 📁 static/
    ├── 🖼️ IITB.png
    ├── 🖼️ Yantrik-logo.jpg
    └── 🖼️ PMRFLOGO.jpg
```

#### Installation Instructions (for end users):
1. **Install Python** (if not installed): [python.org](https://python.org)
2. **Extract** the phase4-mol3d folder
3. **Open Command Prompt** in the folder
4. **Run**: `pip install -r requirements.txt`
5. **Run**: `python launcher.py`

## 🎯 Features Included

✅ **3D Molecular Visualization** - Interactive 3D models
✅ **Hand Gesture Control** - Thumb-index rotation control  
✅ **SMILES to 3D** - Convert chemical notation to 3D structures
✅ **PDB Protein Loading** - Load protein structures from database
✅ **Predefined Molecules** - Water, Ethanol, Caffeine, etc.
✅ **Atom Inspection** - Click atoms for detailed information
✅ **XYZ Coordinate Support** - Load custom molecular coordinates

## 🖥️ System Requirements

- **Windows 7/8/10/11**
- **2GB RAM minimum**
- **Modern web browser** (Chrome, Firefox, Edge)
- **Internet connection** (for PDB downloads only)

## 🚀 Quick Start

### For Portable Version:
1. Download `Phase4-Mol3D-Portable.exe`
2. Double-click to run
3. App opens in browser automatically
4. Select a molecule and click "Render 3D"

### For Python Version:
1. Extract folder
2. Run `python launcher.py`
3. App opens in browser at http://localhost:5000

## 📋 Usage Instructions

1. **Select Molecule**: Choose from dropdown or enter SMILES
2. **Render 3D**: Click button to generate 3D structure
3. **Hand Control**: Enable for gesture-based rotation
4. **PDB Loading**: Enter PDB ID for proteins/DNA
5. **Inspect Mode**: Click atoms for detailed information

## 🔧 Troubleshooting

**App won't start?**
- Ensure no antivirus blocking
- Try running as administrator
- Check Windows Defender exclusions

**Browser doesn't open?**
- Manually go to http://localhost:5000
- Try different browser

**Molecules won't load?**
- Check internet connection (for PDB)
- Verify SMILES notation is correct

## 📞 Support

For issues or questions about Phase4-Mol3D molecular visualizer, contact your system administrator or development team.

---
**Phase4-Mol3D** - Advanced Molecular Visualization System
*Developed for IIT Bombay Software Project*