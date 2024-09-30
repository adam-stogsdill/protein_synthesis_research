import os
import pandas as pd

def load_pdb(molecule_filter: list[str], data_loc: str, length_filter = None) -> pd.DataFrame:
    if not os.path.exists(data_loc):
        raise Exception(f"Failed to find {data_loc}")
    
    output_data = {"Name": [], "Sequence": [], "MolType": [], 'length': []}
    
    with open(data_loc, 'r') as data_file:
        
        keep_running = True
        while keep_running:
            
            mol_data_list = data_file.readline().split(" ")
            if len(mol_data_list) < 4:
                break
            sequence = data_file.readline().strip()
            if "(5'" not in mol_data_list[-1]:
                mol_type, length, name = mol_data_list[1].split(":")[-1], float(mol_data_list[2].split(":")[-1]), ' '.join(mol_data_list[4:]).strip()
            else:
                mol_type, length, name = mol_data_list[1].split(":")[-1], float(mol_data_list[2].split(":")[-1]), ' '.join(mol_data_list[4:-1]).strip()
            
            if molecule_filter != [] and mol_type.lower() not in molecule_filter:
                continue
            
            if length_filter is not None and not length_filter(sequence):
                continue
            
            output_data["Name"].append(name)
            output_data['Sequence'].append(sequence)
            output_data["MolType"].append(mol_type)
            output_data["length"].append(length)
              
    return pd.DataFrame.from_dict(output_data)