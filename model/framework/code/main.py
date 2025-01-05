# imports
import os
import csv
import sys
import joblib
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

#model paths
mdl_sex_path = os.path.abspath(os.path.join(root, "../..",  "checkpoints", "sexualsSVCFinalHPT_UMFP_model5005.pkl"))
mdl_abs_path = os.path.abspath(os.path.join(root, "../..",  "checkpoints", "asexualsRandomForestFinalizedhpt5005_UMFP_model.pkl"))

# my model
def _smi_to_fps(smiles):
    mols = [Chem.MolFromSmiles(smi) for smi in smiles]
    fp = [AllChem.GetMorganFingerprintAsBitVect(mol, 5, nBits=500) for mol in mols] # gets the vector
    return fp

def _load_model(model):
    mdl = joblib.load(model)
    return mdl

def predict(smiles, model):
    X = _smi_to_fps(smiles)
    mdl = _load_model(model)
    y_pred = mdl.predict_proba(X)
    return y_pred[:,1]

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs_sex = predict(smiles_list, mdl_sex_path)
outputs_abs = predict(smiles_list, mdl_abs_path)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs_sex)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["sexual_stage", "asexual_blood_stage"])  # header
    for s, a in zip(outputs_sex, outputs_abs):
        writer.writerow([s, a])
