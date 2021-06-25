from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=220)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=220)
        self.write(f"Score : {self.score}", align="center", font=("Verdana", 15, "normal"))

    def gameover(self):
        self.penup()
        self.hideturtle()
        self.color("blue")
        self.goto(x=-100, y=0)
        self.write("GAME OVER", font=("courier", 30, "normal"))