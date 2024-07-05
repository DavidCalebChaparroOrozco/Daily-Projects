# Importing necessary libraries
import turtle
import random

def setup():
    global length, height, scale, strange, solve
    length = 300    # Length of the maze
    height = 300    # Height of the maze
    scale = 15      # Scale factor for drawing
    strange = False # Option for strange behavior (not currently used)
    solve = True    # Option to solve the maze after generation

def grid_setup():
    global grid, visit, visited, heights, rows, total
    grid = []
    visit = []
    visited = []
    heights = height // scale   # Number of rows in the grid
    rows = length // scale      # Number of columns in the grid
    total = rows * heights      # Total number of cells in the grid
    for counter in range(total):
        grid.append(counter)
        visit.append(0)
        visited.append(0)

def NESW(current):
    # Determine possible moves (North, East, South, West)
    cords = [current + rows, current + 1, current - rows, current - 1]
    stats = []
    for i in cords:
        # Check if the move is out of bounds or crosses a wall
        if i >= total or i < 0 or (i // rows != current // rows and i % rows != current % rows):
            stats.append(3)
        else:
            stats.append(visit[i])
    
    # Choose the next cell based on the least visited neighbors
    if visit[current] <= min(stats):
        return visited[current]
    
    min_stats_indices = [i for i, v in enumerate(stats) if v == min(stats)]
    choice = random.choice(min_stats_indices)
    
    # Optional strange behavior condition (not currently used)
    if strange and len(min_stats_indices) in [1, 3]:
        return visited[current]
    
    selected_index = random.choice(min_stats_indices)
    selected_cord = cords[selected_index]
    visit[selected_cord] += 1
    visited[selected_cord] = current
    return selected_cord

def tset():
    global t, wn
    wn = turtle.Screen()
    wn.bgcolor("grey")
    t = turtle.Turtle()
    t.ht()
    t.speed(0)
    t.pensize(scale - (scale * 0.2))
    t.color("white")
    t.up()
    t.goto((-.5 * rows) * scale, (-.5 * heights) * scale)
    t.pendown()

def generate(current):
    # Recursive function to generate the maze
    if min(visit) == 1:
        return
    next_cell = NESW(current)
    t.goto(((next_cell % rows) - .5 * rows) * scale, ((next_cell // rows) - .5 * heights) * scale)
    generate(next_cell)

def solver(path):
    # Recursive function to solve the maze
    if path == 0:
        return
    next_path = visited[path]
    t.goto(((next_path % rows) - .5 * rows) * scale, ((next_path // rows) - .5 * heights) * scale)
    solver(next_path)

def StartStop():
    # Draw start and end points of the maze
    global path
    t.pensize(scale * 0.6)
    t.up()
    t.goto((-.5 * rows) * scale, (-.5 * heights) * scale)
    t.down()
    t.seth(180)
    t.color("green")   # Start point color
    t.forward(scale)
    t.up()
    path = grid[total - 1]
    t.goto(((path % rows) - .5 * rows) * scale, ((path // rows) - .5 * heights) * scale)
    t.down()
    t.color("red")    # End point color
    t.seth(0)
    t.forward(scale)
    t.up()
    t.backward(scale)

def main():
    # Main function to initialize and run the maze generator
    setup()
    grid_setup()
    tset()
    visit[0] = 1
    generate(0)
    StartStop()
    if solve:
        t.down()
        t.color("blue")   # Path color for solving
        solver(grid[total - 1])
    wn.exitonclick()

# Start the maze generator
main()