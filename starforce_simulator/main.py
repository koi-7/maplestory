#!/usr/bin/env python3
# coding: utf-8


import numpy as np
from table import meso_table, prob_table


SUCCESS  = 0
FAIL     = 1
DECREASE = 2
DESTROY  = 3


def main():
    cost_list = []
    destroy_list = []

    star_goal = int(input('目標スター数: '))
    eq_lev = int(input('装備レベル: '))

    for _ in range(1000):
        star = 0
        cost = 0
        destroy_count = 0

        while star != star_goal:
            cost += meso_table[eq_lev][star]

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
        destroy_list.append(destroy_count)

    print('平均費用: ' + "{:,}".format(np.average(cost_list)) + ' メル')
    print('平均破壊回数: ' + "{:,}".format(np.average(destroy_list)) + ' 回')


if __name__ == '__main__':
    main()
