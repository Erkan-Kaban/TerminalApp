def player_hit(self, player_hand, player_hand_value, bet_amount):
            player_hand_total = 0
            # Drawing a single card at every hit.
            # player_hand += cards.draw_cards("Draw")
            player_hand_value = cards.get_values(player_hand)
            print(Fore.CYAN + str(player_hand))
            player_hand_total = self.get_values(player_hand_value)
            print("Total of: " + str(player_hand_total) + "\n")
            if player_hand_total < 21:
                player_hand += cards.draw_cards("Draw")
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