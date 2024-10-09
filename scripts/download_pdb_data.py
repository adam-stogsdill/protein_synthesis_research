import urllib.request
import os

def download_pdb_data(id, website='https://files.wwpdb.org/pub/pdb/data/biounit/PDB/all/'):
    url = f'{website}{id.lower()}.pdb1.gz'
    # download the data
    urllib.request.urlretrieve('tmp.gz')