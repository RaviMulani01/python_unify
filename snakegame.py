import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
GAME_OVER_COLOR = (255, 0, 0)
FONT_SIZE = 36

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize Snake
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = RIGHT

# Initialize Food
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game state
game_over = False

# Initialize font
font = pygame.font.Font(None, FONT_SIZE)

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP and snake_direction != DOWN:
                    snake_direction = UP
                elif event.key == pygame.K_DOWN and snake_direction != UP:
                    snake_direction = DOWN
                elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                    snake_direction = LEFT
                elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                    snake_direction = RIGHT
            else:
                if event.key == pygame.K_SPACE:
                    # Restart the game
                    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
                    snake_direction = RIGHT
                    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                    game_over = False

    if not game_over:
        # Move the snake
        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, new_head)

        # Check if the snake has collided with the wall or itself
        if (
            new_head[0] < 0
            or new_head[0] >= GRID_WIDTH
            or new_head[1] < 0
            or new_head[1] >= GRID_HEIGHT
            or new_head in snake[1:]
        ):
            game_over = True

        # Check if the snake has eaten the food
        if snake[0] == food:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()

    # Draw the background
    screen.fill(BACKGROUND_COLOR)

    if game_over:
        draw_text("Game Over!!", GAME_OVER_COLOR, WIDTH // 2, HEIGHT // 2)
        draw_text("Press SPACE to restart", GAME_OVER_COLOR, WIDTH // 2, HEIGHT // 2 + FONT_SIZE)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(
            screen,
            SNAKE_COLOR,
            pygame.Rect(
                segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE
            ),
        )

    # Draw the food
    pygame.draw.rect(
        screen,
        FOOD_COLOR,
        pygame.Rect(food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE),
    )

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(100)

# Quit Pygame
pygame.quit()
sys.exit()