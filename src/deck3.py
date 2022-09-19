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
    
    # Draw "two" cards from the current deck.
    def draw_cards(self) -> None:
        self.hand = self.deck_of_cards[-2:]
        del self.deck_of_cards[-2:]
        return self.hand
        
       
        
    


#Testing cards as a fresh deck, using the shuffle and draw cards.
cards = Deck()
cards.shuffle()
hand = cards.draw_cards()
hand_value = cards.get_values(hand)
print(hand_value)
