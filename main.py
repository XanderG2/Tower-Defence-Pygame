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

cellSize = 20
gridCoords = []

for x in range(0, width, cellSize):
    for y in range(0, height, cellSize):
        top_right = (x + cellSize, y)
        bottom_left = (x, y + cellSize)
        gridCoords.append([top_right, bottom_left])

print(gridCoords)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    screen.fill(white)
    for x in range(0, width, cellSize):
        pygame.draw.line(screen, black, (x, 0), (x, height))
    for y in range(0, height, cellSize):
        pygame.draw.line(screen, black, (0, y), (width, y))
    mousePos = pygame.mouse.get_pos()
    for index, coords in enumerate(gridCoords):
        top_right, bottom_left = coords
        if bottom_left[0] <= mousePos[0] <= top_right[0] and bottom_left[1] <= mousePos[1] <= top_right[1]:
            print(f"Mouse is in cell {index}")
    pygame.display.flip()

pygame.quit()
