# 🧬 Phase4-Mol3D Molecular Visualizer

Advanced 3D molecular visualization web application with hand gesture controls.

## Features

- **3D Molecular Visualization** - Interactive 3D molecular models
- **Hand Gesture Control** - Thumb-index rotation control using MediaPipe
- **SMILES to 3D Conversion** - Convert chemical notation to 3D structures
- **PDB Protein Loading** - Load protein structures from RCSB database
- **Predefined Molecule Library** - Water, Ethanol, Caffeine, and more
- **Atom Inspection** - Click atoms for detailed information
- **XYZ Coordinate Support** - Load custom molecular coordinates

## Technology Stack

- **Backend**: Python Flask + RDKit
- **Frontend**: HTML5 + 3Dmol.js + MediaPipe
- **Deployment**: Render (render.com)

## Live Demo

🚀 **Deployed at**: [Your Render URL will appear here after deployment]

## Local Development

```bash
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

## Deployment

This app is configured for one-click deployment on Render.com:

1. Fork this repository
2. Connect to Render
3. Deploy as Web Service
4. Render auto-detects Python and uses:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`

## Project Structure

```
phase4-mol3d/
├── app.py              # Main Flask application
├── converter.py        # SMILES to MOL conversion
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Frontend interface
└── static/
    ├── IITB.png       # IIT Bombay logo
    ├── Yantrik-logo.jpg
    └── PMRFLOGO.jpg
```

## Usage

1. **Select Molecule**: Choose from dropdown or enter SMILES notation
2. **Render 3D**: Click to generate interactive 3D structure
3. **Hand Control**: Enable for gesture-based rotation
4. **PDB Loading**: Enter PDB ID for proteins/DNA structures
5. **Inspect Mode**: Click atoms for detailed information

---

**Developed for IIT Bombay Software Project**  
*Phase4-Mol3D Molecular Visualization System*