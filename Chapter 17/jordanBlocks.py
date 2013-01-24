#jordanBlocks.py Testing block animation

import pygame, sys, time
from pygame.locals import *

pygame.init()

#setting window properties using the pygame.display module
WINDOWWIDTH = 400
WINDOWHEIGHT = 300
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('animation')

UPLEFT = 7
UPRIGHT = 9
DOWNLEFT = 1
DOWNRIGHT = 3

MOVESPEED = 11

b1 = {'rect':pygame.Rect(100,100, 40, 40),'color':(30,30,30),'dir':UPLEFT}
b2 = {'rect':pygame.Rect(100,100, 40, 40),'color':(0, 0, 255),'dir':UPRIGHT}
b3 = {'rect':pygame.Rect(100,100, 40, 40),'color':(0, 255, 0),'dir':DOWNLEFT}
b4 = {'rect':pygame.Rect(100,100, 40, 40),'color':(255, 0, 0),'dir':DOWNRIGHT}

blocks = [b1,b2,b3,b4]

#game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill((0,0,0))
    for b in blocks:
        
        #decide how to move the block
        if b['dir'] == UPLEFT:
            b['rect'].x -= MOVESPEED
            b['rect'].y -= MOVESPEED
        elif b['dir'] == UPRIGHT:
            b['rect'].x += MOVESPEED
            b['rect'].y -= MOVESPEED
        elif b['dir'] == DOWNLEFT:
            b['rect'].x -= MOVESPEED
            b['rect'].y += MOVESPEED
        elif b['dir'] == DOWNRIGHT:
            b['rect'].x += MOVESPEED
            b['rect'].y += MOVESPEED

        #decide if the block needs to change dir
        if b['rect'].top < 0:
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
            else:    
                b['dir'] = DOWNLEFT
        elif b['rect'].left < 0:
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
            else:
                b['dir'] = DOWNRIGHT
        elif b['rect'].right > WINDOWWIDTH:
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            else:
                b['dir'] = UPLEFT
        elif b['rect'].bottom > WINDOWHEIGHT:
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
            else:
                b['dir'] = UPLEFT

        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    pygame.display.update()
    time.sleep(0.02)
                    
