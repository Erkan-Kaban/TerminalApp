from CardGame.Blackjack.money import Money
from deck import Deck


class Blackjack(Money):
    def blackjack_table(self) -> None:
        print("Welcome to BlackJack! \nYou as the player will start with 500 credits \n ")
        # Cards are shuffled.
        cards.shuffle()
        print("Cards are shuffling")     

    # Player starts at 500 credits.
    def player(self, credits = 500) -> None:
        while(True):
            player_money = Money() # Instance of a class here from money.py
            player_hand_total = 0
            # player can make a bet up to and including 500.
            bet_amount = player_money.bet()
            # Draw_cards called under deck.py to deal a card to player
            player_hand = cards.draw_cards("Deal")
            # Contain the players card value in a variable player_hand_value
            player_hand_value = cards.get_values(player_hand)
            print("Your hand is: \n")
            # Prints players hand
            print(player_hand)

            
            player_hand_total += self.get_values(player_hand_value)
            # Prints the total in a string
            print('Total of: ' + str(player_hand_total))
        
            while(player_hand_total < 21):
                player_hand_total = 0
                players_choice = input('Do you want to (h) hit or (s) stand: ')
                if players_choice == 's':
                    pass #let the dealer play from here. < need to do something here.
                if players_choice == 'h':
                    player_hand += cards.draw_cards("Draw")
                    player_hand_value = cards.get_values(player_hand)
                    print(player_hand)
                    # for key, value in player_hand_value.items():
                        # player_hand_total += player_hand_value[key]
                    player_hand_total += self.get_values(player_hand_value)
                    print('Total of: ' + str(player_hand_total))
                    if player_hand_total > 21:
                        print("Bust! You went over 21! you lose")

            if player_hand_total == 21:
                player_money.blackjack(bet_amount)
                credits += bet_amount * 2.5
                print("Your total credits are now: " + str(credits))   

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
table.player()
    



    



