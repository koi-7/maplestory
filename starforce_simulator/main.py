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
    destroy_count = 0

    for _ in range(600):
        star = 0
        cost = 0

        while star != 17:
            cost += meso_table[160][star]

            result = np.random.choice(4, p=prob_table[star])

            if result == SUCCESS:
                star += 1
            elif result == FAIL:
                pass
            elif result == DECREASE:
                star -= 1
            elif result == DESTROY:
                destroy_count += 1
                star = 12

        cost_list.append(cost)

    print('平均費用: {:,} メル'.format(np.average(cost_list)))
    print('破壊回数: ' + str(destroy_count) + ' 回')


if __name__ == '__main__':
    main()
