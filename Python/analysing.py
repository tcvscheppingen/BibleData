import pandas as pd
import plotters as po
# This script is used as a way to test the capability of Pandas to read .txt files

data = pd.read_excel('Data/200416_BibleData.xlsx', sheet_name='KruisTabelCR')

po.plot_corr(data, 12, 12)
