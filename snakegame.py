import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))

# Set the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set the snake initial position and size
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"

# Set the desired direction of movement
desired_direction = snake_direction

# Set the food initial position
food_position = [random.randrange(1, (width // 10)) * 10,
                 random.randrange(1, (height // 10)) * 10]
food_spawn = True

# Set the game clock
clock = pygame.time.Clock()

# Set the game over flag
game_over = False

# Set the initial score
score = 0

# Game loop
while not game_over:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                desired_direction = "RIGHT"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                desired_direction = "LEFT"
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                desired_direction = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                desired_direction = "DOWN"

    # Update the snake_direction based on the desired_direction
    snake_direction = desired_direction

    # Move the snake
    if snake_direction == "RIGHT":
        snake_position[0] += 10
    if snake_direction == "LEFT":
        snake_position[0] -= 10
    if snake_direction == "UP":
        snake_position[1] -= 10
    if snake_direction == "DOWN":
        snake_position[1] += 10

    # Check if the snake hits the food
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop(0)

    # Spawn new food
    if not food_spawn:
        food_position = [random.randrange(1, (width // 10)) * 10,
                         random.randrange(1, (height // 10)) * 10]
        food_spawn = True

    # Create a new segment for the snake
    snake_body.append(list(snake_position))

    # Check if the snake hits itself or the boundaries
    if snake_position[0] < 0 or snake_position[0] > width-10:
        game_over = True
    if snake_position[1] < 0 or snake_position[1] > height-10:
        game_over = True
    for block in snake_body[:-1]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over = True

    # Set the background color
    window.fill(black)

    # Draw the snake
    for block in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(
            block[0], block[1], 10, 10))

    # Draw the food
    pygame.draw.rect(window, red, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    # Draw the score in the bottom right corner
    font = pygame.font.SysFont("comicsansms", 24)
    score_text = font.render("Score: " + str(score), True, white)
    score_rect = score_text.get_rect()
    score_rect.bottomright = (width - 10, height - 10)
    window.blit(score_text, score_rect)

    # Update the game window
    pygame.display.flip()

    # Set the game speed
    clock.tick(15)

# Game over message
font = pygame.font.SysFont("comicsansms", 72)
game_over_message = font.render("Game Over", True, blue)
game_over_rect = game_over_message.get_rect()
game_over_rect.midtop = (width/2, height/4)
window.blit(game_over_message, game_over_rect)
pygame.display.flip()

# Display the final score for a few seconds before closing the game
time.sleep(2)

# Quit the game
pygame.quit()
