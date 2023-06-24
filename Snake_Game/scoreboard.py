from turtle import Turtle
ALIGN="center"
FONT=("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def update(self):
        self.clear()

    def hit(self):
        self.score+=1
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER: {self.score}", align=ALIGN, font=FONT)
