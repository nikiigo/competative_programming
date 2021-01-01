# -*- coding: utf-8 -*-
import itertools
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def main():
    n = int(input())
    a = []
    for s in range(n):
        a.append(list(map(int, input().split())))
    logging.debug('{}'.format(a))
    result = []
    min_cost = 0
    for i, p in enumerate(itertools.permutations(list(range(1, n + 1)))):
        logging.debug('{} {}'.format(i, p))
        my_cost = 0
        for j in range(n - 1):
            logging.debug('{} {} {}'.format(j, p[j], p[j + 1]))
            my_cost += a[p[j] - 1][p[j + 1] - 1]
        if i == 0:
            min_cost = my_cost
            result = p
        else:
            if my_cost < min_cost:
                min_cost = my_cost
                result = p
            else:
                pass
    print(" ".join(map(str, result)))


if __name__ == '__main__':
    main()
