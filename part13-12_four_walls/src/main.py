# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

wdw_width = 640
wdw_height = 480

window = pygame.display.set_mode((wdw_width, wdw_height))
robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

x = 200
y = 200
velocity = 2

right = False
left = False
up = False
down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
        
        if event.type == pygame.QUIT:
            exit()

    if right:
        if x + width < wdw_width:
            x += velocity
    if left:
        if x > 0:
            x -= velocity
    if down:
        if y + height < wdw_height:
            y += 2
    if up:
        if y > 0:
            y -= 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)