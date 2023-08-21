'''Library, which is commonly used for developing games and multimedia applications in Python.'''
import pygame

'''This class is responsible for managing sound playback.'''
class Sound:

    def __init__(self, path):
        self.path = path #self.path: Stores the path to the sound file.
        self.sound = pygame.mixer.Sound(path)#Creates an instance of pygame.mixer.Sound 
        #using the provided sound file path. This instance will be used to play the sound.


    #The play method plays the sound associated with the Sound instance.
    def play(self):
        pygame.mixer.Sound.play(self.sound)