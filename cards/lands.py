from hit import targets_drawn

# Calculates how many lands you can expect in a hand,
# given the number of lands in the deck

def lands(lands_in_deck = 24, cards_drawn = 7):
    return targets_drawn(lands_in_deck, 60, cards_drawn)

# Calculates the probability of at least n lands in a hand,
# given the number of lands in the deck

def at_least_n_lands(n, lands_in_deck = 24, cards_drawn = 7):
    prob = 0.0
    land_dict = lands(lands_in_deck, cards_drawn)
    for number in land_dict:
        if number >= n:
            prob += land_dict[number]

    return prob

# A print function for the land utilities

def print_lands(lands_in_deck = 24, cards_drawn = 7, at_least_n = -1):
    land_dict = lands(lands_in_deck, cards_drawn)
    for number in land_dict:
        print "The probability of {} lands is: {}%".format(
            number,
            land_dict[number] * 100
        )
    
    if at_least_n != -1:
        prob = 0.0
        for number in land_dict:
            if number >= at_least_n:
                prob += land_dict[number]
        print "The probability of hitting at least {} lands is {}%".format(
            at_least_n,
            prob * 100
        )
