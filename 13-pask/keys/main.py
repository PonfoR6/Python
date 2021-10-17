from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def fwd():
    tim.forward(100)

def bck():
    tim.backward(100)

def left():
    new_heading = tim.heading() + 90
    tim.setheading(new_heading)

def right():
    new_heading = tim.heading() - 90
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fwd, "w")
screen.onkey(bck, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")



screen.exitonclick()