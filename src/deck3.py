from cards import Cards
from random import shuffle
# import itertools

class Deck(Cards):
    def __init__(self) -> None:
        self.deck_of_cards = self.card_options()
        self.deck_of_cards = list(self.deck_of_cards)
        # print(self.deck_of_cards)

    def shuffle(self) -> None:
        shuffle(self.deck_of_cards)
        # print(self.deck_of_cards)
        # self.result = dict(self.deck_of_cards) # changes to dictionary
        # print(self.result)
        # print(len(result))
    
    def draw_cards(self) -> None:
        self.hand = self.deck_of_cards[-2:]
        del self.deck_of_cards[-2:]
        return self.hand
        
        # self.hand = dict(itertools.islice(self.result.items(), 2))
        # del self.hand[0]
        # for k, v in self.result:
        #     self.result.popitem(k)
        # self.result.popitem([0:1])
        # print(self.hand)
        # # print(len(self.result))
        # print(self.result)
        # self.hand = self.deck_of_cards[1 :: 2]
        # print(len(self.hand))
        # print(self.hand[0])
        
    def get_values(self, cards):
        card_value = {}
        for card in cards:
            for character in card:
                if character.isdigit():
                    card_value[card] = int(card[0])
                elif card.startswith("A"):
                    card_value[card] = 11
                elif card.startswith("10") or card.startswith(character):
                    card_value[card] = 10
        return card_value



cards = Deck()
cards.shuffle()
hand = cards.draw_cards()
hand_value = cards.get_values(hand)
print(hand_value)
# cards.shuffle()
# cards.draw_cards()