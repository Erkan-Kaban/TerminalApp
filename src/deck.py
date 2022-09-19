import cards
from random import shuffle

# class Deck
# Created an instance of cards.
deck_of_cards = cards.cards()
# Assigned new_deck variable with card options.
new_deck = deck_of_cards.card_options()
# converted into a list as dictionary cannot be used in the random shuffle method.
list_of_cards = list(new_deck.items())
# Shuffling cards
shuffle(list_of_cards)

# Converting back to a dictionary
result = dict(list_of_cards)
print(result)
print(len(result))