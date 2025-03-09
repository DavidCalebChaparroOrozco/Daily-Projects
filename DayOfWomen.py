# Importing necessary libraries
import turtle

# Function to draw a petal
def draw_petal(t, radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

# Function to draw a rose with multiple petals
def draw_rose():
    t = turtle.Turtle()
    t.speed(10)
    t.color("red")
    t.width(3)
    
    t.penup()
    t.goto(0, -100)
    t.pendown()
    
    for _ in range(6):
        draw_petal(t, 100, 60)
        t.left(60)
    
    t.hideturtle()

# Function to draw the stem and leaves
def draw_stem():
    t = turtle.Turtle()
    t.speed(10)
    t.color("green")
    t.width(4)
    
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.goto(0, -250)  # Draw the stem
    
    # Draw left leaf
    t.penup()
    t.goto(0, -180)
    t.pendown()
    t.begin_fill()
    t.circle(20, 90)
    t.goto(0, -180)
    t.end_fill()
    
    # Draw right leaf
    t.penup()
    t.goto(0, -220)
    t.pendown()
    t.begin_fill()
    t.circle(-20, 90)
    t.goto(0, -220)
    t.end_fill()
    
    t.hideturtle()

# Function to display the message
def draw_message():
    t = turtle.Turtle()
    t.speed(0)
    t.color("black")  # Changed to black for better visibility
    t.penup()
    t.goto(-200, 150)
    t.write("The best curve of a woman is her smile.", font=("Arial", 16, "bold"))
    t.hideturtle()

# Main function to draw everything
def main():
    turtle.bgcolor("lightpink")  # Set background color
    draw_stem()
    draw_rose()
    draw_message()
    turtle.done()

if __name__ == "__main__":
    main()