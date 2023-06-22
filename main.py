from turtle import Turtle, Screen

turtle=Turtle()
turtle.shape('turtle')
turtle.color('firebrick')
draw=True
for sides in range (2,11):
#    sides=int(input("Enter the number of sides: "))
#    if sides=='off':
#        draw=False
#        break
    turn=(sides-2)*180/sides
    for i in range(sides):
        turtle.forward(100)
        turtle.right(180-turn)

screen=Screen()
screen.exitonclick()
