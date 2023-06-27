from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        #self.high_score = 0
        with open("test.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def update(self):
        self.clear()

    def hit(self):
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset_sb(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("test.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER: {self.score}", align=ALIGN, font=FONT)
