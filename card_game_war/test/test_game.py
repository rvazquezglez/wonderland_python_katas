import unittest
from card_game_war.code.game import Game


class TestGame(unittest.TestCase):
    def get_card(self, rank, suit):
        pass

    def test_play_game(self):
        g = Game()
        player1_cards = []
        player2_cards = []

        self.assertEqual(2, g.play(player1_cards, player2_cards), "the player loses when they run out of cards")

    def test_play_round(self):
        g = Game()
        card1 = None
        card2 = None

        self.assertEqual(2, g.play_round(card1, card2),
                         msg="the highest rank wins the cards in the round")

        self.assertEqual(1, g.play_round(card1, card2),
                         msg="queens are higher rank than jacks")

        self.assertEqual(1, g.play_round(card1, card2),
                         msg="aces are higher rank than kings")

        self.assertEqual(2, g.play_round(card1, card2),
                         msg="if the ranks are equal, clubs beat spades")

        self.assertEqual(1, g.play_round(card1, card2),
                         msg="if the ranks are equal, diamonds beat clubs")

        self.assertEqual(1, g.play_round(card1, card2),
                         msg="if the ranks are equal, hearts beat diamonds")


if __name__ == '__main__':
    unittest.main()
