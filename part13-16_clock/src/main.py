# WRITE YOUR SOLUTION HERE:
import pygame
import math
from datetime import datetime

pygame.init()
wdw_width = 640
wdw_height = 480
screen = pygame.display.set_mode((wdw_width, wdw_height))

def circle(color: int, radius: int):
    pygame.draw.circle(screen, color, (centre_x, centre_y), radius)

def clock_hand(length: int, thickness: int, proportion: float):
    angle = 2 * math.pi * proportion - math.pi / 2
    end_x = centre_x + math.cos(angle) * length
    end_y = centre_y + math.sin(angle) * length

    pygame.draw.line(screen, (0, 0, 255), (centre_x, centre_y), (end_x, end_y), thickness)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    hours = datetime.now().hour % 12
    minutes = datetime.now().minute
    seconds = datetime.now().second

    pygame.display.set_caption(str(datetime.now().time())[:8])

    screen.fill((0, 0, 0))

    centre_x = wdw_width / 2
    centre_y = wdw_height / 2

    circle((255, 0, 0), 200)
    circle((0, 0, 0), 195)
    circle((255, 0, 0), 10)

    clock_hand(185, 1, seconds / 60)
    clock_hand(180, 2, (minutes + seconds / 60) / 60)
    clock_hand(150, 5, (hours + minutes / 60 + seconds / 3600) / 12)

    pygame.display.flip()