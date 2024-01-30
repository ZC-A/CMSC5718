import math
import numpy as np
from scipy.stats import norm

"""
@author ZhangChi
@date 2024/01/30
CMSC 5718 Assignment 1 Question1
Using Order Number 9, stock code 3968, stock name China Merchants Bank, S = 27.20, volatility = 37.2%
It may take about few seconds to calculate answer
"""


S, K = 27.20, 27.20
Volatility = 0.372

T = 0.75
r = 0.523

N, delta_t = 150, 1 / 200
Path_1, Path_2 = 10000, 300000


def calculate_european_call_option():
    d1 = (np.log(S / K) + (r + Volatility ** 2 / 2) * T) / Volatility * math.sqrt(T)
    d2 = d1 - Volatility * math.sqrt(T)
    european_call_option = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return european_call_option


def calculate_monte_carlo():
    output1 = [0] * Path_1
    output2 = [0] * Path_2

    for i in range(Path_1):
        cur_s = S
        for _ in range(N):
            delta_s = cur_s * r * delta_t + Volatility * math.sqrt(delta_t) * cur_s * np.random.normal()
            cur_s += delta_s
        output1[i] = max(0, cur_s - K)

    for i in range(Path_2):
        cur_s = S
        for _ in range(N):
            delta_s = cur_s * r * delta_t + Volatility * math.sqrt(delta_t) * cur_s * np.random.normal()
            cur_s += delta_s
        output2[i] = max(0, cur_s - K)

    return np.mean(output1) * np.exp(-r * T), np.mean(output2) * np.exp(-r * T)


if __name__ == '__main__':
    print("European call option:" + str(calculate_european_call_option()))
    monte_carlo_10000, monte_carlo_300000 = calculate_monte_carlo()
    print("Monte Carlo with 10000 paths: " + str(monte_carlo_10000) + ", with 300000 paths: " + str(monte_carlo_300000))
