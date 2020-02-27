class Card():

    def __init__(self, origin=None, destination=None, seat=None, method=None):
        self.origin = origin
        self.destination = destination
        self.seat = seat
        self.method = method
        self.next_card = None
        self.prev_card = None

    def __str__(self):
        return "{} {} {} {}".format(self.origin, self.destination, self.seat, self.method)

class Sort():

    def __init__(self, algorithm=None):
        self.algorithm = self.default_sort if algorithm is None else algorithm

    def default_sort(self, cards):
        length = len(cards)

        origins = {}
        destinations = {}

        """
        Loop thru the cards once.

        We want to keep track of pointers to the next (and previous) card
        which are basically the destination and origin.
        """
        for card in cards:
            origins[card.origin] = card
            destinations[card.destination] = card
            if card.destination in origins:
                card.next_card = origins[card.destination] 
                origins[card.destination].prev_card = card
            if card.origin in destinations:
                destinations[card.origin].next_card = card
                card.prev_card = destinations[card.origin]

        """
        Cards at this point all have the prev and next pointers but are not "in order".
        """
        sorted_cards = []
        next_card = list(filter(lambda x: (x.prev_card is None), cards))[0]
        sorted_cards.append(next_card)
        while next_card is not None:
            next_card = next_card.next_card
            if next_card:
                sorted_cards.append(next_card)
        return sorted_cards

    def handle(self, cards):
        return self.algorithm(cards)

"""
BELOW IS BASICALLY TEST CODE
"""

import csv
import random

"""
cards = []
with open('passes.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        card = Card(row['origin'], row['destination'], row['seat'], row['method'])
        cards.append(card)

random.shuffle(cards)

print("SHUFFLED CARDS")

for card in cards:
    print(card)

print("RUNNING SORT")
sorted_cards = Sort().handle(cards)
for card in sorted_cards:
    print(card)
"""

def test():
    cards = []
    with open('passes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            card = Card(row['origin'], row['destination'], row['seat'], row['method'])
            cards.append(card)
    
    random.shuffle(cards)
    sorted_cards = Sort().handle(cards)
    assert(sorted_cards[0].origin == 'AAA')
    assert(sorted_cards[1].origin == 'BBB')
    assert(sorted_cards[2].origin == 'CCC')
    assert(sorted_cards[3].origin == 'DDD')
    assert(sorted_cards[4].origin == 'EEE')
    assert(sorted_cards[5].origin == 'FFF')
    assert(sorted_cards[6].origin == 'GGG')
    assert(sorted_cards[7].origin == 'HHH')

test()
test()
test()
test()
test()
test()
test()
test()
