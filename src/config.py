'''
This line imports the pygame module, which is a popular library for creating games and multimedia applications in Python. 
It provides various functions and classes for working with graphics, sound, input devices, and more.
'''
import pygame
'''
This line imports the os module, which provides 
functions for interacting with the operating system, such as working with files and directories.
'''
import os

'''This line imports the Sound class from a module named sound. 
It suggests that there's a class named Sound defined in the sound module that will be used in this code.'''
from sound import Sound
'''This line imports the Theme class from a module named theme. 
It indicates that there's a class named Theme defined in the theme module that will be used in this code.'''
from theme import Theme

'''This line starts the definition of a Python class named Config. 
This class is intended to store and manage various configuration settings and resources for the application.'''
class Config:
    def __init__(self):#The constructor is called when an instance of the class is created and is used to initialize the attributes of the object
        
        self.themes = []#This line initializes an empty list named themes as an attribute of the Config object
        self._add_themes() #This line calls the private method _add_themes() to populate the themes list with different Theme objects.
        self.idx = 0 #This line initializes an attribute named idx with the value 0. 
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.move_sound = Sound(
            os.path.join('assets/sounds/move.wav'))
        self.capture_sound = Sound(
            os.path.join('assets/sounds/capture.wav'))

    #This line defines a method named change_theme() within the Config class. 
    #This method will be used to switch to the next theme in the themes list.
    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    #This line defines a private method _add_themes() within the Config class. This method will be used to add different 
    #theme objects to the themes list.
    def _add_themes(self):
        green = Theme((234, 235, 200), (119, 154, 88), (244, 247, 116), (172, 195, 51), '#C86464', '#C84646')
        brown = Theme((235, 209, 166), (165, 117, 80), (245, 234, 100), (209, 185, 59), '#C86464', '#C84646')
        blue = Theme((229, 228, 200), (60, 95, 135), (123, 187, 227), (43, 119, 191), '#C86464', '#C84646')
        gray = Theme((120, 119, 118), (86, 85, 84), (99, 126, 143), (82, 102, 128), '#C86464', '#C84646')

        self.themes = [green, brown, blue, gray]