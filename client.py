import pygame

pygame.init()

display_width = 400
display_height = 400
display_size = display_width, display_height

black = (0, 0, 0)
white = (255, 255, 255)
screen = pygame.display.set_mode(display_size)

ballImg = pygame.image.load('soccer_ball.png')
def ball(x,y):
    screen.blit(ballImg, (x,y))

x = (display_width * 0.90)
y = (display_height * 0.7)

clock = pygame.time.Clock()
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    screen.fill(black)
    ball(x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
