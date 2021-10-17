import turtle
from turtle import *
from random import randint

tim = turtle.Turtle()
screen = turtle.Screen()

turtle.colormode(255)

tim.shape("turtle")
# tim.color("green")

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

def draw_square(size):
    for _ in range(4):
        tim.forward(size)
        tim.left(90)

def b():
    Turtle().back(45)

def f():
    Turtle().forward(45)

def l():
    Turtle().left(45)
def r():
    Turtle().right(45)


# def draw_dash(dash_size, dashes):
#     for i in range(dashes):
#         tim.forward(dash_size)
#         tim.penup()
#         tim.forward(dash_size)
#         tim.pendown()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

def draw_spirograph(radius, size_of_gap):
    tim.speed("fastest")
    for angle in range(int(360 / size_of_gap)):
        tim.circle(radius)
        tim.setheading(tim.heading() + size_of_gap)


tim.color(random_color())
# draw_square(200)
# draw_dash(1, 5000000)
# draw_shape(685)
# draw_spirograph(100, 1)
# tim.clear()
screen.exitonclick()

onkey(f, "Up")
onkey(b, "Down")
onkey(l, "Left")
onkey(r, "Right")

listen()