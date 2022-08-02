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

    star_start = int(input('開始スター数: '))
    star_goal = int(input('目標スター数: '))
    eq_lev = int(input('装備レベル（130、140、150、160）: '))
    event1 = int(input('30%オフイベント（0: OFF、1: ON）: '))
    event2 = int(input('確定イベント（0: OFF、1: ON）: '))

    for _ in range(1000):
        star = star_start
        cost = 0
        destroy_count = 0

        while star != star_goal:
            if event1:
                cost += meso_table[eq_lev][star] * 0.7
            else:
                cost += meso_table[eq_lev][star]

            result = np.random.choice(4, p=prob_table[star])

            if event2 and (star == 5 or star == 10 or star == 15):
                result = SUCCESS

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

    print('------------------------------')
    print('平均費用: ' + "{:,}".format(np.average(cost_list)) + ' メル')
    print('最大費用: ' + "{:,}".format(max(cost_list)) + ' メル')
    print('平均破壊回数: ' + "{:,}".format(np.average(destroy_list)) + ' 回')
    print('最大破壊回数: ' + "{:,}".format(max(destroy_list)) + ' 回')


if __name__ == '__main__':
    main()
