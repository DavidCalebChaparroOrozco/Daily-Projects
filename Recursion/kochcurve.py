# Importing necessary libraries
import turtle

# Recursive function to draw the Koch Curve
# Draws the Koch Curve using recursion.
def koch_curve(length, level):
    """
    length: The length of the current segment.
    level: The depth of recursion (controls the complexity of the curve).
    """
    if level == 0:
        # Base case: draw a straight line
        turtle.forward(length)  
        return
    
    # Recursive case: Divide the line into 4 segments with turns

    # Divide the line length into thirds
    length /= 3.0  
    # Draw the first segment
    koch_curve(length, level - 1)  
    # Turn left 60 degrees
    turtle.left(60)  
    # Draw the second segment
    koch_curve(length, level - 1)  
    # Turn right 120 degrees
    turtle.right(120)  
    # Draw the third segment
    koch_curve(length, level - 1)  
    # Turn back 60 degrees
    turtle.left(60)  
    # Draw the last segment
    koch_curve(length, level - 1)  

# Function to draw a Koch Snowflake using the Koch Curve
def koch_snowflake(length, level):
    """
    Draws a Koch Snowflake using three Koch Curves.
    
    Parameters:
    length: The length of the sides of the snowflake.
    level: The depth of recursion (controls the complexity of the snowflake).
    """
    # The snowflake consists of three Koch Curves
    for _ in range(3):  
        koch_curve(length, level)
        # Turn right 120 degrees to form the next side
        turtle.right(120)  

# Setup the turtle environment
def setup_environment():
    """
    Sets up the turtle environment for drawing the Koch Snowflake.
    """
    # Set the drawing speed
    turtle.speed("fastest")  
    # Hide the turtle cursor
    turtle.hideturtle()      
    turtle.penup()
    # Move to a starting position
    turtle.goto(-200, 100)  
    turtle.pendown()

# Main execution
if __name__ == "__main__":
    setup_environment()
    
    # Draw the Koch Snowflake with a recursion depth of 4
    koch_snowflake(length=400, level=4)
    
    # Keep the window open after drawing
    turtle.done()  
