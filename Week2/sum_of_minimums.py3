import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
sys.setrecursionlimit(10**6)
res_sum = 0


def build_tree(a):
    global res_sum
    if len(a) > 0:
        i, my_sum = my_min(a)
        logging.debug('i={} my_sum={} a={}'.format(i, my_sum, a))
        res_sum += my_sum
        return build_tree(a[:i]), build_tree(a[i + 1:])
    else:
        logging.debug('a={}'.format(a))


def my_min(a):
    min_cost, min_index = a[0], 0
    for i, value in enumerate(a):
        if i != 0 and value < min_cost:
            min_cost = value
            min_index = i
    if min_index == 0 or min_index == (len(a) - 1):
        pi = len(a)
    else:
        pi = (min_index + 1) * (len(a) - min_index)
    logging.debug(' len(a)={} min_index={} a={}'.format(len(a), min_index, a))
    return min_index, min_cost * pi


def main():
    global res_sum
    n = int(input())
    a = list(map(int, input().split()))
    logging.debug(len(a))
    build_tree(a)
    print(res_sum)


if __name__ == '__main__':
    main()
