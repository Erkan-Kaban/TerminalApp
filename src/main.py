# Main menu of the game - calls all modules for the main menu.
import os
from pick import pick
from textwrap import wrap
import ascii_images
from blackjack import blackjack

# An instance of the Asci class in ascii_images
menu_title = ascii_images.Asci()


def menu():  # A menu function that takes in a title and options.
    title = f"{menu_title.get_title()} \n Please select from the following options"  # Uses the pick module to create this menu.
    options = ["Play against dealer", "How to play", "Quit"]
    option, index = pick(options, title, indicator="\u2660")

    # An if statement checks if index 1 is chosen in the menu.
    # prints instructions from instructions().
    # Gives you the one option to go "Back".
    # Selecting "Back" gives an index of 0.
    # Selecting an index of 0 will call our blackjack module.
    if index == 0:
        blackjack()
    if index == 1:
        title = "\n".join(instructions())
        options = ["Back"]
        index = pick(options, title, indicator="\u2660")
        # An if statement checks if index 0 is chosen and takes you back to menu.
        if index == ("Back", 0):
            menu()


# instructions function uses the package textwrap, to wrap the doctype to a width of 150
def instructions():
    instructions = """Objective of the game-----> Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.
    Card Values/Scoring-----> It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value. 
    Betting------> Before the deal begins, player makes a bet Minimum and maximum limits, limits are 2 credits to 500 credits. Play begins following.
    The Play-----> The player must decide wether to "stand" (not ask for another card) or "hit (ask for another card) and aim a total value of 21.
    Dealers Play -----> The dealer plays when the player has finished there play, the dealer must hit if there total value of their cards are < 17.
    End Objective -----> For the player to win they must attain a higher number than the dealer as close to 21 as possible.
    """
    wrapped_lines = wrap(instructions, width=150)
    return wrapped_lines


# Calling the menu function
menu()
