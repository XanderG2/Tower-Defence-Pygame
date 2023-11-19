import pygame, sys
pygame.init()

width = 900
height = 500
screen = pygame.display.set_mode((width, height))

white = (255,255,255)
black = (0,0,0)
lightGreen = (0,255,0)
darkLightGreen = (51,153,51)
midGreen = (0,204,0)
darkGreen = (0,153,51)
veryDarkGreen = (0,102,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    screen.fill(white)
    pygame.display.flip()

pygame.quit()
