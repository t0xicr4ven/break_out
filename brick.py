from turtle import Turtle
import random

class Brick(Turtle):
    colors = ['green','orange','yellow','pink','purple','gold','gray','brown']

    def __init__(self,x,y):
        super().__init__()
        self.shape('square')
        self.shapesize(1,2,5)
        self.penup()
        self.color(random.choice(self.colors))
        self.goto(x,y)

