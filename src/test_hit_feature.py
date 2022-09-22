# import sys, traceback
# import clearing
# from multiprocessing.sharedctypes import Value
# from CardGame.Blackjack.money import Money
# from deck import Deck
# from colorama import Fore, init
# init(autoreset=True)
from blackjack import blackjack

def fake_input(prompt):
    return 'h'

class test_hit:
    def test_player_hit(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        assert player() == '123'
















