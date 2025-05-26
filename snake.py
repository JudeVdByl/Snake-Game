import time
from turtle import Screen, Turtle

class Snake:

    def __init__(self, screen):
        self.screen = screen
        self.snake_body = []

    def create_snake(self):
        pos = -60

        #Create the original body of the snake witha default length of 3
        for t in range(3):
            pos += 21
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.goto(pos, 0)
            self.snake_body.append(t)




    def go_up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)


    def go_down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)


    def go_left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)


    def go_right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def move(self):

        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)

        self.snake_body[0].forward(20)

    def create(self):
        t = Turtle()
        tail_x = (self.snake_body[-1].xcor())
        tail_y = (self.snake_body[-1].ycor())
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(tail_x, tail_y)
        self.snake_body.append(t)

    def collision(self):
        if self.snake_body[0].xcor() < -300 or self.snake_body[0].xcor() > 300 or self.snake_body[0].ycor() < -300 or self.snake_body[0].ycor() > 300:
            return True
        for seg in self.snake_body[1:]:
            if self.snake_body[0].distance(seg) < 0.1:
                return True
        return False


            
