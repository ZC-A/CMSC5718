"""
@author ZhangChi
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


def calculate_volatility():
    u_arr = []

    for i in range(1, len(data)):
        u_arr.append(math.log(data[i] / data[i - 1]))  # calculate the realized volatility

    u_mean = sum(u_arr) / len(u_arr)

    tmp = 0

    for i in range(len(u_arr)):
        tmp += (u_arr[i] - u_mean) ** 2

    tmp /= len(u_arr)

    return math.sqrt(tmp) * math.sqrt(len(data))


def black_sholes(volatility, s_0, k, t, r):
    d1 = (np.log(s_0 / k) + (r + volatility ** 2 / 2) * T) / volatility * math.sqrt(t)
    d2 = d1 - volatility * math.sqrt(t)
    european_call_option = s_0 * norm.cdf(d1) - k * np.exp(-r * T) * norm.cdf(d2)

    european_put_option = k * np.exp(-r * t) * norm.cdf(-d2) - s_0 * norm.cdf(-d1)

    return european_call_option, european_put_option


if __name__ == '__main__':
    realized_volatility = calculate_volatility()
    print('realized volatility: ' + str(realized_volatility))

    realized_volatility_call, realized_volatility_put = black_sholes(realized_volatility, data[0], data[0], T, r)
    implied_volatility_call, implied_volatility_put = black_sholes(implied_volatility, data[0], data[0], T, r)

    print('realized volatility call and realized volatility put: ' + str(realized_volatility_call + realized_volatility_call))
    print('implied volatility call and implied volatility put: ' + str(implied_volatility_call + implied_volatility_put))
