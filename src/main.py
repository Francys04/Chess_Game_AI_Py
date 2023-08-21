'''
Imports the Pygame library, which is used to create the graphical user interface for the chess game.
'''
import pygame
'''
Imports the sys module, which provides access to some variables used or maintained
by the Python interpreter and to functions that interact strongly with the interpreter.
'''
import sys
from const import *
'''Imports the Game class from the "game" module.'''
from game import Game
'''Imports the Square class from the "square" module.'''
from square import Square
'''Imports the Move class from the "move" module.'''
from move import Move

class Main:
#def __init__(self): The constructor method for the Main class. It initializes the Pygame library,
#sets up the game window, and creates a new instance of the Game class.
#def mainloop(self): The main game loop method. This loop continuously updates the game state and handles user inpu
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):
        
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            # show methods
            #game.show_bg(screen), game.show_last_move(screen), etc.: These lines call methods from the Game class 
            #to update and display various elements of the game, such as the background, last move indicators, 
            #available moves, pieces on the board, and hover effects.
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)

            #if dragger.dragging:: Checks if a piece is currently being dragged by the player.
            #dragger.update_blit(screen): If a piece is being dragged, this line updates the position 
            #of the dragged piece on the screen.
            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                # click
                #if event.type == pygame.MOUSEBUTTONDOWN:: Handles mouse button down events, which occur when the player clicks the mouse.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Updates the position of the mouse cursor.
                    dragger.update_mouse(event.pos)
                    
                    # Calculates the row and column of the clicked square.
                    clicked_row = dragger.mouseY // SQSIZE 
                    clicked_col = dragger.mouseX // SQSIZE

                    # if clicked square has a piece ?
                    # Handles mouse motion events, which occur when the player moves the mouse.
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        # valid piece (color) ?
                        if piece.color == game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            # show methods 
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)
                
                # click release
                # Handles mouse motion events, which occur when the player moves the mouse.
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        # create possible move
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        # valid move ?
                        if board.valid_move(dragger.piece, move):
                            # normal capture
                            captured = board.squares[released_row][released_col].has_piece()
                            board.move(dragger.piece, move)

                            board.set_true_en_passant(dragger.piece)                            

                            # sounds
                            game.play_sound(captured)
                            # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            # next turn
                            game.next_turn()
                    
                    dragger.undrag_piece()
                
                # key press
                elif event.type == pygame.KEYDOWN:
                    
                    # changing themes
                    if event.key == pygame.K_t:
                        game.change_theme()

                     # changing themes
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger

                # quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

#Main class and enters the main game loop by calling the main.mainloop() method.
main = Main()
main.mainloop()