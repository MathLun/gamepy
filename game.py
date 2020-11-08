import pygame

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def render(self):
        display_size = (self.width, self.height)
        self.caption()
        return pygame.display.set_mode(display_size)
    
    def caption(self):
        return pygame.display.set_caption('Ball Game')