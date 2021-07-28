from turtle import Turtle

ALIGN = "center"
FONT = ("Courỉe", 80,"normal" )

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 180)
        self.write(self.r_score, align=ALIGN, font=FONT)


    def l_score_increased(self):
        self.l_score +=1
        self.update_score()

    def r_score_increased(self):
        self.r_score += 1
        self.update_score()

    def win_the_game(self, player):
        self.clear()
        self.write(f"{player} wins", align=ALIGN, font=("Courỉe", 50,"normal" ))





