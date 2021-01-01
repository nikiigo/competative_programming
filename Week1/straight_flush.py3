# -*- coding: utf-8 -*-
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def main():
    my_cards = list(map(str, input().split()))
    card_ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    my_suits = set([x[1] for x in my_cards])
    if (len(my_suits)) > 1:
        print('NO')
    else:
        rank_map = {c: i for i, c in enumerate(card_ranks)}
        my_by_number = [rank_map[card[0]] for card in my_cards]
        my_by_number.sort()
        logging.debug('{}'.format(my_by_number))
        if my_by_number[4] - my_by_number[0] == 4:
            print('YES')
        elif my_by_number[4] == 13 and my_by_number[3] == 4:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
