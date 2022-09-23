class Card_Generator:
    def card_options(self):
        # Created a list of possible card values and suits.
        card_combination = ""
        card_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Spades ♠", "Hearts ♥", "Diamonds ♦", "Clubs ♣"]
        # Combining suits with card_list.
        for suit in suits:
            for cards in card_list:
                # Adding the possible combinations in a string.
                card_combination += cards + " of " + suit + ","
        # Splitting at every comma to make them into an individual index in a list.
        cards = card_combination.split(",")
        # As our for loop created commas at every iteration, we have to pop the last comma value.
        cards.pop()
        return cards

    # This function returns the card value we present to it in a list.
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
