from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.color('blue')
        self.shape('square')
        self.penup()
        self.shapesize(1,5)
        self.goto(pos)

    def paddle_right(self):
        if self.xcor() <= 350:
            self.goto(self.xcor()+60, self.ycor())

    def paddle_left(self):
        if self.xcor() >= -350:
            self.goto(self.xcor()-60, self.ycor())
