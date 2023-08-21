'''
The code imports the pygame module, which is a popular 
library used for developing 2D games and multimedia applications.
'''
import pygame

from const import *

class Dragger:

    def __init__(self):
        self.piece = None #Holds the reference to the game piece being dragged.
        self.dragging = False # Indicates whether a piece is currently being dragged (True) or not (False).
        #Store the current mouse cursor's X and Y coordinates.
        self.mouseX = 0
        self.mouseY = 0
        #Store the initial row and column (grid) where dragging started.
        self.initial_row = 0
        self.initial_col = 0

    # blit method

    def update_blit(self, surface):
        # texture
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        # img
        img = pygame.image.load(texture)
        # rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        # blit
        surface.blit(img, self.piece.texture_rect)

    #Updates the mouse cursor's coordinates.
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos # (xcor, ycor)
    #Records the initial row and column based on the provided position.
    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE
    #Initiates the dragging of a game piece.
    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
    #Ends the dragging of a game piece.
    def undrag_piece(self):
        self.piece = None
        self.dragging = False
