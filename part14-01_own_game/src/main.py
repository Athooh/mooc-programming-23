# The rule of the game is for robot to collect all the coins numbered without hitting the monster. 
# Everytime the robot collects a coin, the number of coins gets increased for 0-10
# The game game should end if the robot hits the monster

import pygame
import random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAYER_SPEED = 2
COIN_COUNT = 10
ENEMY_COUNT = 5


WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Coin Collector Game")

robot = pygame.image.load("robot.png")
player_rect = robot.get_rect()
player_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

coin_image = pygame.image.load("coin.png")
coins = [coin_image.get_rect(center=(random.randint(50, WINDOW_WIDTH - 50), random.randint(50, WINDOW_HEIGHT - 50))) for _ in range(COIN_COUNT)]

monster = pygame.image.load("monster.png")
monsters = [monster.get_rect(center=(random.randint(50, WINDOW_WIDTH - 50), random.randint(50, WINDOW_HEIGHT - 50))) for _ in range(ENEMY_COUNT)]

player_score = 0

font = pygame.font.Font(None, 36)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def check_collision(player, coins):
    for coin in coins:
        if player.colliderect(coin):
            coins.remove(coin)
            return True
    return False

def main():
    global player_score
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player_rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * PLAYER_SPEED
        player_rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * PLAYER_SPEED

        player_rect.x = max(0, min(player_rect.x, WINDOW_WIDTH - player_rect.width))
        player_rect.y = max(0, min(player_rect.y, WINDOW_HEIGHT - player_rect.height))

        if check_collision(player_rect, coins):
            player_score += 1

        for enemy in monsters:
            if player_rect.colliderect(enemy):
                running = False

        screen.fill(WHITE)

        for coin in coins:
            screen.blit(coin_image, coin)

        for enemy in monsters:
            screen.blit(monster, enemy)

        screen.blit(robot, player_rect)

        draw_text("Score: " + str(player_score), font, RED, 10, 10)

        pygame.display.flip()

        if player_score >= COIN_COUNT:
            draw_text("You Win!", font, YELLOW, WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 18)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
