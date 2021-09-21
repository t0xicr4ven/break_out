from turtle import Turtle


class Ball(Turtle):

    def __init__(self, paddle, brick_lst):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.dx, self.dy = 5,6
        self.paddle = paddle
        self.brick_lst = brick_lst

    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)

        #boarder
        if self.xcor() <= -380 or self.xcor() >= 380:
            self.dx *= -1
        if self.ycor() >= 280:
            self.dy *= -1
        if self.ycor() < -300:
            self.goto(0,0)
        # paddle

        if(-240 <= self.ycor() <= -230) and (self.paddle.xcor()-60 <
                self.xcor() < self.paddle.xcor()+60) and self.dy<0:
            self.dy *= -1
