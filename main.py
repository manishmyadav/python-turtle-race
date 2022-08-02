from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.title("Welcome To The Great Turtle Race!")
screen.setup(width=500, height=400)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

user_bet = ''
while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?")

all_turtles = []
y_positions = [-70, -40, -10, 20, 50, 80]

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)
    all_turtles[i].goto(x=-230, y=y_positions[i])

is_race_on = True
screen.title("The Race is ON!")
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.title(f"Congrats! Your {winning_color} turtle won.")
                print(f"Your {winning_color} turtle won!")
            else:
                screen.title(f"The {winning_color} turtle won!")
                print(f"Your 've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()