import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake variables
snake = [(5, 5)]
snake_direction = (1, 0)
snake_speed = 10

# Food variables
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle user input for changing direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, 1):
        snake_direction = (0, -1)
    if keys[pygame.K_DOWN] and snake_direction != (0, -1):
        snake_direction = (0, 1)
    if keys[pygame.K_LEFT] and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    if keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
        snake_direction = (1, 0)

    # Update the snake's position
    x, y = snake[0]
    new_head = (x + snake_direction[0], y + snake_direction[1])
    snake.insert(0, new_head)

    # Check for collision with food
    if snake[0] == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    # Check for collision with the wall or itself
    if (
        x < 0
        or x >= GRID_WIDTH
        or y < 0
        or y >= GRID_HEIGHT
        or snake[0] in snake[1:]
    ):
        pygame.quit()
        sys.exit()

    # Draw the screen
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(
            screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )
    pygame.draw.rect(
        screen, GREEN, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )
    pygame.display.update()

    # Control the game speed
    pygame.time.Clock().tick(snake_speed)
