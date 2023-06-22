from turtle import Turtle, Screen
import random

turtle=Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turtle.shape('turtle')
move=[30, -30]
angle=[90,-90]

turtle.width(10)
for i in range(100):
    turtle.forward(random.choice(move))
    turtle.color(random.choice(colors))
    turtle.right(random.choice(angle))

screen=Screen()
screen.exitonclick()
