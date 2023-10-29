# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

wdw_width = 640
wdw_height = 480

window = pygame.display.set_mode((wdw_width, wdw_height))
robot = pygame.image.load("robot.png") 

width = robot.get_width()
height = robot.get_height()

#ROBOT1
x_1 = wdw_width - width
y_1 = 0

#ROBOT2
x_2 = 0
y_2 = 0

velocity = 3

#ROBOT1
right1 = False
left1 = False
up1 = False
down1 = False

#ROBOT2
right2 = False
left2 = False
up2 = False
down2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #ROBOT1
            if event.key == pygame.K_RIGHT:
                right1 = True
            if event.key == pygame.K_LEFT:
                left1 = True
            if event.key == pygame.K_UP:
                up1 = True
            if event.key == pygame.K_DOWN:
                down1 = True

            #ROBOT2
            if event.key == pygame.K_d:
                right2 = True
            if event.key == pygame.K_a:
                left2 = True
            if event.key == pygame.K_w:
                up2 = True
            if event.key == pygame.K_s:
                down2 = True      

        if event.type == pygame.KEYUP:
            #ROBOT1
            if event.key == pygame.K_RIGHT:
                right1 = False
            if event.key == pygame.K_LEFT:
                left1 = False
            if event.key == pygame.K_UP:
                up1 = False
            if event.key == pygame.K_DOWN:
                down1 = False

            #ROBOT2
            if event.key == pygame.K_d:
                right2 = False
            if event.key == pygame.K_a:
                left2 = False
            if event.key == pygame.K_w:
                up2 = False
            if event.key == pygame.K_s:
                down2 = False

        if event.type == pygame.QUIT:
            exit()

    #ROBOT1
    if right1:
        if x_1 < wdw_width - width:
            x_1 += velocity
    if left1:
        if x_1 > 0:
            x_1 -= velocity
    if up1:
        if y_1 > 0:
            y_1 -= velocity
    if down1:
        if y_1 < wdw_height - height:
            y_1 += velocity

    #ROBOT2
    if right2:
        if x_2 < wdw_width - width:
            x_2 += velocity
    if left2:
        if x_2 > 0:
            x_2 -= velocity
    if up2:
        if y_2 > 0:
            y_2 -= velocity
    if down2:
        if y_2 < wdw_height - height:
            y_2 += velocity

    window.fill((0, 0, 0))
    window.blit(robot, (x_1, y_1))
    window.blit(robot, (x_2, y_2))
    pygame.display.flip()

    clock.tick(60)
