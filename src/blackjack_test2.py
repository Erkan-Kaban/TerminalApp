# Importing pip package CardGame, importing my own deck module.
import sys, traceback
from multiprocessing.sharedctypes import Value
from CardGame.Blackjack.money import Money
from deck import Deck


# Inheriting Money class from pip packages.
class Blackjack(Money):
    def blackjack_table(self) -> None:
        print(
            "Welcome to BlackJack! \nYou as the player will start with $500 credits \n "
        )
        print("Please place your bet")

    def player(self, buy_in=500) -> None:
        # A try block, if user ctrl+c out we catch it and exit gracefully by letting the user know.
        try:
            bet_amount = 0
            # The Loop of the game, so that we can play a fresh hand at the end of every game.
            while True:
                # An if statement once we hit 0 to ask the user to rebuy an amount.
                if self.value == 0:
                    # A while loop to try users entered amount, max is 1000 and doesn't allow for any negative numbers, or other characters.
                    while True:
                        try:
                            rebuy = input(
                                "You've run out of credits, please select rebuy amount (max $1000): $"
                            )
                            while int(rebuy) > 1000:
                                rebuy = input(
                                    "Please enter less or equal to 1000 rebuy amount: $"
                                )
                            # Using the money package to rebuy with the amount inputted above.
                            self.__init__(int(rebuy))
                            break
                        # If there is a value error such as 0 we ask the user to enter a valid option below.
                        except ValueError:
                            print("Please enter a valid amount, $1 > $1000")

                # Need a variable to keep count of the players hand value total.
                player_hand_total = 0
                # The shuffle module is called from my cards module.
                cards.shuffle()
                print("Cards are shuffling")
                # Player can make a bet up to and including their credit amount.
                print(f"Your current credits are: ${self.value}")
                bet_amount = self.bet()
                # Draw_cards called under deck.py to deal a card to player
                player_hand = cards.draw_cards("Deal")
                # Contain the players card value in a variable player_hand_value
                player_hand_value = cards.get_values(player_hand)
                print("Your hand is: \n")
                # Prints players hand
                print(str(player_hand) + "\n")
                player_hand_total += self.get_values(player_hand_value)
                # Prints the total in a string
                print("Total of: " + str(player_hand_total) + "\n")

                # Checking if player has less than 21, while that's True, we will be looping through here.
                while player_hand_total < 21:
                    players_choice = input(
                        "Would you like to hit(another card) or stand(stay) (h/s)? "
                    )

                    if players_choice == "h":
                        player_hand_total = 0
                        player_hand += cards.draw_cards("Draw")
                        player_hand_value = cards.get_values(player_hand)
                        print(player_hand)
                        player_hand_total += self.get_values(player_hand_value)
                        print("Total of: " + str(player_hand_total) + "\n")
                    # An if statement that checks if the user has gone over 21.
                    if player_hand_total > 21:
                        print("Bust! You went over 21! you lose" + "\n")
                        # Prints the remaining value for player.
                        print(f"You have: ${self.value} remaining")

                    if players_choice == "s":
                        # Dealer function activates, plays cards till they hit above 17.
                        dealer_hand_total = self.dealer()
                        if player_hand_total > dealer_hand_total:
                            # Self value is the players total credits.
                            print("You Win!!")
                            print("test one")
                            self.value += bet_amount * 2
                            break
                        elif dealer_hand_total > 21:
                            print("test two")
                            print("You Win!!")
                            self.value += bet_amount * 2
                            break
                        elif player_hand_total == dealer_hand_total:
                            print("Push!! - Draw bet is refunded")
                            self.value += bet_amount
                            break
                        else:
                            ("test three")
                            print("Dealer wins!")
                            break
                # Checks for blackjack
                if player_hand_total == 21:
                    # Using the money.py function named blackjack.
                    self.blackjack(bet_amount)
                    print("Your total credits are now: " + str(self.value) + "\n")
        except KeyboardInterrupt:
            print("/n")
            print("Shutdown requested...exiting")
        except Exception:
            traceback.print_exc(file=sys.stdout)
        sys.exit(0)
        # Seperated this code into a function so I'm repeating code less times.

    def dealer(self):
        dealer_hand_total = 0
        while dealer_hand_total < 17:
            dealer_hand = cards.draw_cards("Draw")
            dealer_hand_value = cards.get_values(dealer_hand)
            print("Dealer deals:")
            print(dealer_hand)
            dealer_hand_total += self.get_values(dealer_hand_value)
            print("Total of: " + str(dealer_hand_total) + "\n")
        return dealer_hand_total

    def get_values(self, values):
        player_hand_total = 0
        for key, value in values.items():
            player_hand_total += values[key]
        return player_hand_total


table = Blackjack()
table.blackjack_table()
cards = Deck()
player = Blackjack()
player.player()
dealer = Blackjack()
dealer.dealer()
