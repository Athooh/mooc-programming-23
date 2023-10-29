# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
robot1 = pygame.image.load("robot.png")

x = 0
y = 50

i = 0
j = 150

velocity = 1
velocity1 = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot1, (i, j))
    pygame.display.flip()
    
    x += velocity
    if velocity > 0 and x+robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity
        
    i += velocity1
    if velocity1 > 0 and i+robot.get_width() >= 640:
        velocity1 = -velocity1
    if velocity1 < 0 and i <= 0:
        velocity1 = -velocity1

    clock.tick(60)