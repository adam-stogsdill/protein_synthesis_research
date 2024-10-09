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

def context_size_filter(dataframe, context_length: int=1024, min_length: int=0, max_length: int=None, window: bool=True, stride: int=100) -> pd.DataFrame:
    output_data = {"Name": [], "Sequence": [], "MolType": [], 'length': []}
    for idx, row in dataframe.iterrows():
        if row['length'] > min_length and row['length'] <= max_length:
            if window and len(row['Sequence']) > context_length:
                for i, index in enumerate(range(0, len(row['Sequence']), stride)):
                    sequence_data = row['Sequence'][index:index+context_length] if len(row['Sequence'][index:]) > context_length else row['Sequence'][index:]
                    output_data['Name'].append(f'{row["Name"]}_{i}')
                    output_data['Sequence'].append(sequence_data)
                    output_data['MolType'].append(row['MolType'])
                    output_data['length'].append(len(sequence_data))
            else:
                for key in output_data:
                    output_data[key].append(row[key])
                
    return pd.DataFrame.from_dict(output_data)
            
            