import turtle as t

screen = t.Screen()
screen.setup(700,700)
bet = screen.textinput('Want to give a try ?', 'Make a bet, choose a color: ')

def red_turtle():
    tim = t.Turtle('turtle')
    tim.color('red')
    tim.penup()
    tim.goto(-300, -100)

def orange_turtle():
    tim = t.Turtle('turtle')
    tim.color('orange')
    tim.penup()
    tim.goto(-300, -50)

def yellow_turtle():
    tim = t.Turtle('turtle')
    tim.color('yellow')
    tim.penup()
    tim.goto(-300, 0)

def green_turtle():
    tim = t.Turtle('turtle')
    tim.color('green')
    tim.penup()
    tim.goto(-300, 50)

def blue_turtle():
    tim = t.Turtle('turtle')
    tim.color('blue')
    tim.penup()
    tim.goto(-300, 100)

def purple_turtle():
    tim = t.Turtle('turtle')
    tim.color('purple')
    tim.penup()
    tim.goto(-300, 150)



red_turtle()
orange_turtle()
yellow_turtle()
green_turtle()
blue_turtle()
purple_turtle()






screen.exitonclick()