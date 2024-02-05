"""
@author ZhangChi
@date 2024/02/05
CMSC 5718 Assignment 1 Question3
Using Order Number 5, stock code 700, stock name Tencent, S = 293.60, volatility = 31.8%
F, UB, LB in Group 3
It may take about few seconds to calculate answer
"""

import math
import numpy as np

S, K = 293.60, 293.60
Volatility = 0.318

T = 0.5
r = 0.0515

N, delta_t = 120, 1 / 240
Path_1, Path_2 = 100000, 300000

F, UB, LB = 1.0080, 1.16, 0.84

NOM = 100000


def calculate_monte_carlo_shark_fin():
    output1 = [0] * Path_1

    for i in range(Path_1):
        cur_s = S
        barrier = False
        for _ in range(N):
            delta_s = cur_s * r * delta_t + Volatility * math.sqrt(delta_t) * cur_s * np.random.normal()
            cur_s += delta_s

            if cur_s > S * UB or cur_s < S * LB:
                barrier = True

        if barrier:
            payoff = NOM * F
        else:
            payoff = NOM * (1 + abs(cur_s / S - 1))

        output1[i] = payoff

    return np.mean(output1) * np.exp(-r * T)


if __name__ == '__main__':
    print("calculate shark fin using monte carlo " + str(calculate_monte_carlo_shark_fin()))
