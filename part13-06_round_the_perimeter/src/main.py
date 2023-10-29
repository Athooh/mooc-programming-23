# # WRITE YOUR SOLUTION HERE:
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
velocity = 1
direction = 1 

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()


    if direction == 1:                               
        x += velocity
        if x + width == wdw_width:    
            direction = 2                              
    elif direction == 2:                               
        y += velocity
        if y + height == wdw_height:
            direction = 3                              
    elif direction == 3:                              
        x -= velocity
        if x == 0:                                 
            direction = 4
    elif direction == 4:                               
        y -= velocity
        if y == 0:                               
            direction = 1

    clock.tick(60)
