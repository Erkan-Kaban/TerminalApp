### User Interaction and Experience
<hr>

The game with the menu screen being display.

It includes a "How to play section", "Quit" and most important "Play against dealer"

![](docs/main_screen.jpg)

### R3 Full attribution to referenced sources

<hr>
<u>The referenced resources used for this project are as follows:</u>
<br><br>

Rossum, G., 2022. PEP 8 – Style Guide for Python Code | peps.python.org. [online] Peps.python.org. Available at: <https://peps.python.org/pep-0008/> [Accessed 22 September 2022].

Patorjk.com. 2022. Text to ASCII Art Generator (TAAG). [online] Available at: <http://patorjk.com/software/taag/#p=display&f=Cards&t=Blackjack> [Accessed 22 September 2022].

PyPI. 2022. clearing. [online] Available at: <https://pypi.org/project/clearing/> [Accessed 22 September 2022].

PyPI. 2022. pick. [online] Available at: <https://pypi.org/project/pick/> [Accessed 22 September 2022].

PyPI. 2022. colorama. [online] Available at: <https://pypi.org/project/colorama/> [Accessed 22 September 2022].

<hr>

### R4 Link to source control repository

[Click here for repository](https://github.com/Erkan-Kaban/TerminalApp)
<hr>

<br>

### R5 The style guide or styling convention adhered to:

<u>PEP8 - Style Guide for Python Code</u>
<br><br>
<hr>

### R6 Features

### <u>Hit Feature</u>

The hit feature allows users to draw another single card to add to their hands. When the user types in the "h" letter. The cards are calculated to the player's total hand value. The player's hand is also shown to the user to decide what to do next. The hit feature is active inside a while loop that keeps track of the user's total card hand value. As long as the value of the user's total card hand value doesn't go over 21, the user keeps getting asked if they would like to hit (take another card).

Variable player_hand_total is inside the main while loop to ensure at every new hand we're dealt, the variable is set back to 0. In addition, this variable is in a while loop condition where the player_hand_total < 21. This loop allows the game at play to keep going till the user reaches 21 or over. When the player's card count adds over 21, we place an if statement. If the hand total is over 21. We print the player has lost and a break to break out of the while loop. The user can write whatever they like instead of 'h.' Still, the program constantly loops back to the question, "Would you like to hit(another card) or stand(stay) (h/s)?" no matter if they input numbers or letters, it won't provoke an error. It will simply keep asking them to input (h/s). 

![](docs/hit_feature.jpg)

### <u>Stand Feature</u>
The stand feature works in the same area as the hit feature. It works with the hit feature, so the user has the option on the same turn to hit or stand. With the stand feature, once the user inputs the 's' key, we call the dealer function outside the while loop. The dealer deals cards themselves till they reach a total value of 17 or over. We then capture that total into a variable named dealer_hand_total. We then place a series of if statements that compare the variable player_hand_total and the dealer_hand_total. If the player's hand total is more than the dealer's total, we print that "You win!!" and calculate their winnings, add it to their total credits, and break out of the loop. If the dealer also goes over 21, we check if they've busted. We also check if the player hand total and dealer hand total are the same. In this case, we "push" credit to be refunded and break out of the loop. Otherwise, all other options are FALSE the dealer wins.

![](docs/stand_feature.jpg)

### <u>Rebuy Feature</u>
For the rebuy feature, we check at the end of every game played with an if statement. For example, we are checking if the user's credit has reached 0 or not. Once this condition is met in the if statement, we place a while loop and use the try/except combination. We wait for input with a message stating that they've run out of credits and give the player the option to specify how many credits they would like to rebuy. Every time the user inputs something invalid (ValueError), we print and ask them to input a correct amount of $1 to $1000. Since we're in a while loop, the program will keep asking until the user inputs something valid. Once the player has inputted a valid amount (1- 1000), we break out of the loop and save their new amount into a new initialized amount they've inputted into the game.

![](docs/rebuy_feature.jpg)

### <u>Bet Feature</u>

With the bet feature, we used an external package from PyPI called CardGame, specifically the money.py module. Inside the money.py we have a function called "bet" that we've inherited from our class. When we call this function, we ask the user to place a bet. This bet function checks if the amount is not above or below the number of credits the player is holding, so it will raise a "That is not a valid bet. Please try again." if the user doesn't place a valid bet. Otherwise, it will get saved into self.bet, where we save that into our local variable called bet_amount. Depending on what unfolds, we use this bet amount to calculate winning or losing for the player.

![](docs/place_bet_feature.jpg)

### <u>Main Menu Feature</u>

The main menu is another imported package from PyPI called "picker" once imported, it allows you to edit what options you'd like. We have a player against the dealer. How to play and quit. The menu uses directional keys on the keyboard to launch the main game or to select how to play or quit. This feature is pretty solid and doesn't have any way for a program to produce errors. We have placed a catching error incase the user does try to ctrl+c, and it will write a message that it's quitting and close the program rather than showing errors.

![](docs/main_screen.jpg)

### Implementation
<hr>

##### Day 1

<br>
The first day of implementation planning, I was able to come up with the following on Trello:
<br><br>

![](docs/Implementation_1.jpg)

Menu creation was on its way, shell scripting, requirement.txt to ensure the game will work from the very beginning of the project and to ensure that every addition that I make, I test on the shell for the changes.
<br><br>

<hr>

##### Day 2

<br>
The second day of implementation planning, I was able to come up with a menu, created a working shell script that reads requirements.txt and checks if the user has created a virtual environment, and the required packages before running the game. Also created some code for the card class that creates a deck of identifiable cards.
<br><br>

![](docs/implementation_2..jpg)

<hr>

#### Day 3
The third day, spent some time creating and completing my deck and card class. As well as adding a PyPI package called 'dealerschoice' and using some of the functions it had to have in game currency. OOP was added to the code and grouped together with methods for everything to be more streamlined, clearer to read and more functional.

![](docs/implementation_3.png)

<hr>

### Day 4
The fourth day, was mainly spent around creating a player class and building on some if statement as well as for loops to check the value of each card. Having a bust feature if the player hits over 21. Adding more features as I go along. I think eventually when I have the logic correct, to try and apply some more OOP.

![](docs/implementation_4.jpg)

<hr>

### Day 5
The fifth day, made some great progress today, completed the player vs dealer function, the black jack class, options to rebuy, the stand feature. As will as being able to quit more gracefully without errors showing. Also a clear screen at the end of every game. We also ask the player if they would like to play again and if they select no it will exit the game gracefully.

![](docs/implementation_5.jpg)

<hr>

### Day 6
The sixth day, tied in my blackjack.py program with the main menu, got it all functioning the way I like it, catching every error I can think of, also worked on my readme a little bit and tried to implement some error catching.

![](docs/implementation_6.jpg)

<hr>

### Installation Instructions
<hr>

1. If you do not have Python installed on your computer or OS, please go to [page](https://www.python.org/downloads/) and install Python.
2. Please also install pip onto your computer or OS, please go to [link](docs/implementation_2..jpg)
3. Clone the repository by writing the command line below

   `git clone https://github.com/Erkan-Kaban/TerminalApp.git`

4. From here we need to change into the directory src folder from the cloned repository on our local system by:
   
    `cd src`
5. From here we can run blackjack by executing the shell script by entering the command 

    `./blackjack.sh`
6. From here we check if you've installed the dependecies required and will run the game with prompts.