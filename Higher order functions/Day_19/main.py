from turtle import Turtle , Screen
import random
is_race_on=False
screen = Screen()
screen.setup(width=500, height=400)
user_ipt=screen.textinput(title="Make a bet",prompt="Enter the turtle color to bet: ")
colors=["violet","indigo","blue","green","yellow","red"]
y=[-80,-50,-20,0,20,50]
all_turtle=[]
for i in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y[i])
    all_turtle.append(new_turtle)

if user_ipt:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)

        if turtle.xcor()>230:
            winner=turtle.pencolor()
            if winner==user_ipt:
                print(f"you win. the winner is {winner}")
            else:
                print(f"you lose.the winner is {winner}")

            is_race_on=False
screen.colormode(255)
screen.exitonclick()


