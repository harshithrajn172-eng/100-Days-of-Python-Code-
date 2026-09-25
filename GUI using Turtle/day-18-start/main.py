from turtle import Turtle, Screen
import random
tim=Turtle()
screen = Screen()
screen.colormode(255)


tim.setheading(215)
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.forward(320)
tim.setheading(0)
tim.pendown()

colors=[(147, 145, 141), (213, 208, 193), (140, 145, 141), (138, 148, 158), (35, 104, 150), (178, 137, 142)]
for i in range(1,101):

    tim.dot(20,random.choice(colors))
    tim.penup()
    tim.forward(50)
    tim.pendown()
    if i % 10 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(360)

screen.exitonclick()




