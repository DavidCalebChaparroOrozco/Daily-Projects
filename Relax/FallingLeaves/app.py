# Import necessary libraries
import pygame
import random
import math
from pygame.locals import *

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Leaves - Autumn Animation")

# Colors
SKY_BLUE = (135, 206, 235)
GROUND_BROWN = (139, 69, 19)
LEAF_COLORS = [
    # Orange
    (255, 165, 0),    
    # Red-Orange
    (255, 69, 0),      
    # Firebrick
    (178, 34, 34),     
    # Chocolate
    (210, 105, 30),    
    # Gold
    (255, 215, 0)      
]

# Leaf class to represent each falling leaf
class Leaf:
    def __init__(self):
        # Random position at the top of the screen
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-50, -10)
        
        # Random size
        self.size = random.randint(10, 25)
        
        # Random shape (0-2 for different leaf shapes)
        self.shape = random.randint(0, 2)
        
        # Random color from our leaf palette
        self.color = random.choice(LEAF_COLORS)
        
        # Physics properties
        # Falling speed
        self.velocity_y = random.uniform(0.5, 2.0)  
        # Horizontal movement
        self.velocity_x = random.uniform(-0.5, 0.5)  
        self.rotation = 0
        self.rotation_speed = random.uniform(-2, 2)
        self.wind_effect = 0
        # How much wind affects the leaf
        self.wind_resistance = random.uniform(0.9, 0.98)  
        
        # For advanced physics
        self.time = 0
        # For swaying motion
        self.amplitude = random.uniform(0.5, 2.0)  
    
    def update(self):
        # Apply gravity
        self.velocity_y += 0.05
        
        # Random wind effect that changes over time
        self.wind_effect = math.sin(self.time * 0.1) * random.uniform(0.5, 1.5)
        
        # Update position with wind effect
        self.velocity_x += self.wind_effect * 0.1
        # Slow down over time
        self.velocity_x *= self.wind_resistance  
        
        # Update position
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Rotation
        self.rotation += self.rotation_speed
        
        # Increment time for wind calculations
        self.time += 0.1
        
        # Reset leaf to top if it falls off screen
        if self.y > HEIGHT + 20:
            self.reset()
        # Also reset if leaf goes too far left or right
        if self.x < -20 or self.x > WIDTH + 20:
            self.reset()
    
    def reset(self):
        # Reset leaf to top with new random properties
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-50, -10)
        self.velocity_y = random.uniform(0.5, 2.0)
        self.velocity_x = random.uniform(-0.5, 0.5)
        self.color = random.choice(LEAF_COLORS)
        self.time = 0
    
    def draw(self, surface):
        # Create a surface for the leaf
        leaf_surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        
        # Draw different leaf shapes
        if self.shape == 0:
            # Simple oval leaf
            pygame.draw.ellipse(leaf_surface, self.color, 
                               (0, 0, self.size * 2, self.size))
        elif self.shape == 1:
            # Pointy leaf shape
            points = [
                (self.size, 0),
                (self.size * 2, self.size // 2),
                (self.size, self.size),
                (0, self.size // 2)
            ]
            pygame.draw.polygon(leaf_surface, self.color, points)
        else:
            # Maple-like leaf
            center = (self.size, self.size // 2)
            pygame.draw.circle(leaf_surface, self.color, center, self.size // 2)
            pygame.draw.ellipse(leaf_surface, self.color, 
                               (self.size // 2, 0, self.size, self.size // 2))
        
        # Rotate the leaf surface
        rotated_leaf = pygame.transform.rotate(leaf_surface, self.rotation)
        
        # Get the rect of the rotated leaf and set its center
        leaf_rect = rotated_leaf.get_rect(center=(self.x, self.y))
        
        # Draw the rotated leaf
        surface.blit(rotated_leaf, leaf_rect)

# Draw the ground at the bottom of the scree
def draw_ground(surface):
    pygame.draw.rect(surface, GROUND_BROWN, (0, HEIGHT - 50, WIDTH, 50))

def main():
    clock = pygame.time.Clock()
    running = True
    
    # Create a list of leaves
    leaves = [Leaf() for _ in range(50)]
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        # Fill the background with sky blue
        screen.fill(SKY_BLUE)
        
        # Draw the ground
        draw_ground(screen)
        
        # Update and draw all leaves
        for leaf in leaves:
            leaf.update()
            leaf.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()