import blackjack_class

# Creating instances of the classes to generate a dealer, player, a deck of cards, and the blackjack game.
def blackjack_game():
    table = blackjack_class.Blackjack()
    dealer = blackjack_class.Blackjack()
    player = blackjack_class.Blackjack()
    table.blackjack_table()
    player.player()
    dealer.dealer()
