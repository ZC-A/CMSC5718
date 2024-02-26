import pandas as pd

data_path = 'CMSC 5718 Assignment 2 stock data.xlsx'

df = pd.read_excel(data_path, sheet_name='data for hedging exercise')
data = df.iloc[3:, 9]   # pick the target column from xlsx file

