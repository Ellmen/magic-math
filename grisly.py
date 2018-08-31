# Calculates how frequently grisly salvage will hit a certain
# card, given the number of cards left in the deck

from random import shuffle

good_cards = ['good'] * 4
bad_cards = ['bad'] * (60 - len(good_cards))

num_cards_played = 9

played = bad_cards[:num_cards_played]
deck = good_cards + bad_cards[num_cards_played:]

hits = 0

trials = 10 ** 4

for _ in range(trials):
   shuffle(deck)
   if 'good' in deck[:5]:
       hits += 1

print hits / float(trials)
