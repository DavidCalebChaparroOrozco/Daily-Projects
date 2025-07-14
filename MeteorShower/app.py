# Import necessary libraries
import tkinter as tk
import random

# Constants for window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Meteor properties
NUM_METEORS = 20
METEOR_SPEED_MIN = 5
METEOR_SPEED_MAX = 15
TAIL_LENGTH = 10

# Star properties
NUM_STARS = 100
STAR_BLINK_PROBABILITY = 0.05

class Star:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.randint(0, WINDOW_WIDTH)
        self.y = random.randint(0, WINDOW_HEIGHT)
        self.size = random.randint(1, 3)
        self.visible = True

    def blink(self):
        # Randomly toggle visibility to simulate blinking
        if random.random() < STAR_BLINK_PROBABILITY:
            self.visible = not self.visible

    def draw(self):
        if self.visible:
            self.canvas.create_oval(
                self.x - self.size, self.y - self.size,
                self.x + self.size, self.y + self.size,
                fill='white', outline=''
            )

class Meteor:
    def __init__(self, canvas):
        self.canvas = canvas
        self.reset()

    def reset(self):
        # Random starting position on the top of the canvas
        self.x = random.randint(0, WINDOW_WIDTH)
        self.y = random.randint(-WINDOW_HEIGHT, 0)
        # Random speed for the meteor
        self.speed = random.randint(METEOR_SPEED_MIN, METEOR_SPEED_MAX)
        # Random color between warm shades
        self.color = random.choice(['red', 'orange', 'yellow'])
        # Store previous positions for the tail effect
        self.trail = []

    def move(self):
        # Add current position to trail
        self.trail.append((self.x, self.y))
        if len(self.trail) > TAIL_LENGTH:
            self.trail.pop(0)

        # Move the meteor downward diagonally
        self.x += self.speed * 0.5
        self.y += self.speed

        # Reset meteor if it goes out of the window bounds
        if self.y > WINDOW_HEIGHT or self.x > WINDOW_WIDTH:
            self.reset()

    def draw(self):
        # Draw the trail with gradient effect (lighter colors as it fades)
        for i, (tx, ty) in enumerate(self.trail):
            intensity = int(255 * (i + 1) / len(self.trail))
            if self.color == 'red':
                color = f'#{intensity:02x}0000'
            elif self.color == 'orange':
                color = f'#{intensity:02x}{int(intensity*0.5):02x}00'
            else:  # yellow
                color = f'#{intensity:02x}{intensity:02x}00'

            self.canvas.create_line(tx, ty, tx+2, ty+2, fill=color, width=2)

        # Draw the meteor head
        self.canvas.create_oval(
            self.x - 2, self.y - 2,
            self.x + 2, self.y + 2,
            fill=self.color,
            outline=''
        )

class MeteorShowerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Meteor Shower Simulation')
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='black')
        self.canvas.pack()

        # Create a list of stars
        self.stars = [Star(self.canvas) for _ in range(NUM_STARS)]
        # Create a list of meteors
        self.meteors = [Meteor(self.canvas) for _ in range(NUM_METEORS)]

        # Start the animation
        self.animate()

    def animate(self):
        # Clear the canvas on each frame
        self.canvas.delete('all')

        # Draw and blink each star
        for star in self.stars:
            star.blink()
            star.draw()

        # Move and draw each meteor
        for meteor in self.meteors:
            meteor.move()
            meteor.draw()

        # Schedule the next frame
        self.root.after(50, self.animate)

if __name__ == '__main__':
    root = tk.Tk()
    app = MeteorShowerApp(root)
    root.mainloop()
