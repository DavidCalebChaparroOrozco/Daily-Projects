import turtle
import random  # Importing random to place toppings randomly

def draw_pizza():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Pizza in Turtle")
    screen.bgcolor("white")

    # Create a turtle
    pizza = turtle.Turtle()
    pizza.speed(3)

    # Draw the pizza base (circle)
    pizza.penup()
    # Move down to center the pizza
    pizza.goto(0, -100)  
    pizza.pendown()
    # Color of the crust
    pizza.color("goldenrod")  
    pizza.begin_fill()
    pizza.circle(100) 
    pizza.end_fill()

    # Add sauce (inner circle)
    pizza.penup()
    pizza.goto(0, -80) 
    pizza.pendown()
    pizza.color("red") 
    pizza.begin_fill()
    pizza.circle(80) 
    pizza.end_fill()

    # Add pepperoni (red circles)
    pizza.penup()
    
    for _ in range(6):
        x = random.randint(-60, 60)
        y = random.randint(-60, 60)
        if (x**2 + y**2) <= (80**2):  
            pizza.goto(x, y)
            pizza.pendown()
            pizza.color("darkred")
            pizza.begin_fill()
            pizza.circle(10)
            pizza.end_fill()
            pizza.penup()

    # Add mushrooms (gray circles)
    for _ in range(4):
        x = random.randint(-60, 60)
        y = random.randint(-60, 60)
        if (x**2 + y**2) <= (80**2): 
            pizza.goto(x, y)
            pizza.pendown()
            pizza.color("gray")
            pizza.begin_fill()
            pizza.circle(5)  
            pizza.end_fill()
            pizza.penup()

    # Finish up
    pizza.hideturtle()  
    turtle.done()  

# Call the function to draw the pizza
draw_pizza()
