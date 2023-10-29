# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()

wdw_width = 640
wdw_height = 480

window = pygame.display.set_mode((wdw_width, wdw_height))
robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

window.fill((0,0,0))

for i in range(1,10 + 1):
    for j in range(1, 10 + 1):
        window.blit(robot, (width - 60 * i, height + ))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()