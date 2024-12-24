# Importing necessary libraries
import pygame
import random
import ctypes
import sys

# Initialize Pygame
pygame.init()

# Get the dimensions of the user's screen
user32 = ctypes.windll.user32
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Set window flags to create a borderless window
flags = pygame.NOFRAME
screen = pygame.display.set_mode((width, height), flags)
pygame.display.set_caption("Snowfall by David Caleb")  

# Get the window handle and set it to be layered (for transparency)
hwnd = pygame.display.get_wm_info()["window"]
ctypes.windll.user32.SetWindowLongW(hwnd, -20, ctypes.windll.user32.GetWindowLongW(hwnd, -20) | 0x8000 | 0x20)
# Set transparency
ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, 0, 1)  

# Create a list of snowflakes with random positions and sizes
snowflakes = [{"x": random.randint(0, width),
               "y": random.randint(0, height),
               "size": random.randint(2, 5)} for _ in range(200)]

# Create a clock object to control the frame rate
clock = pygame.time.Clock()  

# Main loop to keep the program running
while True:
    for event in pygame.event.get():
        # Check for quit event
        if event.type == pygame.QUIT:  
            # Quit Pygame
            pygame.quit()  
            # Exit the program
            sys.exit()  

    # Update the position of each snowflake
    for snowflake in snowflakes:
        # Move snowflake downwards by a random amount
        snowflake["y"] += random.randint(1, 3)  
        # If snowflake goes off the bottom of the screen
        if snowflake["y"] > height:  
            # Reset its x position randomly
            snowflake["x"] = random.randint(0, width)  
            # Reset y position to the top of the screen
            snowflake["y"] = 0  

    # Clear the screen with a transparent background
    screen.fill((0, 0, 0, 0))  
    for snowflake in snowflakes:
        # Draw each snowflake as a white circle
        pygame.draw.circle(screen, (255, 255, 255), (snowflake["x"], snowflake["y"]), snowflake["size"])  
        

    # Update the display with the new frame
    pygame.display.flip()  
    # Limit the frame rate to 30 frames per second
    clock.tick(30)  
