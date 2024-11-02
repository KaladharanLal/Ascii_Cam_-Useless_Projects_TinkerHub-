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

def getChar2(pix):
    ch = ""
    dens = 'N@#W$9876543210?!abc;:+=-,._ '
    densR = 'WEBOCIwxzuiL(|:.'
    densG = 'GHSQUJsgqpj[)/;,'
    densB = 'MKFDYVabdko{]!=`'
    if pix[0]>pix[1] and pix[0]>pix[2]:
        ch = densR[round((1-pix[0]/255)*(len(densR)-1))]
    elif pix[1]>pix[0] and pix[1]>pix[2]:
        ch = densG[round((1-pix[0]/255)*(len(densG)-1))]
    elif pix[2]>pix[1] and pix[2]>pix[1]:
        ch = densB[round((1-pix[0]/255)*(len(densB)-1))]
    else:
        ch = dens[round((1-pix[0]/255)*(len(dens)-1))]
    return ch

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
    camSurf = pygame.Surface((screen.get_width()//resFact, screen.get_height()//resFact))
    camSurf.blit(pygame.transform.scale(pygame.transform.flip(cam.get_image(), 1, 0), (screen.get_width()//resFact, screen.get_height()//resFact)), (0,0))
    # screen.blit(camSurf, (0,0))
    imgMat = pygame.surfarray.pixels3d(camSurf)

    surf2 = pygame.Surface((screen.get_width(), screen.get_height()))
    for i in range(len(imgMat)):
        for j in range(len(imgMat[i])):
            surf2.blit(text.render(getChar2(imgMat[i][j]),True, (255, 255, 255)), (resFact*i, resFact*j))
    screen.blit(surf2, (0, 0))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
