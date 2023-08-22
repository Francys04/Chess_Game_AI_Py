'''unittest for writing and running tests'''
import unittest
'''Mock from unittest.mock for creating mock objects'''
from unittest.mock import Mock
'''pygame for the graphical user interface library'''
import pygame
'''SQSIZE from const which is likely a constant representing the size of a square on the chessboard'''
from dragger import Dragger
from const import SQSIZE

class TestDragger(unittest.TestCase):

    def setUp(self):
        self.dragger = Dragger()
    #This method tests whether the initialization of the 
    #Dragger instance results in the expected initial attribute values.
    def test_initialization(self):
        self.assertIsNone(self.dragger.piece)
        self.assertFalse(self.dragger.dragging)
        self.assertEqual(self.dragger.mouseX, 0)
        self.assertEqual(self.dragger.mouseY, 0)
        self.assertEqual(self.dragger.initial_row, 0)
        self.assertEqual(self.dragger.initial_col, 0)

    def test_update_mouse(self):
        pos = (100, 200)
        self.dragger.update_mouse(pos)
        self.assertEqual(self.dragger.mouseX, pos[0])
        self.assertEqual(self.dragger.mouseY, pos[1])

    def test_save_initial(self):
        pos = (150, 300)
        self.dragger.save_initial(pos)
        self.assertEqual(self.dragger.initial_row, pos[1] // SQSIZE)
    # This method tests the drag_piece method to ensure that the piece is correctly 
    #associated with the dragger and that the dragging state is set to True.
    def test_drag_piece(self):
        piece = Mock()
        self.dragger.drag_piece(piece)
        self.assertEqual(self.dragger.piece, piece)
        self.assertTrue(self.dragger.dragging)

    def test_undrag_piece(self):
        self.dragger.undrag_piece()
        self.assertIsNone(self.dragger.piece)
        self.assertFalse(self.dragger.dragging)

#This block of code ensures that the tests are executed when 
#the script is run directly (not imported as a module).
if __name__ == '__main__':
    unittest.main()
