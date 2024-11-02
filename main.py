import pygame
from IPython.utils.coloransi import value
from pygame.math import Vector2 as vec
import pygame.camera

defWidth = 1920
defHeight = 1080

# pygame setup
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (defWidth, defHeight), "RGB")
cam.start()

screen = pygame.display.set_mode((defWidth, defHeight))
clock = pygame.time.Clock()
running = True

resFact = 12.0 # 5 to 30
resChangeSense = .1
incrRes = False
decRes = False

contrast = 0
contChangeSense = 4
incCont = False
decCont = False

imgMat = [[],[]]

text = pygame.font.Font("Courier_Prime/CourierPrime-Regular.ttf", round(resFact))

def getChar(pix):
    avg = (pix[0]+pix[1]+pix[2])/3
    dens = 'N@#W$9876543210?!abc;:+=-,._ '
    return dens[round((1-avg/255)*(len(dens)-1))]

def getChar2(pix):
    ch = ""
    spc = ""
    for _ in range(round(contrast)):
        spc += " "
    dens = 'N@#W$9876543210?!abc;:+=-,._ '
    densR = 'WEBOCIwxzuiL(|:. '
    densG = 'GHSQUJsgqpj[)/;, '
    densB = 'MKFDYVabdko{]!=` '
    if pix[0]>pix[1] and pix[0]>pix[2]:
        s = densR+spc
        ch = s[round((1-pix[0]/255)*(len(s)-1))]
    elif pix[1]>pix[0] and pix[1]>pix[2]:
        s = densG+spc
        ch = s[round((1-pix[0]/255)*(len(s)-1))]
    elif pix[2]>pix[1] and pix[2]>pix[1]:
        s = densB+spc
        ch = s[round((1-pix[0]/255)*(len(s)-1))]
    else:
        s = dens+spc
        ch = s[round((1-pix[0]/255)*(len(s)-1))]
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
            if event.key == pygame.K_UP:
                incrRes = True
            if event.key == pygame.K_DOWN:
                decRes = True
            if event.key == pygame.K_LEFT:
                decCont = True
            if event.key == pygame.K_RIGHT:
                incCont = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                incrRes = False
            if event.key == pygame.K_DOWN:
                decRes = False
            if event.key == pygame.K_LEFT:
                decCont = False
            if event.key == pygame.K_RIGHT:
                incCont = False
    if incrRes and resFact<=30:
        resFact += resChangeSense
    if decRes and resFact>=5:
        resFact -= resChangeSense
    if incCont and contrast<=50:
        contrast += resChangeSense
    if decCont and contrast>=1:
        contrast -= resChangeSense

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER
    camSurf = pygame.Surface((screen.get_width()//round(resFact), screen.get_height()//round(resFact)))
    camSurf.blit(pygame.transform.scale(pygame.transform.flip(cam.get_image(), 1, 0), (screen.get_width()//round(resFact), screen.get_height()//round(resFact))), (0,0))
    # screen.blit(camSurf, (0,0))
    imgMat = pygame.surfarray.pixels3d(camSurf)

    surf2 = pygame.Surface((screen.get_width(), screen.get_height()))

    text = pygame.font.Font("Courier_Prime/CourierPrime-Regular.ttf", round(resFact))
    for i in range(len(imgMat)):
        for j in range(len(imgMat[i])):
            surf2.blit(text.render(getChar2(imgMat[i][j]),True, (255, 255, 255)), (round(resFact)*i, round(resFact)*j))
    screen.blit(surf2, (0, 0))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()