# os module provides functions for interacting with the operating system, such as working with file paths.
import os

class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name #Name of the piece (e.g., 'pawn', 'knight', etc.).
        self.color = color #Color of the piece ('white' or 'black').
        value_sign = 1 if color == 'white' else -1 #Value of the piece for scoring purposes.
        self.value = value * value_sign 
        self.moves = [] 
        self.moved = False
        self.texture = texture#File path to the image representing the piece's texture.
        self.set_texture()
        self.texture_rect = texture_rect # Rectangle defining the position and size of the piece's texture on the image.

    #set_texture method sets the texture attribute with a file path based on the piece's color and name
    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')
        
    #adds a move to the list of possible moves for the piece.
    def add_move(self, move):
        self.moves.append(move)
        
    #This method resets the list of possible moves.
    def clear_moves(self):
        self.moves = []

class Pawn(Piece):

    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        self.en_passant = False
        super().__init__('pawn', color, 1.0)

class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color, 3.0)

class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3.001)

class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color, 5.0)

class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color, 9.0)

class King(Piece):

    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__('king', color, 10000.0)
        
'''
The subsequent classes (Pawn, Knight, Bishop, Rook, Queen, King) are subclasses of the 
Piece class. Each subclass defines its specific behavior and attributes that are unique to that chess piece. 
The provided code defines the basic structure of these subclasses, 
which you can further customize with additional functionality specific to each piece.
'''