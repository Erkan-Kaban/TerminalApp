from cards import Cards
from random import shuffle

class Deck(Cards):
    def deck_of_cards(self) -> None:
        deck_of_cards = self.card_options()
        deck_of_cards = list(deck_of_cards.items())
        shuffle(deck_of_cards)
        deck_of_cards = dict(deck_of_cards)
        print(deck_of_cards)

cards = Deck()
cards.deck_of_cards()