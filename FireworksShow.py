# Import necessary libraries
import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🎆 Fireworks Show by David Caleb")
screen.setup(width=800, height=600)
# Turn off automatic screen updates
screen.tracer(0)  

# Create a turtle for drawing fireworks
firework = turtle.Turtle()
firework.hideturtle()
firework.speed(0)

# List of bright colors
colors = ["red", "yellow", "blue", "green", "magenta", "cyan", "white", "orange", "violet"]

# Draws a single firework explosion at (x, y)
def draw_firework(x, y):
    firework.penup()
    firework.goto(x, y)
    firework.pendown()

    # Choose random color and number of sparks
    color = random.choice(colors)
    sparks = random.randint(10, 20)
    firework.pensize(2)
    firework.pencolor(color)

    for _ in range(sparks):
        angle = random.randint(0, 360)
        length = random.randint(20, 80)

        firework.penup()
        firework.goto(x, y)
        firework.setheading(angle)
        firework.pendown()
        firework.forward(length)

    screen.update()
    time.sleep(0.2)

    # Clear the drawing after a short delay to simulate fading
    firework.clear()

# Launch multiple fireworks with random positions
def launch_fireworks(count=20):
    for _ in range(count):
        x = random.randint(-380, 380)
        y = random.randint(0, 250)
        draw_firework(x, y)
        time.sleep(0.3)

# Run the fireworks show
launch_fireworks()

# Exit when clicked
screen.exitonclick()
