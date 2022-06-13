import itertools
import random
from collections import Counter
import time

royal = False
start_time = time.time()
iteration = 1
while royal == False:
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    # values
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    # four suits
    deck = list(itertools.product(vals, suits))

    random.shuffle(deck)  # shuffle

    poker_hand = deck[0:5]  # take first five random values for hand
    # poker_hand = [('king', 'clubs'), ('ace', 'clubs'), ('queen', 'clubs'), ('jack', 'clubs'), ('10', 'clubs')]
    poker_hand_vals = []
    poker_hand_suits = []
    c = 0
    print()
    print('Your hand:')
    for val, suit in poker_hand:
        poker_hand_vals.append(val)
        poker_hand_suits.append(suit)
        print('The %s of %s' % (val, suit))
    # print(poker_hand)
    # print(poker_hand_vals,poker_hand_suits)

    suit_counter = Counter(poker_hand_suits)
    val_counter = Counter(poker_hand_vals)
    # print()
    # dictionaries
    # print(val_counter.most_common(13))
    # count the occurrences of values
    # print(suit_counter.most_common(4))
    # count the occurrences of suits

    x = []
    for i in suit_counter.most_common(1):
        # the most common suit
        y = str(i[1]) + " of a kind"
        # the occurance ofthe most common suit
    for i in val_counter.most_common(5):
        # for the five cards
        x.append(i[0])

        # append every value to a new list
    if sorted(x) == ['10', 'ace', 'jack', 'king', 'queen'] and y == "5 of a kind":
        royal = True
        print("Royal Flush")
        print("--- %s seconds ---" % (time.time() - start_time))
        print("--- %s hands ---" % iteration)
    iteration += 1
