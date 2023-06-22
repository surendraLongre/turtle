import turtle as t
from turtle import Screen
import random

# write random color function code
def random_color():
    return random.randint(0,255)

turtle=t.Turtle()
t.colormode(255)
turtle.shape('turtle')
move=[30, -30]
angle=[0,90,180,270]

turtle.speed("fastest")
turtle.width(10)
for i in range(200):
    turtle.color((random_color(),random_color(),random_color()))
    turtle.forward(random.choice(move))
    turtle.setheading(random.choice(angle))

screen=Screen()
screen.exitonclick()
