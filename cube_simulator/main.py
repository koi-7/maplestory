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

cube_cost = {1: 20000000, 2: 42500000, 3: 20000000, 4: 42500000}

prob_table = {
    1: [[0.06,  0.94],
        [0.018, 0.982],
        [0.003, 0.997]],
    2: [[0.15,  0.85],
        [0.035, 0.965],
        [0.01,  0.99]],
    3: [[0.12,  0.88],
        [0.036, 0.964],
        [0.006, 0.994]],
    4: [[0.3,   0.7],
        [0.07,  0.93],
        [0.02,  0.98]]
}

def main():
    cost_list = []
    num_of_cube_list = []

    cube = int(input('キューブ（1: ネオミラクルキューブ、2: ブラックキューブ）: '))
    start_tier = int(input('現在の等級（1: レア、2: エピック、3: ユニーク）: '))
    miracle_time = int(input('ミラクルタイム（0: OFF、1: ON）: '))

    if miracle_time and cube == 1:
        cube = 3
    elif miracle_time and cube == 2:
        cube = 4

    for _ in range(1000):
        cost = 0
        num_of_cube = 0
        current_tier = start_tier - 1

        while current_tier != LEGENDARY:
            cost += cube_cost[cube]
            num_of_cube += 1

            result = np.random.choice(2, p=prob_table[cube][current_tier])

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
