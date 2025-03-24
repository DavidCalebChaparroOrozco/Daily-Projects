# Import necessary libraries
import turtle

# L-System 3D Implementation
# This program generates 3D graphics using recursive rules of L-Systems.
# Applies the L-System rules to the axiom for a given number of iterations.
def apply_rules(axiom, rules, iterations):
    for _ in range(iterations):
        new_axiom = ""
        for char in axiom:
            # Replace characters based on rules
            new_axiom += rules.get(char, char)  
        axiom = new_axiom
    return axiom

# Draws the L-System using the turtle graphics library.
def draw_lsystem(turtle, instructions, angle, distance):
    # Stack to save the turtle's state for branching
    stack = []  
    for command in instructions:
        if command == "F":
            # Move forward
            turtle.forward(distance)  
        elif command == "+":
            # Turn right
            turtle.right(angle)  
        elif command == "-":
            # Turn left
            turtle.left(angle)  
        elif command == "[":
            # Save state
            stack.append((turtle.position(), turtle.heading()))  
        elif command == "]":
            # Restore state
            position, heading = stack.pop()  
            turtle.penup()
            turtle.goto(position)
            turtle.setheading(heading)
            turtle.pendown()

# Main function to run the L-System
def main():
    # Define the axiom and rules for the L-System
    axiom = "F"
    rules = {
        # Example rule for a 3D structure
        "F": "FF+[+F-F-F]-[-F+F+F]"  
    }
    # Number of iterations
    iterations = 4  
    # Turning angle in degrees
    angle = 25  
    # Distance to move forward
    distance = 10  

    # Generate the L-System string
    lsystem_string = apply_rules(axiom, rules, iterations)

    # Set up the turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    t = turtle.Turtle()
    # Fastest drawing speed
    t.speed(0)  
    t.penup()
    # Start position
    t.goto(0, -300)  
    # Initial orientation
    t.setheading(90)  
    t.pendown()

    # Draw the L-System
    draw_lsystem(t, lsystem_string, angle, distance)

    # Finish
    t.hideturtle()
    screen.mainloop()

# Run the program
if __name__ == "__main__":
    main()