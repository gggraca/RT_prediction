from rdkit.Chem import Descriptors
from rdkit import Chem

from pandas import DataFrame
import pandas as pd

#read the data
data = pd.read_csv('SLPOS_metabolites_known_RT.csv')


# get the full list of descriptors
def get_descriptors(mol):
    ret_dict={}
    for name,func in Descriptors.descList:
        ret_dict[name] = func(mol)

    data = DataFrame(ret_dict,index=[0])
    return data


smile_list = data['SMILES'].tolist()
che_property = DataFrame()

for smile in smile_list:
    try:
        mol = Chem.MolFromSmiles(smile)
        chemistry = get_descriptors(mol)
        che_property = che_property.append(chemistry, ignore_index=True)
    except:
        print(smile)
        continue

che_property.to_csv('result.csv')

