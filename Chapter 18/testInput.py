#testInput.py Jordan's Test Input
import pygame, sys, random
from pygame.locals import *

#check for collision
def doRectsOverlap(rect1, rect2):
    for a,b in [(rect1, rect2),(rect2, rect1)]:
        if (isPointInsideRect(a.left, a.top, b) or
            isPointInsideRect(a.left, a.bottom, b) or
            isPointInsideRect(a.right, a.top, b) or
            isPointInsideRect(a.right, a.bottom, b)):
            return True
    
    return False

def isPointInsideRect(x,y,rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

def drawText(content):
    #debug info
    basicFont = pygame.font.SysFont(None, 22)
    text = basicFont.render(content, True, GREEN, (0,0,255))

    return text

#main game
pygame.init()
mainClock = pygame.time.Clock()

WIN_WIDTH = 400
WIN_HEIGHT = 300
windowSurface = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT),0,32)
pygame.display.set_caption('Jordans Test Input')

player = pygame.Rect(100,100,30,30)
foodSize = 10
foods = []
foodCount = 20
foodTimerMax = 30
foodTimer = 0

for food in range(foodCount):
    foods.append(pygame.Rect(random.randint(0, WIN_WIDTH - foodSize),
                             random.randint(0, WIN_HEIGHT - foodSize),
                             foodSize,
                             foodSize))
GREEN = (0,255,0)

PLAYER_SPEED = 4
moveLeft = False
moveRight = False
moveDown = False
moveUp = False
moveRandom = False



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

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
            if event.key == ord('x'):
                moveRandom = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_UP:
                moveUp = False
            if event.key == K_DOWN:
                moveDown = False
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False
            if event.key == ord('x'):
                moveRandom = False

    if moveUp and player.top > 0:
        player.top -= PLAYER_SPEED
    if moveDown and player.bottom < WIN_HEIGHT:
        player.bottom += PLAYER_SPEED
    if moveLeft and player.left > 0:
        player.left -= PLAYER_SPEED
    if moveRight and player.right < WIN_WIDTH:
        player.right += PLAYER_SPEED
    if moveRandom:
        player.x = random.randint(0, WIN_WIDTH - player.width)
        player.y = random.randint(0, WIN_HEIGHT - player.height)
        
    windowSurface.fill((0,0,0))
    pygame.draw.rect(windowSurface,(255,255,255),player)

    #check if should add food
    foodTimer += 1
    if foodTimer == foodTimerMax:
        foodTimer = 0
        foods.append(pygame.Rect(random.randint(0, WIN_WIDTH - foodSize),
                             random.randint(0, WIN_HEIGHT - foodSize),
                             foodSize,
                             foodSize))

    #draw food
    for food in foods[:]:
        if doRectsOverlap(food, player):
            foods.remove(food)
        else:
            pygame.draw.rect(windowSurface, GREEN, food)

    text = drawText(str(len(foods)))
    pygame.draw.rect(windowSurface, (255,255,255), text.get_rect())
    windowSurface.blit(text, text.get_rect())

    pygame.display.update()
    mainClock.tick(40)
