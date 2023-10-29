# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
pygame.display.set_caption("Asteroids")

wdw_width = 640
wdw_height = 480
screen = pygame.display.set_mode((wdw_width, wdw_height))
robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

robot_width = robot.get_width()
robot_height = robot.get_height()

rock_width = rock.get_width()
rock_height = rock.get_height()

x = wdw_width / 2 - robot_width / 2
y = wdw_height - robot_height
velocity = 3 
points = 0

number = 5
positions = []
for i in range(number):
    positions.append([randint(0, wdw_width - rock_width), - randint(100, 1000)])

right = False
left = False

clock = pygame.time.Clock()
font_family = pygame.font.SysFont("Arial", 24)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False

        if event.type == pygame.QUIT:
            exit()

    if right:
        if x + robot_width < wdw_width:
            x += velocity
    if left:
        if x > 0:
            x -= velocity 

    for i in range(number):
        positions[i][1] += 1
        if positions[i][1] + rock_width >= wdw_height:
            exit()
        if positions[i][1] + rock_height >= y:
            robot_middle = x + robot_width / 2
            rock_middle = positions[i][0] + rock_width / 2
            if abs(robot_middle - rock_middle) <= (robot_width + rock_width)/2:
                positions[i][0] = randint(0, wdw_width - rock_width)
                positions[i][1] = -randint(100, 1000)
                points += 1

    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))

    for i in range(number):
        screen.blit(rock, (positions[i][0], positions[i][1]))

    text = font_family.render("Points: " + str(points), True, (255, 0, 0))
    screen.blit(text, (wdw_width - 150, 10))

    pygame.display.flip()

    clock.tick(60)