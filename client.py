import pygame

from ball import Ball
from game import Game

pygame.init()

white_color = (255, 255, 255)
black_color = (0, 0, 0)

display_width = 800
display_height = 600
game = Game(display_width, display_height)
screen = game.render()

ball_width = 73
ball_image = 'assets/ball.png'
ball = Ball(ball_image)

game_width = display_width
game_height = display_height

clock = pygame.time.Clock()

def game_loop():
    x = (game_width * 0.45)
    y = (game_height * 0.8)

    x_change = 0
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.exit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        screen.fill(white_color)
        ball.position(screen, game_width, game_height, x, y)

        if x > display_width - ball_width or x < 0:
            gameExit = True

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
