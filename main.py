from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle


WIDTH = 800
HEIGHT = 900

root = Screen()
root.setup(width=WIDTH, height=HEIGHT)
root.title('Break Out')
root.tracer(0)

ball = Ball()
paddle = Paddle((0,-400))

root.listen()
root.onkeypress(paddle.paddle_left, 'Left')
root.onkeypress(paddle.paddle_right, 'Right')

while True:
    root.update()

root.exitonclick()
