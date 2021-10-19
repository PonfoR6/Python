import colorgram
import turtle as t
import random

colors = colorgram.extract("image.jpg", 10)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

rgb_colors = rgb_colors[2:]

t.colormode(255)
tim = t.Turtle()
screen = t.Screen()

tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()
