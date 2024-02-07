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
Path = 100000

F, UB, LB = 1.0080, 1.16, 0.84

NOM = 100000

profit_ratio = 0.0135


def calculate_monte_carlo_shark_fin(cur_f, cur_lb, cur_ub):
    output1 = [0] * Path

    for i in range(Path):
        cur_s = S
        barrier = False
        for _ in range(N):
            delta_s = cur_s * r * delta_t + Volatility * math.sqrt(delta_t) * cur_s * np.random.normal()
            cur_s += delta_s

            if cur_s > S * cur_ub or cur_s < S * cur_lb:
                barrier = True
                break

        if barrier:
            payoff = NOM * cur_f
        else:
            payoff = NOM * (1 + abs(cur_s / S - 1))

        output1[i] = payoff

    return np.mean(output1) * np.exp(-r * T)


def calculate_better_profit_f():
    profit = 0.0
    lower_f, upper_f = 0.0, F    # binary search to find the F value

    while abs(profit_ratio - profit) >= 1e-4:
        cur_payoff = calculate_monte_carlo_shark_fin((lower_f + upper_f) / 2, LB, UB)

        profit = (NOM - cur_payoff) / NOM

        if profit - profit_ratio >= 1e-4:
            lower_f = (lower_f + upper_f) / 2

        elif profit_ratio - profit >= 1e-4:
            upper_f = (lower_f + upper_f) / 2

    return (lower_f + upper_f) / 2


def calculate_better_profit_x():
    profit = 0.0
    lower_x, upper_x = 0.0, 1.0

    while abs(profit_ratio - profit) >= 1e-4:  # binary search to find the x
        x = (lower_x + upper_x) / 2
        cur_payoff = calculate_monte_carlo_shark_fin(F, 1 - x, 1 + x)

        profit = abs(NOM - cur_payoff) / NOM  # since under the barrier event, profit is lower than 1.35%, when the profit is lower increase the odds of barrier events

        if profit - profit_ratio >= 1e-4:     # when profit is higher than 1.35%, decrease the odds
            if NOM - cur_payoff <= 0:
                upper_x = (lower_x + upper_x) / 2
            else:
                lower_x = (lower_x + upper_x) / 2  # but under the case of calculation error due to the negative and postive problem, change the opposite pointer when come across the change of sign

        elif profit_ratio - profit >= 1e-4:
            if NOM - cur_payoff <= 0:
                lower_x = (lower_x + upper_x) / 2
            else:
                upper_x = (lower_x + upper_x) / 2
        print((lower_x + upper_x) / 2)
    return (lower_x + upper_x) / 2


if __name__ == '__main__':
    fair_price = calculate_monte_carlo_shark_fin(F, LB, UB)
    print("calculate fair price shark fin using monte carlo " + str(fair_price))
    print("inital profit " + str(NOM - fair_price))
    print("change F to: " + str(calculate_better_profit_f()))
    print("The settings of x: " + str(calculate_better_profit_x()))
