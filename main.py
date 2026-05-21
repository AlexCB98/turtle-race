import turtle as t

tim = t.Turtle()
screen = t.Screen()
screen.setup(700,700)
bet = screen.textinput('Want to give a try ?', 'Make a bet, choose a color: ')

def red_turtle():
    tim = t.Turtle('turtle')
    tim.color('red')
    tim.penup()
    tim.goto(-300, -200)

red_turtle()






screen.exitonclick()