from turtle import Turtle, Screen
import random
import turtle

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make a bet", prompt="Who will win the race? Enter a color:")
print(user_bet)
colors = ["red", "green", "purple", "blue", "orange", "yellow"]
y_axis = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-240, y_axis[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You lose! The {winning_color} turtle is the winner")

screen.exitonclick()
