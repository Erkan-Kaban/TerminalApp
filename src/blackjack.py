from CardGame.Blackjack.money import Money
from deck import Deck

player_value = 0
print("Welcome to BlackJack! \n You as the player will start with 100 credits \n ")
# player starts at 100 credits.
player_money = Money() #instance of a class here
# player can make a bet up to and including 100.
bet_amount = player_money.bet()


# Cards are supplied and shuffled.
cards = Deck()
cards.shuffle()
print("Cards are shuffling")
player_hand = cards.draw_cards("Deal")
player_hand_value = cards.get_values(player_hand)
print("Your hand is: \n")
print(player_hand)
for card_values in player_hand_value:
    player_value += player_hand_value[card_values]

print('Total of: ' + str(player_value))
player_value = 21
if player_value == 21:
    player_money.blackjack(bet_amount)