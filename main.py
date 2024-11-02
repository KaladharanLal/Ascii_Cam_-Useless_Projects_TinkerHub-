import pygame
from pygame.math import Vector2 as vec

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True

resFact = 10
imgMat = [[],[]]
textSize = resFact

text = pygame.font.Font("Courier_Prime/CourierPrime-Regular.ttf", textSize)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER
    snake = pygame.image.load("./pygame_logo.png")
    #screen.blit(pygame.transform.scale(snake, (snake.get_width()//2, snake.get_height()//2)), (0,0))
    surf = pygame.Surface((720,720))
    surf.blit(pygame.transform.scale(snake, (snake.get_width()//resFact, snake.get_height()//resFact)), (0,0))
    imgMat = pygame.surfarray.pixels3d(surf)
    # print(imgMat[10][10])
    for i in range(len(imgMat)):
        for j in range(len(imgMat[i])):
            for k in range(3):
                if imgMat[i][j][k] == 0:
                    imgMat[i][j][k] = 255
    # print(imgMat[10][10])
    pygame.surfarray.blit_array(screen,imgMat)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()