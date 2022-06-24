import turtle
import random

class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.shape('turtle')
        self.food.color('orange')
        self.food.penup()
        self.food.speed(0)
        self.food.direction = 'stop'
        self.food.goto(0, 0)


    def getX(self):
        return self.food.xcor()

    def getY(self):
        return self.food.ycor()

    def goToRandom(self,x1, x2, y1, y2):
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)

        self.food.goto(x,y)









