#TODO: make it so that the keys only trigger one event when pressed and not multiple

import pygame
from pygame.locals import *
import random

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
FRAME_RATE = 25

score = 0
gameOver = False
cannonwidth = 20
cannonheight = 20
ballRadius = 8
cannonBalls = []
invaders = []
cannonxpos = WINDOW_WIDTH / 2
cannonypos = WINDOW_HEIGHT - cannonheight

cannonVel = 10


class cannonBall:

    def __init__(self, cbX, cbY):
        self.mask = pygame.mask.Mask((8, 8), True)
        self.cbX = cannonxpos + 10
        self.cbY = cannonypos + 10

    def animate(self):
        self.cbY -= 10


class invader:
    def __init__(self):
        self.mask = pygame.mask.Mask((20, 20), True)
        self.invX = random.randint(1, WINDOW_WIDTH - 20)
        self.invY = random.randint(1, 45)

    def animate(self):
        if not gameOver:
            self.invY += 3


def offset(mask1, mask2):
    return int(mask2.cbX - mask1.invX), int(mask2.cbY - mask1.invY)


pygame.init()

resetDone = False


def reset():
    global resetDone
    if resetDone:
        return
    invaders.clear()
    for x in range(3):
        invaders.append(invader())
    resetDone = True


def mousepress(event):
    global resetDone
    if event.type == MOUSEBUTTONDOWN:
        resetDone = False


def keypress():
    global resetDone
    global cannonxpos
    global cbY
    global cbX
    global gameOver
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if not gameOver:
            if cannonxpos > 0:
                cannonxpos -= cannonVel

    if keys[pygame.K_RIGHT]:
        if not gameOver:
            if cannonxpos < WINDOW_WIDTH - 20:
                cannonxpos += cannonVel

    elif keys[pygame.K_ESCAPE]:
        resetDone = False
        gameOver = False

    if keys[pygame.K_SPACE]:
        if not gameOver:
            cannonBalls.append(cannonBall(cannonxpos, cannonypos))


def paint():
    global score
    win.fill((0, 0, 0))

    drawcannon(cannonxpos, cannonypos, cannonwidth, cannonheight)
    for x in cannonBalls:
        drawCannonBall(x.cbX, x.cbY, ballRadius)

    for x in invaders:
        drawInvader(x.invX, x.invY)

    font = pygame.font.SysFont(None, 20)
    img = font.render('Score = ' + str(score), True, 'CYAN')
    win.blit(img, (10, 10))

    if gameOver:
        font = pygame.font.SysFont(None, 100)
        img = font.render('Game Over', True, 'RED')
        win.blit(img, (10, WINDOW_HEIGHT / 2))


def drawcannon(x, y, width, height):
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))


def drawCannonBall(x, y, radius):
    pygame.draw.circle(win, (255, 255, 255), (x, y), radius)


def drawInvader(x, y):
    pygame.draw.polygon(win, (0, 255, 0), [[x, y], [x + 20, y], [x + 10, y + 20]])


win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("SpaceInvaders")

run = True

while run:
    pygame.time.delay(int(1000 / FRAME_RATE))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        else:
            mousepress(event)

    for x in cannonBalls.copy():
        x.animate()
        if x.cbY < 20:
            cannonBalls.remove(x)

    for x in invaders.copy():
        x.animate()
        if x.invY > WINDOW_HEIGHT:
            invaders.clear()
            gameOver = True
            reset()

    for x in invaders.copy():
        for y in cannonBalls.copy():
            if x.mask.overlap(y.mask, offset(x, y)):
                if x in invaders:
                    invaders.remove(x)
                    score += 1
                if y in cannonBalls:
                    cannonBalls.remove(y)

    if len(invaders) == 0:
        resetDone = False

    reset()
    keypress()
    paint()

    pygame.display.update()

pygame.quit()