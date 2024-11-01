# Importing necessary libraries
import turtle

# Set up the screen with a spooky background color
wn = turtle.Screen()
wn.title("Jack-o'-Lantern by David Caleb")
wn.bgcolor("black")

# Create a turtle object for drawing
t = turtle.Turtle()  
t.speed(8)  
# Hide the turtle icon for a cleaner look
t.hideturtle()  

# Function to draw a filled circle at specified coordinates
def drawcircle(x, y):
    t.color("orange")  
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.circle(70)
    t.end_fill()

# Draw two circles (eyes) with Halloween colors
drawcircle(20, 0)
drawcircle(-20, 0)

# Function to draw a triangle (pupil) at specified coordinates
def triangle(x, y):
    t.color("red")
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    for i in range(3):
        t.forward(40)
        t.left(360 / 3)
    t.end_fill()

# Draw pupils for the eyes
triangle(15, 80)
triangle(-55, 80)
triangle(-20, 50)

# Function to draw a spooky mouth
def mouth():
    t.color("yellow")
    t.up()
    t.goto(-60, 40)
    t.down()
    t.begin_fill()
    t.goto(-30, 20)
    t.goto(30, 20) 
    t.goto(60, 40) 
    t.goto(0, 30)  
    t.end_fill()

mouth()

# Function to draw a spooky stem (like a pumpkin stem)
def stem():
    t.color("darkgreen")
    t.up()
    t.goto(-40, 130)    
    t.down()
    t.begin_fill()
    t.goto(40, 130)     
    t.goto(20, 150)     
    t.goto(10, 170)     
    t.goto(0, 180)      
    t.goto(-15, 175)    
    t.goto(-10, 155)    
    t.goto(-15, 140)    
    t.goto(-40, 130)    
    t.end_fill()

stem()

# Function to display a Halloween message on screen
def display_message():
    message_turtle = turtle.Turtle()  
    message_turtle.color("white")
    message_turtle.penup()              
    message_turtle.hideturtle()         
    
    message_turtle.goto(0, -200)  
    
    message_turtle.write("Happy Halloween,\nOctober 31, 2024", align="center", font=("Trebuchet MS", 24, "bold"))

display_message()

# Keep window open until closed by user
turtle.done()