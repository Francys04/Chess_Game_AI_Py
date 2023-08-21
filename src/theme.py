from color import Color

class Theme:

    def __init__(self, light_bg, dark_bg, 
                       light_trace, dark_trace,
                       light_moves, dark_moves):
        
        self.bg = Color(light_bg, dark_bg)
        self.trace = Color(light_trace, dark_trace)
        self.moves = Color(light_moves, dark_moves)
        
        
'''- light_bg: Background color for light squares on the game board.
- dark_bg: Background color for dark squares on the game board.
- light_trace: Color for trace indicators (e.g., highlighting last move positions) on light squares.
- dark_trace: Color for trace indicators on dark squares.
- light_moves: Color for valid move indicators on light squares.
- dark_moves: Color for valid move indicators on dark squares.'''