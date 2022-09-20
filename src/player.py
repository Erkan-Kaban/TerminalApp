from CardGame.Blackjack.money import Money
from deck import Deck
from player1 import Player

class Blackjack(player):
    def blackjack_table(self) -> None:
        print('Welcome to BlackJack! \nYou as the player will start with $500 credits \n ')
        player.player()
         


    # This loop function gets the players hand (two cards and adds up the sum value)              
    def get_values(self, values):
        player_hand_total = 0
        for key, value in values.items():
            player_hand_total += values[key]
        return player_hand_total

# Creating an instance of Deck to get handed a new deck.  
cards = Deck()
table = Blackjack()
table.blackjack_table()
#table.player()
player = Player()
    



    



