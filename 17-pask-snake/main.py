import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("pink")
screen.setup(width=600, height=600)
screen.tracer(0)

tim = turtle.Turtle()
tim.shape("square")
tim.color("white")
tim.penup()
tim.goto(0, 0)
tim.direction = "Stop"

food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("Roboto", 24, "bold"))


def fwd():
    if tim.direction != "down":
        tim.direction = "up"


def back():
    if tim.direction != "up":
        tim.direction = "down"


def left():
    if tim.direction != "right":
        tim.direction = "left"


def right():
    if tim.direction != "left":
        tim.direction = "right"


def motion():
    if tim.direction == "up":
        y = tim.ycor()
        tim.sety(y + 20)
    if tim.direction == "down":
        y = tim.ycor()
        tim.sety(y - 20)
    if tim.direction == "left":
        x = tim.xcor()
        tim.setx(x - 20)
    if tim.direction == "right":
        x = tim.xcor()
        tim.setx(x + 20)


screen.listen()
screen.onkeypress(fwd, "w")
screen.onkeypress(back, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")

segments = []

while True:
    screen.update()
    if tim.xcor() > 290 or tim.xcor() < -290 or tim.ycor() > 290 or tim.ycor() < -290:
        time.sleep(1)
        tim.goto(0, 0)
        tim.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Roboto", 24, "bold"))
    if tim.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Roboto", 24, "bold"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = tim.xcor()
        y = tim.ycor()
        segments[0].goto(x, y)
    motion()
    for segment in segments:
        if segment.distance(tim) < 20:
            time.sleep(1)
            tim.goto(0, 0)
            tim.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("Roboto", 24, "bold"))
    time.sleep(delay)

screen.mainloop()
