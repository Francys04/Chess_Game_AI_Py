import unittest
from unittest.mock import MagicMock, patch
from main import Main  # Assuming the code is in a file named "main.py"
import pygame
from assets.sounds import *

class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        cls.mock_display = MagicMock(spec=pygame.Surface)
        cls.mock_display.set_mode.return_value = cls.mock_display

    @patch('main.Game')
    def test_init(self, mock_game):
        mock_game_instance = mock_game.return_value
        main = Main()
        self.assertEqual(main.game, mock_game_instance)

    @patch('main.Game')
    @patch('pygame.display.set_mode')
    @patch('pygame.init')
    def test_init_calls(self, mock_init, mock_set_mode, mock_game):
        main = Main()
        mock_init.assert_called_once()
        mock_set_mode.assert_called_once_with((800, 800))
        mock_game.assert_called_once()

    @patch('main.pygame.display.update')
    @patch('main.pygame.display.set_caption')
    def test_mainloop(self, mock_set_caption, mock_display_update):
        main = Main()
        main.screen = self.mock_display
        main.game.dragger.dragging = False  # Set up for MOUSEBUTTONDOWN event simulation
        main.game.board.squares[1][2].has_piece.return_value = True
        main.game.board.squares[1][2].piece.color = 'white'
        main.game.board.valid_move.return_value = True

        # Simulate MOUSEBUTTONDOWN event
        with patch('main.pygame.event.get', return_value=[MagicMock(type=pygame.MOUSEBUTTONDOWN, pos=(150, 150))]):
            main.mainloop()
            self.assertTrue(main.game.dragger.dragging)
            self.assertTrue(main.game.board.calc_moves.called)
            self.assertTrue(main.game.dragger.save_initial.called)
            self.assertTrue(main.game.dragger.drag_piece.called)

        # Simulate MOUSEMOTION event
        with patch('main.pygame.event.get', return_value=[MagicMock(type=pygame.MOUSEMOTION, pos=(150, 150))]):
            main.mainloop()
            self.assertTrue(main.game.dragger.dragging)
            self.assertTrue(main.game.set_hover.called)

        # Simulate MOUSEBUTTONUP event
        main.game.board.valid_move.return_value = False  # Set up for MOUSEBUTTONUP event simulation
        with patch('main.pygame.event.get', return_value=[MagicMock(type=pygame.MOUSEBUTTONUP, pos=(250, 250))]):
            main.mainloop()
            self.assertFalse(main.game.dragger.dragging)

        # Simulate KEYDOWN event
        with patch('main.pygame.event.get', return_value=[MagicMock(type=pygame.KEYDOWN, key=pygame.K_t)]):
            main.mainloop()
            self.assertTrue(main.game.change_theme.called)

        # Simulate QUIT event
        with patch('main.pygame.event.get', return_value=[MagicMock(type=pygame.QUIT)]):
            with self.assertRaises(SystemExit):
                main.mainloop()

        self.assertEqual(mock_set_caption.call_count, 5)  # Main loop iterates multiple times

if __name__ == '__main__':
    unittest.main()
