import pygame, sys
import random
import math
from pygame import mixer

# Intialize the pygame
pygame.init()

# Giving values to color
black = (0, 0, 0)

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('city.png')

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Corona Catch")
icon = pygame.image.load('firstgame_logo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('gunrocket.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

exitgame = False

if exitgame == False:
    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('firstgame_logo.png'))
        enemyX.append(random.randint(0, 735))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(1)
        enemyY_change.append(40)

# bullet
# Ready state: You can't see the bullet on the screen
# Fire state: The bullet is moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# GAme over text
#over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    scoredisp = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(scoredisp, (x, y))
    line = font.render("______________________________________________________________________________", True, (173, 171, 176))
    screen.blit(line, (0, 430))
    rules = font.render("Press Right/Left Arrow To Move & Space to Shoot", True, (255, 255, 255))
    screen.blit(rules, (10, 560))


def player(x, y):
    screen.blit(playerImg, (round(x), round(y)))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (round(x), round(y)))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# running = False
# intro screen
def introfunc():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    break

        screen.fill((50, 147, 68))
        IntroText1 = font.render("Welcome to Corona Catch!!", True, (255, 255, 255))
        screen.blit(IntroText1, (200,150))
        IntroText2 = font.render("Shoot Max no of Corona Possible", True, (255, 255, 255))
        screen.blit(IntroText2, (130, 200))
        IntroText4 = font.render("By pressing Space button", True, (255, 255, 255))
        screen.blit(IntroText4, (200, 230))
        IntroText5 = font.render("Aim: Corona should not touch the line", True, (240, 232, 19))
        screen.blit(IntroText5, (120, 280))
        IntroText6 = font.render("Ready?", True, (255, 255, 255))
        screen.blit(IntroText6, (310, 360))
        IntroText3 = font.render("Start by pressing space", True, (255, 255, 255))
        screen.blit(IntroText3, (200, 450))
        pygame.display.update()

def lastfunc():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    break

        screen.fill((166, 138, 191))
        IntroText1 = font.render("Oops! GAME OVER!!", True, (255, 255, 255))
        screen.blit(IntroText1, (200, 150))
        IntroText2 = font.render("Your Score is "+str(score)+" !!", True, (255, 255, 255))
        screen.blit(IntroText2, (200, 250))
        IntroText3 = font.render("Press Space To Exit!!", True, (255, 255, 255))
        screen.blit(IntroText3, (200, 350))
        pygame.display.update()


introfunc()

# Game loop : This holds the screen

running = True
while running:

    gameend = False
    # rgb format
    screen.fill((0, 255, 0))

    # background image
    screen.blit(background, (0, 0))

    # playerX += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check which key is pressed right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # print("Left arrow is pressed")
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                # print("Right arrow is pressed")
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("Keystroke has been released")
                playerX_change = 0

    # To make the player remains inside the screen
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # To handle array of enemies

    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[i] = 2000
            running = False #17 Nov
            exitgame = True
            break

        # To ensure enemy remains inside the screen
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collide_sound = mixer.Sound('explosion.wav')
            collide_sound.play()
            bulletY = 480
            bullet_state = "ready"
            if exitgame == False:
                score += 1
            # print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        # To stop the enemy when it reaches at coordinates of player
        if enemyY[i] >= 480:
            enemyX_change[i] = 0
            enemyY_change[i] = 0

        # calling function enemy
        enemy(enemyX[i], enemyY[i], i)

    if exitgame:
        lastfunc()
        break
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # calling function player
    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()

