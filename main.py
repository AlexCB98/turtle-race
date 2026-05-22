import turtle as t

screen = t.Screen()
screen.setup(700,500)
bet = screen.textinput('Want to give a try ?', 'Make a bet, choose a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-125, -75, -25, 25, 75, 125]

for turtle_i in range(0, 6):
    tim = t.Turtle('turtle')
    tim.color(colors[turtle_i])
    tim.penup()
    tim.goto(-300, y_position[turtle_i])








screen.exitonclick()