'''
The constructor initializes a Move instance with two parameters: initial and final. 
#Both parameters are expected to be objects representing squares on the game board.
# '''
class Move:

    def __init__(self, initial, final):
        # initial and final are squares
        self.initial = initial
        self.final = final

    #This method defines a string representation of a Move instance.
    #It returns a formatted string that indicates the initial and final positions of the move in terms of row and column indices.
    #For example, the string might look like "(2, 3) -> (4, 5)" to represent moving a piece from row 2, column 3 to row 4, column 5.
    def __str__(self):
        s = ''
        s += f'({self.initial.col}, {self.initial.row})'
        s += f' -> ({self.final.col}, {self.final.row})'
        return s

    #It returns True if both the initial and final positions of the current Move instance are 
    #equal to the corresponding positions of another Move instance (other), and False otherwise.
    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final