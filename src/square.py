
class Square:
    '''This dictionary maps column indices (0 to 7) to their corresponding alphabetic labels ('a' to 'h').'''
    ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    def __init__(self, row, col, piece=None):
        self.row = row #Stores the row index of the square.
        self.col = col #Stores the column index of the square.
        self.piece = piece #Represents the piece located on the square (default is None if no piece is present).
        self.alphacol = self.ALPHACOLS[col] #Represents the alphabetic column label of the square (e.g., 'a' for column 0).

    '''Returns True if both the row and column indices of the current and other squares are the same, and False otherwise.'''
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    '''Returns True if the square has a piece on it (not empty).'''
    def has_piece(self):
        return self.piece != None
    '''Returns True if the square is empty (no piece on it).'''
    def isempty(self):
        return not self.has_piece()
    '''Returns True if the square has a piece of the specified color.'''
    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color
    '''Returns True if the square has an enemy piece (piece of a different color).'''
    def has_enemy_piece(self, color):
        return self.has_piece() and self.piece.color != color
    '''Returns True if the square is either empty or has an enemy piece.'''
    def isempty_or_enemy(self, color):
        return self.isempty() or self.has_enemy_piece(color)

    '''Returns True if all arguments are within the range, otherwise returns False.'''
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        
        return True

    @staticmethod
    def get_alphacol(col):
        ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        return ALPHACOLS[col]