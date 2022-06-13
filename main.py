import itertools
# for deck creation
import random
# random number gen
from collections import Counter
# used dictionaries (Counter)
import time
# for statistics

royal = False
# boolean
start_time = time.time()
# init time
iteration = 1
# count interations
while not royal:
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    # values for cards
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    # four suits of cards
    deck = list(itertools.product(vals, suits))
    # deck is not a hand this generates a deck with itertools
    random.shuffle(deck)
    # shuffle deck
    poker_hand = deck[0:5]  # take first five random values for hand
    # poker_hand = [('king', 'clubs'), ('ace', 'clubs'), ('queen', 'clubs'), ('jack', 'clubs'), ('10', 'clubs')]
    # test victory hand above
    poker_hand_vals = []
    # array for vals
    poker_hand_suits = []
    # array for suits
    print()
    print('Your hand:')
    for val, suit in poker_hand:
        poker_hand_vals.append(val)
        # append to new arrays for card logic
        poker_hand_suits.append(suit)
        # append to new arrays for card logic
        print('The %s of %s' % (val, suit))
        # print method for 5 different cards in hand
    # print(poker_hand)
    # print(poker_hand_vals,poker_hand_suits)

    suit_counter = Counter(poker_hand_suits)
    # create new Counter object for suits
    val_counter = Counter(poker_hand_vals)
    # create new Counter object for vals

    # print()
    # dictionaries
    # print(val_counter.most_common(13))
    # count the occurrences of values
    # print(suit_counter.most_common(4))
    # count the occurrences of suits
    new_val_list = []
    # seperate the five future values of the hand
    for i in suit_counter.most_common(1):
        # the most common suit
        y = str(i[1]) + " of a kind"
        # "5 of a kind"
    for i in val_counter.most_common(5):
        # for the five cards
        new_val_list.append(i[0])
        # append every value to a new list
    if sorted(new_val_list) == ['10', 'ace', 'jack', 'king', 'queen'] and y == "5 of a kind":
        royal = True
        print("Royal Flush")
        print("--- %s seconds ---" % (time.time() - start_time))
        print("--- %s hands ---" % iteration)
    iteration += 1
