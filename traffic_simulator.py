import turtle
import time
import random

# ================= SCREEN =================
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)   # Full screen
screen.bgcolor("#5d7ea3")             # Rainy sky
screen.title("Rainy Traffic Highway Scene")
screen.tracer(0)

# ================= DRAWER =================
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Screen size helpers
W = screen.window_width() // 2
H = screen.window_height() // 2

# ================= BASIC FUNCTIONS =================
def rect(x, y, w, h, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def circle_fill(x, y, r, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# ================= BACKGROUND =================
def mountain(x, y, s):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#6b4f3a")
    t.begin_fill()
    t.goto(x+s, y+s)
    t.goto(x+2*s, y)
    t.goto(x, y)
    t.end_fill()

def tree(x, y):
    rect(x, y, 16, 45, "#4a2f17")
    circle_fill(x-8, y+35, 18, "darkgreen")
    circle_fill(x+12, y+42, 18, "green")
    circle_fill(x+2, y+55, 18, "limegreen")

def road(y):
    rect(-W, y, W*2, 90, "#333333")

    # center divider line
    t.penup()
    t.goto(-W, y+42)
    t.color("white")
    t.width(3)
    t.setheading(0)

    for _ in range(40):
        t.pendown()
        t.forward(30)
        t.penup()
        t.forward(25)

# ================= STATIC DRAW =================
# Sun
circle_fill(W-150, H-150, 55, "yellow")

# Mountains
for x in range(-W, W, 220):
    mountain(x, 70, 110)

# Grass
rect(-W, -20, W*2, 120, "#2fa82f")

# Trees
for x in range(-W+50, W, 180):
    tree(x, 20)

# Roads
road(-260)
road(-120)

# ================= BIRDS =================
birds = []

def make_bird():
    b = turtle.Turtle()
    b.hideturtle()
    b.penup()
    b.color("black")
    b.speed(0)
    return b

for i in range(6):
    birds.append([make_bird(), random.randint(-W, W), random.randint(150, H-80), random.randint(2,5)])

# ================= CAR CREATION =================
def make_car(color):
    c = turtle.Turtle()
    c.penup()
    c.shape("square")
    c.color(color)
    c.shapesize(stretch_wid=1.4, stretch_len=2.8)
    return c

def make_wheel():
    w = turtle.Turtle()
    w.penup()
    w.shape("circle")
    w.color("black")
    w.shapesize(0.6,0.6)
    return w

cars = []

# Lower road -> moving right
colors1 = ["gold", "red", "cyan", "orange", "purple"]
x = -W
for i in range(5):
    body = make_car(colors1[i])
    w1 = make_wheel()
    w2 = make_wheel()
    cars.append([body,w1,w2,x,-235,4])
    x -= 220

# Upper road -> moving left
colors2 = ["white", "blue", "pink", "yellow", "green", "silver"]
x = W
for i in range(6):
    body = make_car(colors2[i])
    w1 = make_wheel()
    w2 = make_wheel()
    cars.append([body,w1,w2,x,-95,-5])
    x += 180

# ================= RAIN DROPS =================
drops = []
for _ in range(140):
    d = turtle.Turtle()
    d.hideturtle()
    d.penup()
    d.color("lightblue")
    d.speed(0)
    drops.append([d, random.randint(-W, W), random.randint(-H, H)])

# ================= MAIN LOOP =================
while True:

    # Move Cars
    for c in cars:
        body,w1,w2,x,y,speed = c

        x += speed

        if speed > 0 and x > W+80:
            x = -W-150
        elif speed < 0 and x < -W-80:
            x = W+150

        body.goto(x,y)
        w1.goto(x-24,y-22)
        w2.goto(x+24,y-22)

        w1.setheading(w1.heading()+18)
        w2.setheading(w2.heading()+18)

        c[3] = x

    # Rain Animation
    for d in drops:
        pen,x,y = d
        pen.clear()
        pen.goto(x,y)
        pen.pendown()
        pen.setheading(-110)
        pen.forward(12)
        pen.penup()

        y -= 18
        x -= 3

        if y < -H:
            y = H
            x = random.randint(-W, W)

        d[1] = x
        d[2] = y

    # Flying Birds
    for b in birds:
        pen,x,y,speed = b
        pen.clear()
        pen.goto(x,y)
        pen.pendown()
        pen.setheading(60)
        pen.circle(10,120)
        pen.penup()
        pen.goto(x+16,y)
        pen.pendown()
        pen.setheading(120)
        pen.circle(10,120)
        pen.penup()

        x += speed
        if x > W+50:
            x = -W-50

        b[1] = x

    screen.update()
    time.sleep(0.03)
