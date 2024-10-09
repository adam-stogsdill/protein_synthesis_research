from Bio.PDB import PDBParser

# Initialize the PDB parser
parser = PDBParser()

# Load the structure from the PDB file
structure = parser.get_structure('8z0f', file='./data/8z0f.pdb')

