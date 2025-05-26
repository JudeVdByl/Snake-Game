from turtle import Turtle
import random
from snake import Snake

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.9,stretch_wid=0.9)

        self.color("yellow")
        self.speed("fastest")
        self.ate()



    def ate(self):
        self.random_x = random.randint(-280, 280)
        self.random_y = random.randint(-280, 280)
        self.goto(self.random_x,self.random_y)

