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

        # This loop gets the players hand (two cards and adds up the sum value)
        for key, value in player_hand_value.items():
            player_hand_total += player_hand_value[key]
        
        # Prints the total in a string
        print('Total of: ' + str(player_hand_total))
        
        # if player_hand_total == 21:
        #     player_money.blackjack(bet_amount)
        #     credits += bet_amount * 2.5
        #     print("Your total credits are now: " + str(credits))   
        # else:
        while(player_hand_total < 21):
            player_hand_total = 0
            players_choice = input('Do you want to (h) hit or (s) stand: ')
            if players_choice == 'h':
                player_hand += cards.draw_cards("Draw")
                player_hand_value = cards.get_values(player_hand)
                print(player_hand)
                # print(player_hand_value)
                for key, value in player_hand_value.items():
                    player_hand_total += player_hand_value[key]
                print('Total of: ' + str(player_hand_total))
                if player_hand_total > 21:
                    print("Bust!")
                    break
    
                
        if player_hand_total == 21:
            player_money.blackjack(bet_amount)
            credits += bet_amount * 2.5
            print("Your total credits are now: " + str(credits))   
                    

# Creating an instance of Deck to get handed a new deck.  
cards = Deck()
table = Blackjack()
table.blackjack_table()
table.player()
    



    



