# Import necessary libraries
import turtle
import math
import time
import threading

# GLOBAL SETUP
screen = turtle.Screen()
screen.title("Realistic Cartoon Cat by David Caleb")
screen.setup(width=800, height=800)
day_color = "lightblue"
night_color = "#0c1445"
is_day = True
screen.bgcolor(day_color)

cat = turtle.Turtle()
cat.hideturtle()
cat.speed(0)

# Pupils as global turtles
left_pupil = turtle.Turtle()
right_pupil = turtle.Turtle()
for pupil in [left_pupil, right_pupil]:
    pupil.shape("circle")
    pupil.color("black")
    pupil.shapesize(0.6)
    pupil.penup()

# Laser pointer (red dot)
laser = turtle.Turtle()
laser.hideturtle()
laser.shape("circle")
laser.color("red")
laser.shapesize(0.3)
laser.penup()

# "Zzz..." sleeper turtle
sleeper = turtle.Turtle()
sleeper.hideturtle()
sleeper.penup()
sleeper.color("white")

# DRAWING HELPERS
def draw_circle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# DRAW CAT PARTS
def draw_head():
    draw_circle(cat, 0, 0, 100, "gray")

def draw_ears():
    # Lowered ear positions
    base_y = 60       
    tip_y = 160       
    inner_y = 90

    # Left ear
    cat.penup()
    cat.goto(-60, base_y)
    cat.fillcolor("gray")
    cat.begin_fill()
    cat.pendown()
    cat.goto(-100, tip_y)
    cat.goto(-30, inner_y)
    cat.goto(-60, base_y)
    cat.end_fill()

    # Right ear
    cat.penup()
    cat.goto(60, base_y)
    cat.begin_fill()
    cat.pendown()
    cat.goto(100, tip_y)
    cat.goto(30, inner_y)
    cat.goto(60, base_y)
    cat.end_fill()

def draw_body():
    cat.penup()
    # Adjusted upward to be fully visible
    cat.goto(0, -120)  
    cat.setheading(0)
    cat.color("gray")
    cat.begin_fill()
    cat.pendown()
    cat.circle(80)
    cat.end_fill()

def draw_eyes(opened=True):
    if opened:
        draw_circle(cat, -30, 40, 20, "white")
        draw_circle(cat, 30, 40, 20, "white")
        left_pupil.goto(-30, 40)
        right_pupil.goto(30, 40)
        left_pupil.showturtle()
        right_pupil.showturtle()
    else:
        left_pupil.hideturtle()
        right_pupil.hideturtle()
        cat.color("white")
        for x in [-30, 30]:
            cat.penup()
            cat.goto(x - 15, 40)
            cat.setheading(-60)
            cat.pendown()
            cat.circle(15, 120)

def draw_nose():
    cat.penup()
    cat.goto(-10, 15)
    cat.setheading(0)
    cat.color("pink")
    cat.begin_fill()
    cat.pendown()
    cat.goto(10, 15)
    cat.goto(0, 0)
    cat.goto(-10, 15)
    cat.end_fill()

def draw_mouth():
    cat.penup()
    cat.goto(0, 0)
    cat.setheading(-60)
    cat.pendown()
    cat.circle(15, 120)
    cat.penup()
    cat.goto(0, 0)
    cat.setheading(-120)
    cat.pendown()
    cat.circle(-15, 120)

def draw_whiskers():
    cat.pensize(2)
    cat.color("black")
    for y in [10, 0, -10]:
        cat.penup()
        cat.goto(-50, y)
        cat.setheading(180)
        cat.pendown()
        cat.forward(30)
        cat.penup()
        cat.goto(50, y)
        cat.setheading(0)
        cat.pendown()
        cat.forward(30)

# CAT DRAWER
def draw_cat(open_eyes=True):
    cat.clear()
    draw_body()
    draw_head()
    draw_ears()
    draw_eyes(opened=open_eyes)
    draw_nose()
    draw_mouth()
    draw_whiskers()

    # Show or animate "Zzz..." if it's night
    sleeper.clear()
    if not open_eyes:
        animate_zzz()

# ANIMATION OF "Zzz..."
def animate_zzz():
    def float_text():
        sleeper.goto(0, 160)
        sleeper.write("Zzz...", align="center", font=("Arial", 20, "italic"))
        for i in range(20):
            y = 160 + i * 2
            sleeper.clear()
            sleeper.goto(0, y)
            sleeper.write("Zzz...", align="center", font=("Arial", 20, "italic"))
            time.sleep(0.1)
        sleeper.clear()

    threading.Thread(target=float_text, daemon=True).start()

# EYE TRACKING
def follow_mouse(x, y):
    if not is_day:
        return
    def move_pupil(pupil, center_x, center_y):
        dx = x - center_x
        dy = y - center_y
        angle = math.atan2(dy, dx)
        dist = min(6, math.hypot(dx, dy))
        new_x = center_x + math.cos(angle) * dist
        new_y = center_y + math.sin(angle) * dist
        pupil.goto(new_x, new_y)

    move_pupil(left_pupil, -30, 40)
    move_pupil(right_pupil, 30, 40)
    laser.goto(x, y)
    laser.showturtle()

# TOGGLE BACKGROUND AND EYES
def toggle_day_night():
    global is_day
    is_day = not is_day
    screen.bgcolor(day_color if is_day else night_color)
    draw_cat(open_eyes=is_day)
    if not is_day:
        laser.hideturtle()

# BUTTON DRAWING
button = turtle.Turtle()
button.hideturtle()
button.penup()
button.speed(0)

def draw_toggle_button():
    button.clear()
    button.goto(0, 350)
    button.shape("square")
    button.color("white")
    button.shapesize(1.5, 10)
    button.stamp()
    button.goto(0, 340)
    label = "Switch to Night" if is_day else "Switch to Day"
    button.write(label, align="center", font=("Arial", 12, "bold"))

# EVENT HANDLER
def check_button(x, y):
    if -80 < x < 80 and 330 < y < 370:
        toggle_day_night()
        draw_toggle_button()
    else:
        follow_mouse(x, y)

# RUN PROGRAM
draw_cat(open_eyes=True)
draw_toggle_button()
screen.onscreenclick(check_button)
screen.mainloop()