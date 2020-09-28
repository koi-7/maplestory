#!/usr/bin/python3
# coding: utf-8


import numpy as np
from table import meso_table, prob_table


SUCCESS  = 0
FAIL     = 1
DECREASE = 2
DESTROY  = 3


def main():
    cost_list = []

    for _ in range(10):
        star = 0
        cost = 0

        while star != 17:
            cost += meso_table[star]

            result = np.random.choice(4, p=prob_table[star])

            if result == SUCCESS:
                star += 1
            elif result == FAIL:
                pass
            elif result == DECREASE:
                star -= 1
            elif result == DESTROY:
                star = 12

        cost_list.append(cost)
        print(cost)

    print('平均: {:,} メル'.format(np.average(cost_list)))


if __name__ == '__main__':
    main()
