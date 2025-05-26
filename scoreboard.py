from turtle import Turtle

class Scoreboard:

    def __init__(self):
        self.score = Turtle()
        self.scorecount = 0
        self.score.hideturtle()
        self.score.penup()
        self.score.color("white")
        self.score.goto(x=0,y=280)
        self.score.write(f"Score: 0",move=False,align='center',font=("Arial",16,"normal"))
    # 
    # def update(self):   



    def increase_score(self):
        self.scorecount +=1
        self.score.clear()
        self.score.write(f"Score: {self.scorecount}", move=False, align='center', font=("Arial", 16, "normal"))

    def game_over(self):
        self.score.goto(0, 0)
        self.score.write("GAME OVER", align='center', font=("Arial", 24, "bold"))


