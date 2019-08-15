import random
import pygame
from pygame.locals import *

def on_grid_random():
    x = (random.randint(10,290))
    y = (random.randint(60,340))
    return (x //10 * 10, y //10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def pause():
    pause_screen_pos = (0, 50)
    pause_screen = pygame.Surface((300, 300))
    pause_screen.fill((255, 255, 255))
    screen.blit(pause_screen, pause_screen_pos)
    pause_txt_font = pygame.font.SysFont("Arial", 50, 1)
    pause_txt = pause_txt_font.render("PAUSE", 1, (0, 0, 0))
    c_q_font = pygame.font.SysFont("monospace", 15)
    c_txt = c_q_font.render("c to continue", 1, (0, 0, 0))
    q_txt = c_q_font.render("q to quit", 1, (0, 0, 0))
    screen.blit(pause_txt, (75,150))
    screen.blit(c_txt, (25, 200))
    screen.blit(q_txt, (200, 200))
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                if event.key == K_c:
                    waiting = False

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

game_over = False

points = 0
pygame.init()
screen = pygame.display.set_mode((300,400))
pygame.display.set_caption('Snake')
title_font = pygame.font.SysFont("monospace", 20, 1)
title = title_font.render("Artur Snake Test", 1, (255,255,255))
count_font = pygame.font.SysFont("arial", 15)


snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

border_left = (0,50)
border_right = (290,50)
border_bottom = (10,340)
border_top = (5,50)
border_vert = pygame.Surface((10,300))
border_vert.fill((255,255,255))
border_hor = pygame.Surface((290,10))
border_hor.fill((255,255,255))

my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(10)
    count = count_font.render(f"Points: {points}", 1, (255, 0, 0))
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    screen.blit(border_vert, border_left)
    screen.blit(border_vert, border_right)
    screen.blit(border_hor, border_top)
    screen.blit(border_hor, border_bottom)
    screen.blit(title, (60, 10))
    screen.blit(count, (10, 350))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_p:
                pause()


    if collision(snake[0], apple_pos):
        points = points + 1
        apple_pos = on_grid_random()
        snake.append((0, 0))

    if collision(snake[0], ((10,50),(290,50))):
        pause()

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    for pos in snake:
        screen.blit(snake_skin, pos)

    if snake[0][0] == 280 or snake[0][1] == 330 or snake[0][0] <= 10 or snake[0][1] <= 60:
        game_over = True

    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True

    pygame.display.update()

    if game_over:
        break