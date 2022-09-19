from cards import Cards
from random import shuffle
# import itertools

# Class inherits from the cards module.
class Deck(Cards):
    # Initialize with a deck of cards from the card_option() function.
    def __init__(self) -> None:
        self.deck_of_cards = self.card_options()
        self.deck_of_cards = list(self.deck_of_cards)

    # Initialize shuffle for the deck of cards. 
    def shuffle(self) -> None:
        shuffle(self.deck_of_cards)
    
    # Depending on the selection, we get a certain amount of cards drawn.
    def draw_cards(self, value):
        if value == "Deal": # If we select to deal we draw 2 cards.
            value = -2
        else: # Else draw a single card
            value = -1
        self.hand = self.deck_of_cards[value:]
        del self.deck_of_cards[value:]
        return self.hand

#Testing cards as a fresh deck, using the shuffle and draw cards.
# cards = Deck()
# cards.shuffle()
# hand = cards.draw_cards("Deal")
# hand_value = cards.get_values(hand)
# print(hand_value)

