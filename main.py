from turtle import Turtle, Screen
import random

turtle=Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turtle.shape('turtle')
move=[30, -30]
angle=[0,90,180,360]

turtle.width(10)
for i in range(200):
    turtle.color(random.choice(colors))
    turtle.forward(random.choice(move))
    turtle.right(random.choice(angle))

screen=Screen()
screen.exitonclick()
