from flask import Flask, jsonify, request
from firebase_functions import https_fn
import requests
from rdkit import Chem
from rdkit.Chem import AllChem

# Initialize Flask app for Cloud Functions
app = Flask(__name__)

# Predefined Molecule Library
MOLECULES = {
    "Water (H₂O)": "O",
    "Ethanol (C₂H₆O)": "CCO",
    "Methane (CH₄)": "CH4",
    "Carbon Dioxide (CO₂)": "O=C=O",
    "Glucose (C₆H₁₂O₆)": "C(C1C(C(C(C(O1)O)O)O)O)O",
    "Alanine": "CC(C(=O)O)N",
    "Caffeine": "Cn1cnc2n(C)c(=O)n(C)c(=O)c12",
}

def smiles_to_molblock(smiles: str) -> str:
    """Convert a SMILES string to a 3-D MOL block."""
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            raise ValueError("Invalid SMILES string")

        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol, randomSeed=42)
        AllChem.UFFOptimizeMolecule(mol)
        return Chem.MolToMolBlock(mol)
    except Exception as e:
        raise RuntimeError(f"Conversion failed: {e}")

@app.route('/molecules')
def molecules():
    """Send molecule library to frontend."""
    return jsonify(MOLECULES)

@app.route('/molblock', methods=['POST'])
def molblock():
    data = request.get_json()
    smiles = data.get("smiles", "")
    try:
        molblock = smiles_to_molblock(smiles)
        return jsonify({"molblock": molblock})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/load_pdb/<pdb_id>')
def load_pdb(pdb_id):
    url = f"https://files.rcsb.org/download/{pdb_id.upper()}.pdb"
    r = requests.get(url)
    if r.status_code == 200:
        return jsonify({"pdb": r.text})
    return jsonify({"error": "Invalid or unavailable PDB ID."}), 404

@app.route('/xyz', methods=['POST'])
def xyz():
    data = request.get_json()
    xyz_text = data.get("xyz", "").strip()
    if not xyz_text:
        return jsonify({"error": "XYZ data missing"}), 400
    return jsonify({"xyz": xyz_text})

# Firebase Cloud Function
@https_fn.on_request()
def api(req):
    """Cloud Function entry point."""
    with app.request_context(req.environ):
        return app.full_dispatch_request()