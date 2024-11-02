import pygame
from pygame.math import Vector2 as vec
import pygame.camera

# pygame setup
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (1000, 800), "RGB")
cam.start()

screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
running = True

resFact = 10
imgMat = [[],[]]
textSize = resFact

text = pygame.font.Font("Courier_Prime/CourierPrime-Regular.ttf", textSize)

def getChar(pix):
    avg = (pix[0]+pix[1]+pix[2])/3
    dens = 'N@#W$9876543210?!abc;:+=-,._ '
    return dens[round((1-avg/255)*(len(dens)-1))]

# print(pygame.camera.list_cameras())

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
    canv = pygame.image.load("./pygame_logo.png")
    #screen.blit(pygame.transform.scale(canv, (canv.get_width()//2, canv.get_height()//2)), (0,0))
    surf = pygame.Surface((screen.get_width()//resFact, screen.get_height()//resFact))
    surf.blit(pygame.transform.scale(canv, (screen.get_width()//resFact, screen.get_height()//resFact)), (0,0))
    # screen.blit(pygame.transform.scale(pygame.transform.scale(canv, (screen.get_width()//resFact, screen.get_height()//resFact)), (screen.get_width(), screen.get_height())), (0,0))

    camSurf = pygame.Surface((screen.get_width()//resFact, screen.get_height()//resFact))
    camSurf.blit(pygame.transform.scale(cam.get_image(), (screen.get_width()//resFact, screen.get_height()//resFact)), (0,0))
    screen.blit(camSurf, (0,0))
    imgMat = pygame.surfarray.pixels3d(camSurf)
    # print(imgMat[10][10])
    # for i in range(len(imgMat)):
    #     for j in range(len(imgMat[i])):
    #         # for k in range(3):
    #         #     if imgMat[i][j][k] == 0:
    #         #         imgMat[i][j][k] = 100
    #         imgMat[i][j][0] = 200
    # print(imgMat[10][10])
    # pygame.surfarray.blit_array(surf,imgMat)

    surf2 = pygame.Surface((screen.get_width(), screen.get_height()))
    for i in range(len(imgMat)):
        for j in range(len(imgMat[i])):
            surf2.blit(text.render(getChar(imgMat[i][j]),True, (255, 255, 255)), (resFact*i, resFact*j))
    screen.blit(surf2, (0, 0))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()