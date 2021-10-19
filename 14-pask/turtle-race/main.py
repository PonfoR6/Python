import random
import turtle
from turtle import Turtle, Screen

#
# screen = turtle.Screen()
# win_length = 500
# win_height = 500
#
# turtles = 8
#
# screen.setup(500, 500)
#
#
# class TurtleR(object):
#     def __init__(self, color, pos):
#         self.pos = pos
#         self.color = color
#         self.tim = turtle.Turtle()
#         self.tim.shape('turtle')
#         self.tim.color(color)
#         self.tim.penup()
#         self.tim.setpos(pos)
#         self.tim.setheading(90)
#
#     def move(self):
#         r = random.randrange(1, 20)
#         self.pos = (self.pos[0], self.pos[1] + r)
#         self.tim.pendown()
#         self.tim.forward(r)
#
#
# def startRace():
#     t_list = []
#     turtle.clearscreen()
#     turtle.hideturtle()
#     colors = ["red", "green", "blue", 'yellow', 'pink', 'orange', 'purple', 'black', 'grey']
#     start = -(win_length / 2) + 20
#     for t in range(turtles):
#         new_pos_x = start + t * win_length // turtles
#         t_list.append(TurtleR(colors[t], (new_pos_x, -230)))
#         t_list[t].tim.showturtle()
#
#     run = True
#     while run:
#         for t in t_list:
#             t.move()
#
#         maxColor = []
#         maxDis = 0
#         for t in t_list:
#             if t.pos[1] > 230 and t.pos[1] > maxDis:
#                 maxDis = t.pos[1]
#                 maxColor = []
#                 maxColor.append(t.color)
#             elif t.pos[1] > 230 and t.pos[1] == maxDis:
#                 maxDis = t.pos[1]
#                 maxColor.append(t.color)
#
#         if len(maxColor) > 0:
#             run = False
#             print('The winner is: ')
#             for win in maxColor:
#                 print(win)
#
# startRace()
# screen.exitonclick()

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="bet", prompt="Which turtle will win the race?")
print(user_bet)
confirm_bet = screen.textinput(title="Are you sure?", prompt="Are you sure this is the color you want to bet on?")
if confirm_bet == "no":
    user_bet = screen.textinput(title="bet", prompt="Which turtle will win the race?")
colors = ["red", "green", "orange", "black", "purple", "blue", "yellow"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            turtle.write(f'{winning_color} has won the race!', font=("Arial", 12, "bold"))
            if winning_color == user_bet:
                print(f"You've won! {winning_color} won the race!")
            else:
                print(f"You've lost, {winning_color} won the race!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
