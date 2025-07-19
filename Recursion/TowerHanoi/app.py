# Import necessary libraries
import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DISK_HEIGHT = 20
BASE_WIDTH = 20
BASE_HEIGHT = 150
POLE_WIDTH = 10
POLE_HEIGHT = 200
COLORS = {
    'background': (240, 240, 240),
    # Brown
    'base': (139, 69, 19),  
    # Lighter brown
    'pole': (160, 82, 45),   
    'disks': [
        # Red
        (255, 0, 0),    
        # Green
        (0, 255, 0),    
        # Blue
        (0, 0, 255),    
        # Yellow
        (255, 255, 0),  
        # Purple
        (255, 0, 255),  
        # Cyan
        (0, 255, 255),  
        # Orange
        (255, 128, 0),  
    ]
}

class Disk:
    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.width = size * 30
        self.height = DISK_HEIGHT

class Tower:
    def __init__(self, x_pos):
        self.x_pos = x_pos
        self.disks = []
    
    def add_disk(self, disk):
        self.disks.append(disk)
    
    def remove_disk(self):
        if self.disks:
            return self.disks.pop()
        return None
    
    def get_top_disk(self):
        if self.disks:
            return self.disks[-1]
        return None

class HanoiGame:
    def __init__(self, difficulty=3):
        # Number of disks
        self.difficulty = difficulty  
        self.towers = [Tower(200), Tower(400), Tower(600)]
        self.selected_tower = None
        self.moves = 0
        self.setup_game()
        
    def setup_game(self):
        # Clear all towers
        for tower in self.towers:
            tower.disks = []
        
        # Add disks to first tower
        for i in range(self.difficulty, 0, -1):
            color_index = (i - 1) % len(COLORS['disks'])
            self.towers[0].add_disk(Disk(i, COLORS['disks'][color_index]))
        
        self.moves = 0
    
    def select_tower(self, tower_index):
        if self.selected_tower is None:
            # Select a tower if it has disks
            if self.towers[tower_index].disks:
                self.selected_tower = tower_index
        else:
            # Try to move disk from selected tower to clicked tower
            self.move_disk(self.selected_tower, tower_index)
            self.selected_tower = None
    
    def move_disk(self, from_idx, to_idx):
        from_tower = self.towers[from_idx]
        to_tower = self.towers[to_idx]
        
        if not from_tower.disks:
            return False
        
        disk_to_move = from_tower.get_top_disk()
        top_disk_to = to_tower.get_top_disk()
        
        # Check if move is valid
        if top_disk_to is None or disk_to_move.size < top_disk_to.size:
            disk = from_tower.remove_disk()
            to_tower.add_disk(disk)
            self.moves += 1
            return True
        
        return False
    
    # Game is over when all disks are on the last tower
    def is_game_over(self):
        return len(self.towers[-1].disks) == self.difficulty
    
    # Draw background
    def draw(self, screen):
        screen.fill(COLORS['background'])
        
        # Draw bases
        for tower in self.towers:
            pygame.draw.rect(screen, COLORS['base'], 
                            (tower.x_pos - BASE_WIDTH//2, SCREEN_HEIGHT - BASE_HEIGHT, 
                                BASE_WIDTH, BASE_HEIGHT))
        
        # Draw poles
        for tower in self.towers:
            pygame.draw.rect(screen, COLORS['pole'], 
                            (tower.x_pos - POLE_WIDTH//2, SCREEN_HEIGHT - BASE_HEIGHT - POLE_HEIGHT, 
                                POLE_WIDTH, POLE_HEIGHT))
        
        # Draw disks
        for i, tower in enumerate(self.towers):
            for j, disk in enumerate(tower.disks):
                y_pos = SCREEN_HEIGHT - BASE_HEIGHT - (j + 1) * DISK_HEIGHT
                pygame.draw.rect(screen, disk.color, 
                                (tower.x_pos - disk.width//2, y_pos, 
                                    disk.width, disk.height))
        
        # Highlight selected tower
        if self.selected_tower is not None:
            pygame.draw.rect(screen, (0, 255, 0), 
                            (self.towers[self.selected_tower].x_pos - 50, 50, 
                                100, 30), 2)
        
        # Display moves and difficulty
        font = pygame.font.SysFont(None, 36)
        moves_text = font.render(f"Moves: {self.moves}", True, (0, 0, 0))
        difficulty_text = font.render(f"Disks: {self.difficulty}", True, (0, 0, 0))
        screen.blit(moves_text, (20, 20))
        screen.blit(difficulty_text, (20, 60))
        
        # Display game over message
        if self.is_game_over():
            game_over_font = pygame.font.SysFont(None, 72)
            game_over_text = game_over_font.render("You Win!", True, (0, 128, 0))
            screen.blit(game_over_text, 
                        (SCREEN_WIDTH//2 - game_over_text.get_width()//2, 
                        SCREEN_HEIGHT//2 - game_over_text.get_height()//2))

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Towers of Hanoi")
    
    clock = pygame.time.Clock()
    game = HanoiGame(difficulty=3)
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check which tower was clicked
                x, y = pygame.mouse.get_pos()
                for i, tower in enumerate(game.towers):
                    if tower.x_pos - 50 <= x <= tower.x_pos + 50:
                        game.select_tower(i)
                        break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game = HanoiGame(difficulty=3)
                elif event.key == pygame.K_2:
                    game = HanoiGame(difficulty=4)
                elif event.key == pygame.K_3:
                    game = HanoiGame(difficulty=5)
                elif event.key == pygame.K_r:
                    game.setup_game()
        
        # Draw everything
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()