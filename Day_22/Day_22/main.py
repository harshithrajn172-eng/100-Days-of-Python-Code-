from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=800,height=600)
screen.title("pong")
screen.bgcolor("black")
screen.tracer(0)
paddle_1=Paddle(380,0)
paddle_2=Paddle(x_cor=-380,y_cor=0)
ball=Ball()
score=Scoreboard()


screen.listen()
screen.onkey(paddle_1.up,"Up")
screen.onkey(paddle_1.down,"Down")
screen.onkey(paddle_2.up,"w")
screen.onkey(paddle_2.down,"s")


game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(paddle_1)<50and ball.xcor()>320 or  ball.distance(paddle_2) < 50 and ball.xcor() <-320:
        ball.bounce_x()

    if ball.xcor()>400:
        ball.goto(0,0)
        ball.move_speed=0.1
        ball.bounce_x()
        score.r_point()
    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.move_speed=0.1
        ball.bounce_x()
        score.l_point()







screen.listen()
screen.onkey(paddle_1.up(),"Up")
screen.onkey(paddle_1.down(),"Down")
screen.onkey(paddle_2.up(),"w")
screen.onkey(paddle_2.down(),"s")










screen.exitonclick()