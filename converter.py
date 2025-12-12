from rdkit import Chem
from rdkit.Chem import AllChem

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
