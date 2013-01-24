#trying to remember drawing objects and shiz
import pygame, random, sys, time
from pygame.locals import *

#set up pygame
pygame.init()
mainClock = pygame.time.Clock()

#set up main surface
WIN_WIDTH = 400
WIN_HEIGHT = 300
mainSurface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT),0,32)
pygame.display.set_caption('Remember dis')

#set up the player and resources
player = pygame.Rect(100,100,20,20)
playerImage = pygame.image.load('player.png')
playerStretchedImage = pygame.transform.scale(playerImage,(20,20))
foodImage = pygame.image.load('cherry.png')
foods = []
foodCounter = 0
NEWFOOD = 40
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WIN_WIDTH - 20),
                             random.randint(0, WIN_HEIGHT - 20),
                             10,
                             10))

#set up environment variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
PLAYERSPEED = 6

#set up the sounds
pickUpSound = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('background.mid')
playMusic = False

#main loop
while True:
    #event checking
    for event in pygame.event.get():
        #begin event for loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveLeft = True
                moveRight = False
            if event.key == K_RIGHT:
                moveRight = True
                moveLeft = False
            if event.key == K_UP:
                moveUp = True
                moveDown = False
            if event.key == K_DOWN:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False
            if event.key == K_UP:
                moveUp = False
            if event.key == K_DOWN:
                moveDown = False
            if event.key == ord('x'):
                for i in range(random.randint(1, 10)):
                    foods.append(pygame.Rect(random.randint(0, WIN_WIDTH - 10),
                                            random.randint(0, WIN_HEIGHT - 10),
                                            10,
                                            10))
            if event.key == ord('m'):
                if playMusic:
                    pygame.mixer.music.play(-1,0.0)
                else:
                    pygame.mixer.music.stop()
                playMusic = not playMusic
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        #end event for loop

    #check food counters
    foodCounter+=1
    if foodCounter == NEWFOOD:
        foods.append(pygame.Rect(random.randint(0, WIN_WIDTH - 10),
                                 random.randint(0, WIN_HEIGHT - 10),
                                 10,
                                 10))
        foodCounter = 0

    #move player
    if moveUp:
        player.top -= PLAYERSPEED
    if moveDown:
        player.top += PLAYERSPEED
    if moveLeft:
        player.left -= PLAYERSPEED
    if moveRight:
        player.left += PLAYERSPEED

    #check if food collides with player
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left,
                                 player.top,
                                 player.width + 2,
                                 player.height + 2)
            playerStretchedImage = pygame.transform.scale(playerImage,
                                                          (player.width,
                                                           player.height))
            if playMusic:
                pickUpSound.play()

    #draw surface
    mainSurface.fill((0,0,0))

    #draw player
    mainSurface.blit(playerStretchedImage, player)
                
    #draw food
    for food in foods:
        mainSurface.blit(foodImage, food)

    #update
    pygame.display.update()
    
    #clock timer
    mainClock.tick(40)    
