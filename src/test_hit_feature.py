import blackjack_class
import pytest



player = blackjack_class.Blackjack()
table = blackjack_class.Blackjack()
dealer = blackjack_class.Blackjack()
player = blackjack_class.Blackjack()
table.blackjack_table()
player.player()
dealer.dealer()

def fake_input(prompt):
    return 'h'

class Test_hit:
    def test_player_hit(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        assert player.bet_amount == '1001'
        # assert player.player_hit == 's'















