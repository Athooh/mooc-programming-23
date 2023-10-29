# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()

wdw_width = 640
wdw_height = 480

window = pygame.display.set_mode((wdw_width, wdw_height))

robot = pygame.image.load("robot.png")

number = 20

robots = []
for i in range(number):
    robots.append([-1000,wdw_height])

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for i in range(number):
        if robots[i][1]+robot.get_height() < wdw_height:
            robots[i][1] += 1
        else:
            if robots[i][0] < -robot.get_width() or robots[i][0] > wdw_width:
                robots[i][0] = randint(0,wdw_width-robot.get_width())
                robots[i][1] = -randint(100,1000)
            elif robots[i][0]+robot.get_width()/2 < wdw_width/2:
                    robots[i][0] -= 1
            else:
                robots[i][0] += 1

    window.fill((0, 0, 0))
    for i in range(number):
        window.blit(robot, (robots[i][0], robots[i][1]))
    pygame.display.flip()

    clock.tick(60)