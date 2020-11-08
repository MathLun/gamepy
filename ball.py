import pygame

class Ball:
    def __init__(self, img):
        self.img = img

    def loadImage(self):
        return pygame.image.load(self.img)
    
    def position(self, screen, game_width, game_height, x, y):
        return screen.blit(self.loadImage(), (x,y))