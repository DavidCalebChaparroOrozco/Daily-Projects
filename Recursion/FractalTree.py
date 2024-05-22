# Importing necessary libraries
import turtle

def draw_tree(branch_length, angle, recursion_factor):
    # Base condition to stop recursion
    if branch_length > 5:  
        turtle.forward(branch_length)
        turtle.right(angle)
        
        # Recursive call to draw the right sub-branch
        draw_tree(branch_length - recursion_factor, angle, recursion_factor)
        
        turtle.left(2 * angle)
        
        # Recursive call to draw the left sub-branch
        draw_tree(branch_length - recursion_factor, angle, recursion_factor)
        
        turtle.right(angle)
        turtle.backward(branch_length)

def main():
    # Setup the drawing window
    window = turtle.Screen()
    window.bgcolor("white")

    # Setup the turtle
    turtle.left(90)  # Point the turtle upwards
    turtle.up()      # Lift the pen
    turtle.backward(100)  # Move the turtle to a starting position
    turtle.down()    # Lower the pen
    turtle.color("green")  # Set the color of the turtle's pen

    # Tree parameters
    initial_length = 100
    division_angle = 30
    recursion_decrement = 15

    # Initial call to draw the tree
    draw_tree(initial_length, division_angle, recursion_decrement)

    # Keep the window open
    turtle.done()

if __name__ == "__main__":
    main()
