# Importing necessary libraries
import turtle
import random

# Set up the window
window = turtle.Screen()
window.title("Christmas Tree Generator by David Caleb")

# Create the turtle for drawing the tree
tree_maker = turtle.Turtle()
tree_maker.color("darkgreen")

# Draw outline of tree
tree_maker.begin_fill()
tree_points = [[0, 400], [-200, 300], [-100, 300], [-300, 200], [-100, 200], [-400, 0], [400, 0], [100, 200], [300, 200], [100, 300], [200, 300], [0, 400]]

for tree_edge in tree_points:
    tree_maker.goto(tree_edge)
tree_maker.end_fill()

# Draw trunk of tree
tree_maker.penup()
tree_maker.color("saddlebrown")
tree_maker.goto(100, 0)
tree_maker.pendown()

tree_maker.begin_fill()
trunk_points = [[100, 0], [-100, 0], [-100, -100], [100, -100], [100, 0]]
for each in trunk_points:
    tree_maker.goto(each)
tree_maker.end_fill()

# Function to draw ornaments
def draw_ornament(x, y):
    tree_maker.penup()
    tree_maker.goto(x, y)
    tree_maker.pendown()
    
    # Choose a random color for the ornament
    colors = ["red", "blue", "gold", "silver", "purple"]
    tree_maker.color(random.choice(colors))
    
    # Draw a circle for the ornament
    tree_maker.begin_fill()
    tree_maker.circle(15)  
    tree_maker.end_fill()

# Add ornaments to the tree at various positions
ornament_positions = [
    (-150, 250), (-50, 250), (50, 230), (150, 230),
    (-175, 175), (-75, 175), (75, 150), (175, 150),
    (-125, 100), (125, 100), (0, 50)
]

for pos in ornament_positions:
    draw_ornament(pos[0], pos[1])

# Draw a star on top of the tree
def draw_star(x, y):
    tree_maker.penup()
    tree_maker.goto(x, y)
    tree_maker.setheading(90)
    tree_maker.pendown()
    
    # Star color and size
    tree_maker.color("gold")
    size = 20
    
    # Draw the star shape
    for _ in range(5):
        tree_maker.forward(size)
        tree_maker.right(144)  

# Draw the star at the top of the tree
draw_star(0, 400)

# Write a festive message
tree_maker.penup()        
tree_maker.goto(0, -200) 
tree_maker.setheading(0) 
tree_maker.color("red")
tree_maker.pendown()       

tree_maker.write("Happy Holidays!", align="center", font=("Arial", 42, "normal"))
tree_maker.penup()         
tree_maker.goto(0, -250)   
tree_maker.pendown()       

tree_maker.write("I wish you a happy holiday and a prosperous new year.", align="center", font=("Arial", 18, "normal"))

# Hide turtle and finish up
tree_maker.hideturtle()

# Keep the window open
window.mainloop()
