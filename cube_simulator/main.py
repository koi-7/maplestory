#!/usr/bin/env python3
# coding: utf-8


import numpy as np


RARE      = 0
EPIC      = 1
UNIQUE    = 2
LEGENDARY = 3

CUBE_COST = 20000000

TIER_INCREASE = 0
TIER_STAY = 1


prob_table = [
    [0.06, 0.94],
    [0.018, 0.982],
    [0.003, 0.997]
]

def main():
    cost_list = []
    num_of_cube_list = []

    start_tier = int(input('現在の等級（1: レア、2: エピック、3: ユニーク）: '))

    for _ in range(1000):
        cost = 0
        num_of_cube = 0
        current_tier = start_tier - 1

        while current_tier != LEGENDARY:
            cost += CUBE_COST
            num_of_cube += 1

            result = np.random.choice(2, p=prob_table[current_tier])

            if result == TIER_INCREASE:
                current_tier += 1
            elif result == TIER_STAY:
                pass

        cost_list.append(cost)
        num_of_cube_list.append(num_of_cube)

    print('平均費用: ' + "{:,}".format(np.average(cost_list)) + ' メル')
    print('平均個数: ' + "{:,}".format(np.average(num_of_cube_list)) + ' 個')


if __name__ == '__main__':
    main()
