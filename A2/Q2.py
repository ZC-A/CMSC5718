"""
@author ZhangChi HuangShuyin
@date 2024/02/26
CMSC 5718 Assignment 2 Question1
Using Order Number 5, stock code 11, read the xlsx file
"""

import pandas as pd
import math
import numpy as np
from scipy.stats import norm

data_path = 'CMSC 5718 Assignment 2 stock data.xlsx'

df = pd.read_excel(data_path, sheet_name='data for hedging exercise')
data = list(df.iloc[3:, 9])   # pick the target column from xlsx file
r = 0.0503
implied_volatility = 0.2114
T = 0.9973

