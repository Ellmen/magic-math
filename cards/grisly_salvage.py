# Calculates how frequently grisly salvage will hit a certain
# card, given the number of cards left in the deck

from hit import targets_drawn

def grisly_salvage(cards_played = 9, targets_left = 4):
    cards_left = 60 - targets_left - cards_played
    cards_drawn = 5
    return targets_drawn(targets_left, cards_left, cards_drawn)[0]
