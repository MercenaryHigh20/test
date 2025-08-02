import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake and food size
block_size = 20
snake_speed = 15

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Score display
def show_score(score):
    value = font.render("Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

# Draw snake
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block_size, block_size])

# Game loop
def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    dx = 0
    dy = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(black)
            msg = font.render("You lost! Press Q to Quit or R to Restart", True, red)
            screen.blit(msg, [width / 6, height / 3])
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -block_size
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = block_size
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -block_size
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = block_size
                    dx = 0

        # Snake movement
        x += dx
        y += dy

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check collision with self
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        show_score(length_of_snake - 1)

        pygame.display.update()

        # Check if food eaten
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
game_loop()