from random import shuffle
from collections import defaultdict


def targets_drawn(targets_left, cards_left, cards_drawn):
    good_cards = [1] * targets_left
    bad_cards = [0] * (cards_left - targets_left)
    deck = good_cards + bad_cards

    hits = defaultdict(int)

    trials = 10 ** 4

    for _ in range(trials):
        shuffle(deck)
        num_hits = sum(deck[:cards_drawn])
        hits[num_hits] += 1

    for hit in hits:
        hits[hit] = hits[hit] / float(trials)

    return hits
