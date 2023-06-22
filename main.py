import turtle as t
import colorgram
from turtle import Screen
import random

# write random color function code
def random_color():
    return random.randint(0,255)

turtle=t.Turtle()
t.colormode(255)
turtle.shape('turtle')
#move=[30, -30]
#angle=[0,90,180,270]
#
#turtle.speed("fastest")
#turtle.width(3)
#angle_change_by=5
#draw hirst painting
#get colors
rgb_colors=[]
colors=colorgram.extract('image.jpg', 30)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    if (r<240 or g<240 or b<240):
        rgb_colors.append((r,g,b))
#start drawing hirst painting
turtle.penup()
turtle.setheading(230)
turtle.forward(400)
turtle.setheading(0)
for i in range(15):
    for j in range(10):
        turtle.color(random.choice(rgb_colors))
        turtle.pendown()
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)
    turtle.backward(8*50+10*20//2)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)

#hirst painting ends
print("done")
screen=Screen()
screen.exitonclick()
