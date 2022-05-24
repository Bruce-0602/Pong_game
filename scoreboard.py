from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
L_SCORE_POSITION = (-100, 200)
R_SCORE_POSITION = (100, 200)

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("pink")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(L_SCORE_POSITION)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(R_SCORE_POSITION)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()