import pandas as pd
# This script is used as a way to demonstrate Pandas' capability of parsing .txt files
# For now this code has no other use, but it wil be implemented in future versions in order to read data from .txt files

data = pd.read_csv('Data/BiblicalPlacesWithRefMerged.txt', sep="\t")

print(data)
