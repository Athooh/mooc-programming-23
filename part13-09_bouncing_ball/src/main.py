# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()

wdw_width = 640
wdw_height = 480

window = pygame.display.set_mode((wdw_width, wdw_height))
ball = pygame.image.load("ball.png")

width = ball.get_width()
height = ball.get_height()

x = 320
y = 240
h = 1

x_velocity = 2
y_velocity = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))    
    window.blit(ball, (x, y))
    pygame.display.flip()

    if x + width >= 640 or x <= 0:
        x_velocity = -x_velocity
    if y + height >= 480 or y <= 0:
        y_velocity = -y_velocity

    x += x_velocity
    y += y_velocity

    clock.tick(60)