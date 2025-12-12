from flask import Flask, render_template, request, jsonify
from converter import smiles_to_molblock
import requests

app = Flask(__name__)

# ---- Predefined Molecule Library (aligned with Phase 1 nomenclature) ---- #
MOLECULES = {
    "Water (H₂O)": "O",
    "Ethanol (C₂H₆O)": "CCO",
    "Methane (CH₄)": "CH4",
    "Carbon Dioxide (CO₂)": "O=C=O",
    "Glucose (C₆H₁₂O₆)": "C(C1C(C(C(C(O1)O)O)O)O)O",
    # Extra examples specific to Phase 4
    "Alanine": "CC(C(=O)O)N",
    "Caffeine": "Cn1cnc2n(C)c(=O)n(C)c(=O)c12",
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/molecules')
def molecules():
    """Send molecule library to frontend (same naming as Phase 1, with extras)."""
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

if __name__ == "__main__":
    app.run(debug=True)
