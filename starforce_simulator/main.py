#!/usr/bin/python3
# coding: utf-8


import numpy as np
from table import meso_table, prob_table


SUCCESS  = 0
FAIL     = 1
DECREASE = 2
DESTROY  = 3


def main():
    star = 0
    cost = 0

    star_list = []

    while star != 17:
        cost += meso_table[star]
        star_list.append(star)

        result = np.random.choice(4, p=prob_table[star])

        if result == SUCCESS:
            star += 1
        elif result == FAIL:
            pass
        elif result == DECREASE:
            star -= 1
        elif result == DESTROY:
            star_list.append('d')
            star = 12

    print()
    print(star_list)
    print()
    print('{:,} メル'.format(cost))
    print()



if __name__ == '__main__':
    main()
