import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def infinite_sequence(x, y):
    a, i = 0, 0
    while True:
        yield a, i
        i += 1
        if i % 2 == 1:
            a += x
        else:
            a -= y


def main():
    x, y, z = map(int, input().split())
    result = -1

    seq = (infinite_sequence(x, y))
    # i=0 is a special case and it is handled by z = 0
    a, i = next(seq)
    while True:
        a, i = next(seq)
        # z=0 is a special case . We know solution and it is the only one when i=0
        if z == 0:
            result = 0
            break
        # if x > y then the odd and even parts of the sequence are ascending
        elif x > y:
            if z > a:
                logging.debug('z > a, a and i: {} {}'.format(a, i))
                continue
            elif z == a:
                result = i
                break
            else:
                a, i = next(seq)
                while z > a:
                    # We have to check now only the sequence elements with indez having current parity
                    logging.debug('z > a, second loop, a and i: {} {}'.format(a, i))
                    a, i = next(seq)
                    a, i = next(seq)
                if z == a:
                    result = i
                else:
                    break
        # if x < y then the odd and even parts of the sequence are descending
        elif x < y:
            if z < a:
                logging.debug('z < a, a and i: {} {}'.format(a, i))
                continue
            elif z == a:
                result = i
                break
            else:
                a, i = next(seq)
                while z < a:
                    # We have to check now only the sequence elements with indez having current parity
                    logging.debug('z < a, second loop, a and i: {} {}'.format(a, i))
                    a, i = next(seq)
                    a, i = next(seq)
                if z == a:
                    result = i
                else:
                    break
        else:
            # if x = y and z <> 0 then we have such element with index 1 only when x=z
            if z == a:
                result = i
            else:
                break
    print(result)


if __name__ == '__main__':
    main()
