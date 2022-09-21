# Importing pip package CardGame, importing my own deck module.
from CardGame.Blackjack.money import Money
from deck import Deck

# Inheriting Money class from pip packages.
class Blackjack(Money):
    def blackjack_table(self, person) -> None:
        print('Welcome to BlackJack! \nYou as the player will start with $500 credits \n ')
        print('Please place your bet')
        print("Enter if you would like to stand or hit by typing 's' or 'h'")

    def player(self, buy_in = 500) -> None:
        while(True):
            if self.value == 0:
                rebuy = input("You've run out of credits, please select rebuy amount: $")
                # Using the money package to rebuy.
                self.__init__(int(rebuy))
            # Need a variable to keep count of the players hand value total.
            player_hand_total = 0
            # The shuffle module is called from my cards module.
            cards.shuffle()
            print('Cards are shuffling')
            # Player can make a bet up to and including 500.    
            bet_amount = self.bet()
            # Draw_cards called under deck.py to deal a card to player
            player_hand = cards.draw_cards('Deal')
            # Contain the players card value in a variable player_hand_value
            player_hand_value = cards.get_values(player_hand)
            print('Your hand is: \n')
            # Prints players hand
            print(str(player_hand) + "\n")
            player_hand_total += self.get_values(player_hand_value)
            # Prints the total in a string
            print('Total of: ' + str(player_hand_total) + '\n')

            # Checking if player has less than 21, while that's True, we will be looping through here.
            while(player_hand_total < 21):
                player_hand_total = 0
                players_choice = input('Do you want to (h) hit or (s) stand: ')
                if players_choice == 's':
                    # Dealer function activates, plays cards till they hit above 17.
                    # self.dealer()
                    dealer_hand_value = self.dealer()
                    if player_hand_total > dealer_hand_value:
                        print('You win!!') #<< gotta work this out.
                        break
                    else:
                        print('Dealer wins!!')
                        break
                if players_choice == 'h':
                    player_hand += cards.draw_cards("Draw")
                    player_hand_value = cards.get_values(player_hand)
                    print(player_hand)
                    player_hand_total += self.get_values(player_hand_value)
                    print('Total of: ' + str(player_hand_total) + '\n')
                # An if statement that checks if the user has gone over 21.
                if player_hand_total > 21:
                    print('Bust! You went over 21! you lose' + '\n')
                    # Prints the remaining value for player.
                    print(f'You have: {self.value} remaining')
            # Checks for blackjack
            if player_hand_total == 21:
                self.blackjack(bet_amount)
                self.value += bet_amount * 2.5
                print('Your total credits are now: ' + str(self.value) + '\n')
    # Seperated this code into a function so I'm repeating code less times. 
    def dealer(self):
        dealer_hand_total = 0
        while(dealer_hand_total < 17):
            dealer_hand = cards.draw_cards('Draw')
            dealer_hand_value = cards.get_values(dealer_hand)
            print('Dealer deals:')
            print(dealer_hand)
            dealer_hand_total += self.get_values(dealer_hand_value)
            print('Total of: ' + str(dealer_hand_total) + '\n')
        return dealer_hand_total


    def get_values(self, values):
        player_hand_total = 0
        for key, value in values.items():
            player_hand_total += values[key]
        return player_hand_total 

cards = Deck()

player = Blackjack()
player.player()
dealer = Blackjack()
dealer.dealer()
