import pygame

pygame.init()

class Ball:
    def __init__(self, img):
        self.img = img

    def loadImage(self):
        return pygame.image.load(self.img)

    def position(self, screen, game_width, game_height):
        x = (game_width * 0.45)
        y = (game_height * 0.8)
        return screen.blit(self.loadImage(), (x,y))

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def render(self):
        display_size = self.width, self.height
        return pygame.display.set_mode(display_size)
    


black_color = (0, 0, 0)

display_width = 800
display_height = 600
game = Game(display_width, display_height)
screen = game.render()

image = 'assets/soccer_ball.png'
ball = Ball(image)

game_width = display_width
game_height = display_height
position_ball = ball.position(screen, game_width, game_height)

clock = pygame.time.Clock()
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    
    screen.fill(black_color)
    
    position_ball

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
