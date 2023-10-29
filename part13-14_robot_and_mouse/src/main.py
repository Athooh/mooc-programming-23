# WRITE YOUR SOLUTION HERE:
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

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x = event.pos[0] - width / 2
            y = event.pos[1] - height / 2
            
        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)