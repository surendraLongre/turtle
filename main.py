import turtle as t
import colorgram
from turtle import Screen
import random

# write random color function code
def random_color():
    return random.randint(0,255)
def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.forward(-10)

def left_angle():
    turtle.left(10)

def right_angle():
    turtle.right(10)

def right_curve():
    right_angle()
    move_forward()

def left_curve():
    left_angle()
    move_backward()
def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


turtle=t.Turtle()
t.colormode(255)
turtle.shape('turtle')
screen=Screen()
#move=[30, -30]
#angle=[0,90,180,270]
#
#turtle.speed("fastest")
#turtle.width(3)
#angle_change_by=5
#add key listeners
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=left_angle)
screen.onkey(key="d", fun=right_angle)
screen.onkey(key="c", fun=clear)

print("done")
screen=Screen()
screen.exitonclick()
