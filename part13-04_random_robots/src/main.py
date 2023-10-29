# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()

wdw_width = 800
wdw_height = 600

window = pygame.display.set_mode((wdw_width, wdw_height))
robot = pygame.image.load("robot.png")

robot_width = robot.get_width()
robot_height = robot.get_height()

window.fill((0, 0, 0))

for _ in range(1000):
    x = random.randint(0, wdw_width - robot_width)
    y = random.randint(0, wdw_height - robot_height)
    window.blit(robot, (x, y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
