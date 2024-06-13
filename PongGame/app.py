# Importing necessary libraries
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BALL_SPEED = 7
PADDLE_SPEED = 7
BALL_RADIUS = 15
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
FONT_SIZE = 50
WIN_SCORE = 5

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong by David Caleb")

# Font setup
font = pygame.font.Font(None, FONT_SIZE)

# Ball class
class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.x_speed = BALL_SPEED * random.choice((1, -1))
        self.y_speed = BALL_SPEED * random.choice((1, -1))

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

        # Ball collision with top or bottom
        if self.y - BALL_RADIUS <= 0 or self.y + BALL_RADIUS >= SCREEN_HEIGHT:
            self.y_speed *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), BALL_RADIUS)

    def reset(self):
        self.__init__()

# Paddle class
class Paddle:
    def __init__(self, x, color):
        self.x = x
        self.y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
        self.y_speed = 0
        self.color = color

    def move(self):
        self.y += self.y_speed

        # Paddle collision with top or bottom
        if self.y < 0:
            self.y = 0
        if self.y + PADDLE_HEIGHT > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - PADDLE_HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

# Game loop
def game_loop():
    ball = Ball()
    left_paddle = Paddle(30, RED)
    right_paddle = Paddle(SCREEN_WIDTH - 50, BLUE)
    clock = pygame.time.Clock()
    running = True
    left_score = 0
    right_score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    left_paddle.y_speed = -PADDLE_SPEED
                if event.key == pygame.K_s:
                    left_paddle.y_speed = PADDLE_SPEED
                if event.key == pygame.K_UP:
                    right_paddle.y_speed = -PADDLE_SPEED
                if event.key == pygame.K_DOWN:
                    right_paddle.y_speed = PADDLE_SPEED
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    left_paddle.y_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    right_paddle.y_speed = 0

        # Move the ball and paddles
        ball.move()
        left_paddle.move()
        right_paddle.move()

        # Ball collision with paddles
        if ball.x - BALL_RADIUS <= left_paddle.x + PADDLE_WIDTH and left_paddle.y <= ball.y <= left_paddle.y + PADDLE_HEIGHT:
            ball.x_speed *= -1
        if ball.x + BALL_RADIUS >= right_paddle.x and right_paddle.y <= ball.y <= right_paddle.y + PADDLE_HEIGHT:
            ball.x_speed *= -1

        # Ball out of bounds
        if ball.x < 0:
            right_score += 1
            ball.reset()
        if ball.x > SCREEN_WIDTH:
            left_score += 1
            ball.reset()

        # Check for win condition
        if left_score == WIN_SCORE or right_score == WIN_SCORE:
            running = False

        # Drawing everything
        screen.fill(BLACK)
        ball.draw(screen)
        left_paddle.draw(screen)
        right_paddle.draw(screen)

        # Draw scores
        left_text = font.render(str(left_score), True, WHITE)
        right_text = font.render(str(right_score), True, WHITE)
        screen.blit(left_text, (SCREEN_WIDTH // 4, 20))
        screen.blit(right_text, (3 * SCREEN_WIDTH // 4, 20))

        pygame.display.flip()
        clock.tick(60)

    # Display the winner
    screen.fill(BLACK)
    if left_score == WIN_SCORE:
        win_text = font.render("Red Wins!", True, RED)
    else:
        win_text = font.render("Blue Wins!", True, BLUE)
    screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 2 - win_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()

if __name__ == "__main__":
    game_loop()
