#replicating chapter 20
import pygame, random, sys, time
from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()

def drawText(textContent, size, surface, x, y):
    fontItem = pygame.font.SysFont(None, size)
    textObj = fontItem.render(textContent, 1 , (255,255,255))
    textRect = textObj.get_rect()
    textRect.topleft = (x,y)
    mainSurface.blit(surface, textRect)

pygame.init()

#Environment
mainClock = pygame.time.Clock()
FPS = 40

#mainSurface
WIN_WIDTH = 500
WIN_HEIGHT = 500
mainSurface = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT),0,32)
pygame.display.set_caption('baddies')



#colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#sounds
endGameSound = pygame.mixer.Sound('gameover.wav')
endGameSound.set_volume(0.5)

#player
PLAYERSPEED = 6
player = {'rect':pygame.Rect(WIN_WIDTH / 2, WIN_HEIGHT /2, 10,10),
          'image':pygame.image.load('player.png'),
          'speed':PLAYERSPEED}
moveUp = moveDown = moveLeft = moveRight = False

#baddies
BMAXSIZE = 40
BMINSIZE = 10
BMAXSPEED = 5
BMINSPEED = 1
MAXBADDIECOUNT = 40
baddieCount = 0
BADDIEIMAGE = pygame.image.load('baddie.png')
baddies = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                moveUp = True
                moveDown = False
            if event.key == K_DOWN:
                moveDown = True
                moveUp = False
            if event.key == K_LEFT:
                moveLeft = True
                moveRight = False
            if event.key == K_RIGHT:
                moveRight = True
                moveLeft = False
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate()
            if event.key == K_UP:
                moveUp = False
            if event.key == K_DOWN:
                moveDown = False
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False

    #add baddies
    if baddieCount != MAXBADDIECOUNT:
        baddieSize = random.randint(BMINSIZE, BMAXSIZE)
        baddies.append({'rect':pygame.Rect(random.randint(0,WIN_WIDTH - baddieSize),
                                          0,
                                          baddieSize,
                                          baddieSize),
                       'speed':random.randint(BMINSPEED,BMAXSPEED)})
        baddieCount += 1

    #move player
    if moveUp and player['rect'].top >= 0:
        player['rect'].top -= PLAYERSPEED
    if moveDown and player['rect'].bottom <= WIN_HEIGHT:
        player['rect'].top += PLAYERSPEED
    if moveLeft and player['rect'].left >= 0:
        player['rect'].left -= PLAYERSPEED
    if moveRight and player['rect'].right <= WIN_WIDTH:
        player['rect'].left += PLAYERSPEED

    #move baddies
    for baddie in baddies:
        baddie['rect'].top += baddie['speed']

    #detect when baddie off the bottom edge
    for baddie in baddies[:]:
        if baddie['rect'].top >= WIN_HEIGHT:
            baddies.remove(baddie)
            baddieCount -= 1

    #detect collisions
    for baddie in baddies:
        if baddie['rect'].colliderect(player['rect']):
            endGameSound.play(0,0)
    
    #draw background
    mainSurface.fill(BLACK)

    #draw player
    mainSurface.blit(player['image'], player['rect'])

    #draw baddies
    for baddie in baddies:
        mainSurface.blit(BADDIEIMAGE,baddie['rect'])

    fontItem = pygame.font.SysFont(None, 44)

    textObj = fontItem.render('test', 1 , (255,255,255))
    textRect = textObj.get_rect()
    textRect.topleft = (100,100)
    mainSurface.blit(mainSurface, textRect)
##    drawText('test',22,mainSurface, 100,100)

    pygame.display.update()
    mainClock.tick(FPS)

