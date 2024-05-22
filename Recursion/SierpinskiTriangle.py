# Importing necessary libraries
import turtle

# Function to draw a filled triangle using the given points and color
def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

# Function to get the midpoint between two points
def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Recursive function to draw the Sierpinski triangle
def sierpinski(points, degree, my_turtle):
    # Color map for different recursion depths
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    # Draw the main triangle
    draw_triangle(points, colormap[degree], my_turtle)
    # If we have not reached the base case, recurse
    if degree > 0:
        sierpinski([points[0], 
                    get_mid(points[0], points[1]), 
                    get_mid(points[0], points[2])],
                degree-1, my_turtle)
        sierpinski([points[1], 
                    get_mid(points[1], points[0]), 
                    get_mid(points[1], points[2])],
                degree-1, my_turtle)
        sierpinski([points[2], 
                    get_mid(points[2], points[0]), 
                    get_mid(points[2], points[1])],
                degree-1, my_turtle)

# Main function to set up the drawing environment and initiate the recursion
def main():
    my_turtle = turtle.Turtle()
    my_screen = turtle.Screen()
    # Define the vertices of the initial large triangle
    my_points = [[-200, -100], [0, 200], [200, -100]]
    # Start the recursion with a depth of 4
    sierpinski(my_points, 4, my_turtle)
    # Wait for user to close the window
    my_screen.exitonclick()

# Execute the main function
main()
