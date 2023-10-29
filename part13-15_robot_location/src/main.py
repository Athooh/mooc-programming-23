# WRITE YOUR SOLUTION HERE:
from random import randint
import pygame

pygame.init()

wdw_width = 640
wdw_height = 480

window = pygame.display.set_mode((wdw_width, wdw_height))
robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

x = 0
y = 0
location_x = 0
location_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            location_x = event.pos[0]
            location_y = event.pos[1]

            if location_x > x and location_x < x + robot.get_width() and location_y > y and location_x < x + robot.get_width():
                x = randint(0, 640 - robot.get_width())
                y = randint(0, 480 - robot.get_height())

        window.fill((0, 0, 0))
        window.blit(robot, (x, y))
        pygame.display.flip()

        if event.type == pygame.QUIT:
            exit()