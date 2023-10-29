# WRITE YOUR SOLUTION HERE:
import pygame
import math
 
pygame.init()

wdw_width = 640
wdw_height = 480

window = pygame.display.set_mode((wdw_width, wdw_height))
robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

angle = 0
radius = 150
number = 10
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    for i in range(number):
        x = wdw_width / 2 + math.cos(angle + 2 * math.pi * i / number) * radius - width / 2
        y = wdw_height / 2 + math.sin(angle + 2 * math.pi * i / number) * radius - height / 2
        window.blit(robot, (x, y))
    pygame.display.flip()
 
    angle += 0.01
    clock.tick(60)