# Blackjack game function
# Importing pip package CardGame, importing my own deck module.
import sys, traceback
import clearing
from multiprocessing.sharedctypes import Value
from CardGame.Blackjack.money import Money
from deck import Deck
from colorama import Fore, init
init(autoreset=True)

class Blackjack(Money):
    def blackjack_table(self) -> None:
        print("Welcome to BlackJack! \nYou as the player will start with $500 credits")
        print("To quit press ctrl+c at any time whilst at play or press n at the end of play \n")

    # Player functionality
    def player(self, value=500) -> None:
        # Self.value is inherited by the money.py package and is the players total credits.
        self.value = value
        # A try block, if user ctrl+c out we catch it and exit gracefully by letting the user know.
        game_over = False
        try:
            # We need a bet amount variable to keep count of how much we bet on each hand.
            bet_amount = 0
            # The Loop of the game, so that we can play a fresh hand at the end of every game.
            while True:
                if game_over is True:
                    clearing.clear()
                    print("Thank you for playing Blackjack :)")
                    sys.exit(0)
                # An if statement once we hit 0 to ask the user to rebuy an amount.
                if self.value == 0:
                    # We go into game over function and try to get an amount from user.
                    rebuy = self.game_over()
                    # We reinitialize our value and rebuy credits.
                    self.__init__(int(rebuy))
                # Calling function to get a bet amount from player and saving it to a variable bet_amount.
                bet_amount = self.bet_amount()
                # play_hand is a function that saves the players hand visually.
                player_hand = self.players_hand()
                # The players total hand value.
                player_hand_total = self.deal_cards(player_hand, bet_amount)
                
                # Checking if player has less than 21, while that's True, we will be looping through here.
                while player_hand_total < 21:
                    players_choice = input("Would you like to hit(another card) or stand(stay) (h/s)? ")
                    # When player selects h as hit we call player_hit function that get's us the players total hand value after hitting.
                    if players_choice == "h":
                        # Call player_hit function and return the players hand and add up to total.
                        player_hand_total = self.player_hit(player_hand, player_hand_total, bet_amount)
                    # When the player selects s as stand we stop player, and let the dealer play. and we calculate our winning/loss and break out of the loop.
                    if players_choice == "s":
                        win_loss = self.player_stand(player_hand_total, bet_amount)
                        self.value = win_loss
                        break

                # When the game is over we ask the user if they would like to quit or play again and place it in a variable.
                game_over = player.play_again()
        except KeyboardInterrupt:
            print("/n")
            print("Shutdown requested...exiting")
        except Exception:
            traceback.print_exc(file=sys.stdout)
        sys.exit(0)

    # Dealer function activates, plays cards till they hit above 17.
    def player_stand(self, player_hand_total, bet_amount):
        dealer_hand_total = self.dealer()
        # After the dealer has dealt cards to itself, we check the variance between player and dealer, calculate who won or lost, and winnings or loss.
        if player_hand_total > dealer_hand_total:
            print(Fore.YELLOW + "You Win!!")
            self.value += bet_amount * 2
            print("Your total credits are now: $" + Fore.YELLOW + str(self.value) + "\n")
            return self.value
        elif dealer_hand_total > 21:
            print(Fore.YELLOW + "Dealer busts!! You Win!!")
            self.value += bet_amount * 2
            print("Your total credits are now: $" + Fore.YELLOW + str(self.value) + "\n")
            return self.value
        elif player_hand_total == dealer_hand_total:
            print(Fore.RED + "Push!! - Draw!! Bet is refunded")
            self.value += bet_amount
            print("Your total credits are now: $" + Fore.YELLOW + str(self.value) + "\n")
            return self.value
        else:
            print(Fore.RED + "Dealer wins!")
            self.value -= bet_amount
            print("Your total credits are now: $" + Fore.RED + str(self.value) + "\n")
            return self.value
        
    # A function when called player gets dealt a single card.
    def player_hit(self, player_hand, player_hand_value, bet_amount):
        player_hand_total = 0
        # Drawing a single card at every hit.
        player_hand += cards.draw_cards("Draw")
        player_hand_value = cards.get_values(player_hand)
        print(Fore.CYAN + str(player_hand))
        player_hand_total = self.get_values(player_hand_value)
        print("Total of: " + str(player_hand_total) + "\n")
        if player_hand_total < 21:
            return player_hand_total
        if player_hand_total == 21:
            # Using the money.py function named blackjack.
            self.blackjack(bet_amount)
            print(Fore.YELLOW + "Thats Blackjack!!")
            print("Your total credits are now: $ " + str(self.value) + "\n")
            return player_hand_total
        if player_hand_total > 21:
            print(Fore.RED + "Bust! You went over 21! you lose" + "\n")
            # Prints the remaining value for player.
            print(f"You have: ${self.value} remaining")
            return player_hand_total
            

    # A Function that returns the players hand visually.
    def players_hand(self):
        # Draw_cards called under deck.py to deal a card to player
        player_hand = cards.draw_cards("Deal")
        return player_hand

    # Returns the bet amount player has made.
    def bet_amount(self):
        cards.shuffle()
        print(Fore.GREEN + "Cards are shuffling")
        print(Fore.CYAN + f"Your current credits are: ${self.value}")
        bet_amount = self.bet()
        return bet_amount

    # A function that deals the player two cards.
    def deal_cards(self, player_hand, bet_amount):
            # Need a variable to keep count of the players hand value total.
        player_hand_total = 0
        player_hand_value = cards.get_values(player_hand)
        print("\n Your hand is: \n")
        # Prints players hand
        print(Fore.CYAN + str(player_hand) + "\n")
        player_hand_total += self.get_values(player_hand_value)
        # Prints the total in a string
        print("Total of: " + str(player_hand_total) + "\n")
        if player_hand_total == 21:
            self.blackjack(bet_amount)
            print(Fore.YELLOW + "Thats Blackjack!!")
            print("Your total credits are now: $ " + str(self.value) + "\n")
            return player_hand_total
        if player_hand_total > 21:
            print(Fore.RED + "Bust! You went over 21! you lose" + "\n")
            # Prints the remaining value for player.
            print(f"You have: ${self.value} remaining")
            return player_hand_total
        return player_hand_total

    # A function that asks the player to play again.
    def play_again(self):
        while True:
            game_over = input("Would you like to play another hand? type n to quit (y/n) ")
            if game_over == "y":
                game_over = False
                clearing.clear()
                return game_over
            elif game_over == "n":
                game_over = True
                clearing.clear()
                return game_over
            else:
                print("Please type in y or n")

    def game_over(self):
        # A loop to try users entered amount, max is 1000 and doesn't allow for any negative numbers, or other characters.
        while True:
            try:
                rebuy = input(
                "You've run out of credits, please select rebuy amount (max $1000): $")
                while int(rebuy) > 1000 or int(rebuy) <= 0:
                    rebuy = input("Please enter less or equal to 1000 rebuy amount: $")
                    # Using the money package to rebuy with the amount inputted above.
                return rebuy
            # If there is a value error such as 0 we ask the user to enter a valid option below.
            except ValueError:
                print("Please enter a valid amount, $1 > $1000")

    # A dealer function, this function is called once the player chooses to stand.
    def dealer(self):
        dealer_hand_total = 0
        while dealer_hand_total < 17:
            # Draw deals a singular card at a time and saves to a variable dealer_hand
            dealer_hand = cards.draw_cards("Draw")
            # The numeric value of the card from dealer and saves to a variable dealer_hand_value
            dealer_hand_value = cards.get_values(dealer_hand)
            print(Fore.CYAN + f"Dealer deals: {dealer_hand[0]}")
            dealer_hand_total += self.get_values(dealer_hand_value)
            print("Total of: " + str(dealer_hand_total) + "\n")
        return dealer_hand_total

    # This function returns the total hand value number.
    def get_values(self, values):
        player_hand_total = 0
        for key, value in values.items():
            player_hand_total += values[key]
        return player_hand_total

if __name__ == '__main__':
    # Creating instances of the classes to generate a dealer, player, a deck of cards, and the blackjack game.
    table = Blackjack()
    table.blackjack_table()
    cards = Deck()
    player = Blackjack()
    player.player()
    dealer = Blackjack()
    dealer.dealer()

