from turtle import Turtle, Screen
import random

#initialize constants
screen=Screen()
screen.setup(1500,1200)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print("Your choice: "+user_bet)
colors=["red", "orange", "yellow", "green", "blue",  "purple", "indigo"]
arr=[]
move_turtle_in_start_x=-730
move_turtle_in_start_y=-1*100*3
winner=""

is_race_on=False

has_winner=False

#define functions

def random_num():
    return random.randint(0,30)

#start code for turtle race
for i in range(len(colors)):
    arr.append(Turtle())
    arr[i].color(colors[i])
    arr[i].shape("turtle")
    arr[i].penup()
    arr[i].goto(move_turtle_in_start_x,move_turtle_in_start_y)
    move_turtle_in_start_y+=100

#define the border line
border=Turtle()
border.penup()
border.goto(700,-600)
border.pendown()
border.goto(700,600)
#start the race
if user_bet:
    is_race_on=True

while is_race_on:
    for i in range(len(colors)):
        if arr[i].xcor()>=700:
            if not has_winner:
                has_winner=True
                winner=colors[i]
            is_race_on=False

        else:
            is_race_on=True
            arr[i].forward(random_num())
            move_turtle_in_start_x=-1*50*3
            

print("race is finished")
if user_bet==winner:
    print(f"you've won! The winner is {winner}")
else:
    print(f"you've lost! The winner is {winner}")




#tim.penup()
#tim.goto(-730,0)
#tim.setheading(0)




#end code for turtle race

print("done")
screen.exitonclick()
