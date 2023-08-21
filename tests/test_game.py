import unittest
from unittest.mock import Mock
from src.game import Game

class TestGameMethods(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.mock_surface = Mock()  # Mocked surface for testing

    def test_next_turn(self):
        self.assertEqual(self.game.next_player, 'white')
        self.game.next_turn()
        self.assertEqual(self.game.next_player, 'black')
        self.game.next_turn()
        self.assertEqual(self.game.next_player, 'white')

    def test_set_hover(self):
        self.assertIsNone(self.game.hovered_sqr)
        self.game.set_hover(2, 3)
        self.assertEqual(self.game.hovered_sqr.row, 2)
        self.assertEqual(self.game.hovered_sqr.col, 3)

    def test_change_theme(self):
        initial_theme = self.game.config.theme
        self.game.change_theme()
        new_theme = self.game.config.theme
        self.assertNotEqual(initial_theme, new_theme)

    # More test methods for other Game methods...

if __name__ == '__main__':
    unittest.main()
