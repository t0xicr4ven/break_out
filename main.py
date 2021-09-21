from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from brick import Brick

WIDTH = 800
HEIGHT = 600

bricks = []

root = Screen()
root.setup(width=WIDTH, height=HEIGHT)
root.title('Break Out')
root.tracer(0)
root.bgcolor(0,0,0)

paddle = Paddle((0,-250))
ball = Ball(paddle, bricks)
bx = -370
by = 430

for _ in range(10):
    for _ in range(14):
        target = Brick(bx,by)
        bricks.append(target)
        bx += 56
    by -= 29
    bx = -370


root.listen()
root.onkeypress(paddle.paddle_left, 'Left')
root.onkeypress(paddle.paddle_right, 'Right')

while True:
    root.update()
    ball.move()
    for i in bricks:
        if i.ycor()-20 <= ball.ycor() <= i.ycor()+20 and (i.xcor()-60 <
                ball.xcor()<i.xcor()+60 and ball.dy>0):
            i.goto(1000,1000)
            ball.dy *= -1
            bricks.remove(i)
root.exitonclick()
