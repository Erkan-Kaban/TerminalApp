from CardGame.Blackjack.money import Money
from deck import Deck

cards = Deck()
# Player starts at 100 credits.



class Blackjack(Money):
    def blackjack_table(self) -> None:
        print("Welcome to BlackJack! \nYou as the player will start with 500 credits \n ")
        # Cards are shuffled.
        cards.shuffle()
        print("Cards are shuffling")
        
    
    def player(self, credits = 500) -> None:
        player_money = Money() # Instance of a class here
        player_hand_total = 0
        # player can make a bet up to and including 500.
        bet_amount = player_money.bet()
        player_hand = cards.draw_cards("Deal")
        player_hand_value = cards.get_values(player_hand)
        print("Your hand is: \n")
        print(player_hand)

        for key, value in player_hand_value.items():
            player_hand_total += player_hand_value[key]

        print('Total of: ' + str(player_hand_total))
        player_hand_total = 21 
        if player_hand_total == 21:
            player_money.blackjack(bet_amount)
            credits += bet_amount * 2.5
            print(credits) 
            
    



table = Blackjack()
table.blackjack_table()
table.player()




