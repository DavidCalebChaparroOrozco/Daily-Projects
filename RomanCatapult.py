# Import necessary libraries
import pygame
import math
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 0.5
GROUND_HEIGHT = SCREEN_HEIGHT - 50

# Colors
DARK_BG = (26, 26, 26)  # #1a1a1a
LIGHT_TEXT = (230, 230, 230)  # #e6e6e6
ACCENT_COLOR = (212, 175, 55)  # #d4af37
WOOD_COLOR = (101, 67, 33)
GROUND_COLOR = (139, 69, 19)
SKY_COLOR = (135, 206, 235)
TARGET_COLOR = (200, 0, 0)
PROJECTILE_COLOR = (50, 50, 50)

class CatapultGame:
    def __init__(self):
        # Game variables
        self.angle = 45
        self.power = 50
        self.projectiles = []
        self.targets = []
        self.score = 0
        self.catapult_pos = (100, GROUND_HEIGHT - 30)
        self.game_active = False
        self.font = pygame.font.SysFont('Arial', 24)
        self.title_font = pygame.font.SysFont('Arial', 36, bold=True)
        
        # Setup pygame screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Roman Catapult by David Caleb")
        
        # Generate initial target
        self.generate_target()
        
    # Generate a new target at a random position
    def generate_target(self):
        x = random.randint(SCREEN_WIDTH // 2, SCREEN_WIDTH - 50)
        y = GROUND_HEIGHT - random.randint(20, 100)
        width = random.randint(30, 60)
        height = random.randint(20, 40)
        
        self.targets.append({
            'rect': pygame.Rect(x, y, width, height),
            'points': width  # Bigger targets give fewer points
        })
        
    # Fire a projectile from the catapult
    def fire_projectile(self):
        if not self.game_active:
            return
            
        # Calculate velocity components
        rad_angle = math.radians(self.angle)
        velocity_x = math.cos(rad_angle) * self.power * 0.5
        velocity_y = -math.sin(rad_angle) * self.power * 0.5
        
        # Add new projectile
        self.projectiles.append({
            'pos': list(self.catapult_pos),
            'vel': [velocity_x, velocity_y],
            'radius': 10
        })
        
    # Start a new game
    def start_game(self):
        self.game_active = True
        self.score = 0
        self.projectiles = []
        self.targets = []
        self.generate_target()
        
    # Update game state
    def update_game(self):
        # Update projectiles
        for proj in self.projectiles[:]:
            # Update position
            proj['pos'][0] += proj['vel'][0]
            proj['pos'][1] += proj['vel'][1]
            
            # Apply gravity
            proj['vel'][1] += GRAVITY
            
            # Check if projectile hit the ground
            if proj['pos'][1] + proj['radius'] >= GROUND_HEIGHT:
                self.projectiles.remove(proj)
                continue
                
            # Check if projectile went off screen
            if (proj['pos'][0] < 0 or proj['pos'][0] > SCREEN_WIDTH or 
                proj['pos'][1] < 0 or proj['pos'][1] > SCREEN_HEIGHT):
                self.projectiles.remove(proj)
                continue
                
            # Check for collisions with targets
            proj_rect = pygame.Rect(
                proj['pos'][0] - proj['radius'],
                proj['pos'][1] - proj['radius'],
                proj['radius'] * 2,
                proj['radius'] * 2
            )
            
            for target in self.targets[:]:
                if proj_rect.colliderect(target['rect']):
                    # Target hit!
                    self.score += max(1, 10 - (target['points'] // 5))
                    self.targets.remove(target)
                    self.projectiles.remove(proj)
                    self.generate_target()
                    break
        
        # Generate new targets if none exist
        if not self.targets and self.game_active:
            self.generate_target()
            
    # Draw everything on the screen
    def draw(self):
        # Fill background (dark)
        self.screen.fill(DARK_BG)
        
        # Draw game area background (sky)
        pygame.draw.rect(
            self.screen, 
            SKY_COLOR,
            (0, 0, SCREEN_WIDTH, GROUND_HEIGHT)
        )
        
        # Draw ground
        pygame.draw.rect(
            self.screen, 
            GROUND_COLOR,
            (0, GROUND_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_HEIGHT)
        )
        
        # Draw catapult base
        pygame.draw.rect(
            self.screen,
            WOOD_COLOR,
            (self.catapult_pos[0] - 30, self.catapult_pos[1] - 10, 60, 20)
        )
        
        # Draw catapult arm
        arm_length = 50
        end_x = self.catapult_pos[0] + math.cos(math.radians(self.angle)) * arm_length
        end_y = self.catapult_pos[1] - math.sin(math.radians(self.angle)) * arm_length
        
        pygame.draw.line(
            self.screen,
            WOOD_COLOR,
            self.catapult_pos,
            (end_x, end_y),
            8
        )
        
        # Draw projectiles
        for proj in self.projectiles:
            pygame.draw.circle(
                self.screen,
                PROJECTILE_COLOR,
                (int(proj['pos'][0]), int(proj['pos'][1])),
                proj['radius']
            )
        
        # Draw targets
        for target in self.targets:
            pygame.draw.rect(
                self.screen,
                TARGET_COLOR,
                target['rect']
            )
        
        # Draw UI elements
        self.draw_ui()
        
    # Draw user interface elements
    def draw_ui(self):
        # Draw title
        title_text = self.title_font.render("ROMAN CATAPULT", True, ACCENT_COLOR)
        self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 20))
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, LIGHT_TEXT)
        self.screen.blit(score_text, (20, 20))
        
        # Draw angle and power indicators
        angle_text = self.font.render(f"Angle: {self.angle}°", True, LIGHT_TEXT)
        power_text = self.font.render(f"Power: {self.power}", True, LIGHT_TEXT)
        
        self.screen.blit(angle_text, (20, 60))
        self.screen.blit(power_text, (20, 90))
        
        # Draw instructions or start message
        if not self.game_active:
            start_text = self.font.render("Press SPACE to start game", True, LIGHT_TEXT)
            self.screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
            
            controls_text = self.font.render("Use ARROW KEYS to adjust angle and power", True, LIGHT_TEXT)
            self.screen.blit(controls_text, (SCREEN_WIDTH // 2 - controls_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))
            
            fire_text = self.font.render("Press F to fire", True, LIGHT_TEXT)
            self.screen.blit(fire_text, (SCREEN_WIDTH // 2 - fire_text.get_width() // 2, SCREEN_HEIGHT // 2 + 80))
        
    # Main game loop
    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.game_active:
                        self.start_game()
                    elif event.key == pygame.K_f and self.game_active:
                        self.fire_projectile()
            
            # Handle continuous key presses
            keys = pygame.key.get_pressed()
            if self.game_active:
                if keys[pygame.K_UP] and self.power < 100:
                    self.power += 1
                if keys[pygame.K_DOWN] and self.power > 10:
                    self.power -= 1
                if keys[pygame.K_LEFT] and self.angle < 80:
                    self.angle += 1
                if keys[pygame.K_RIGHT] and self.angle > 10:
                    self.angle -= 1
            
            # Update game state
            if self.game_active:
                self.update_game()
            
            # Draw everything
            self.draw()
            
            # Update display
            pygame.display.flip()
            
            # Cap the frame rate
            clock.tick(60)
        
        pygame.quit()

# Run the game
if __name__ == "__main__":
    game = CatapultGame()
    game.run()