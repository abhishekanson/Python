import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_width, player_height = 60, 15
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 7

# Block settings
block_width, block_height = 40, 40
block_x = random.randint(0, WIDTH - block_width)
block_y = -block_height
block_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)  # 60 FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    
    # Move block down
    block_y += block_speed
    
    # Check if block caught
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    block_rect = pygame.Rect(block_x, block_y, block_width, block_height)
    
    if block_rect.colliderect(player_rect):
        score += 1
        block_x = random.randint(0, WIDTH - block_width)
        block_y = -block_height
    
    # Check if block missed
    elif block_y > HEIGHT:
        running = False  # Game Over
    
    # Drawing everything
    screen.fill(WHITE)
    
    # Draw player
    pygame.draw.rect(screen, BLUE, player_rect)
    
    # Draw block
    pygame.draw.rect(screen, RED, block_rect)
    
    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()

pygame.quit()
print(f"Game Over! Your score: {score}")
