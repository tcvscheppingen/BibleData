import pandas as pd
# This script is used as a way to test the capability of Pandas to read .txt files

data = pd.read_csv('Data/BiblicalPlacesWithRefMerged.txt', sep="\t")

print(data)
