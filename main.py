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
turtle.width(0)
angle_change_by=5
#draw spirograph
for i in range(int(360/angle_change_by)):
    turtle.circle(200)
    turtle.right(angle_change_by)


#spirograph drawing ends
screen=Screen()
screen.exitonclick()
