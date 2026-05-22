import turtle as t
import random

screen = t.Screen()
screen.setup(700,500)

bet = screen.textinput('Want to give a try ?', 'Make a bet, choose a color: ').lower()

race_on = False


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-125, -75, -25, 25, 75, 125]
all_turtles = []

for turtle_i in range(0, 6):
    new_turtle = t.Turtle('turtle')
    new_turtle.speed(3)
    new_turtle.color(colors[turtle_i])
    new_turtle.penup()
    new_turtle.goto(-300, y_position[turtle_i])
    all_turtles.append(new_turtle)

if bet:
    race_on = True

while race_on:

    for new_t in all_turtles:

        if new_t.xcor() > 320:
            race_on = False
            winning_color = new_t.pencolor()
            if winning_color == bet:
                print(f'You have won. The {winning_color} turtle is the winner.')
            else:
                print(f'You have lost. The {winning_color} turtle is the winner.')

        distance = random.randint(0, 10)
        new_t.forward(distance)


screen.exitonclick()