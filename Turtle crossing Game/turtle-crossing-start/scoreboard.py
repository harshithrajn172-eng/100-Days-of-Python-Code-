from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score=0
        self.goto(-220, 240)
        self.writing()


    def writing(self):
        self.write(f"Level:{self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.writing()

    def game_over(self ):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)




