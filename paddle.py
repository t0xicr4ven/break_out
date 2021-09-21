from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.color('blue')
        self.shape('square')
        self.penup()
        self.shapesize(1,4)
        self.goto(pos)
        self.speed = 3

    def paddle_left(self):
        x = self.xcor()
        self.setx(x-10)
    
    def paddle_right(self):
        x = self.xcor()
        self.setx(x+10)

