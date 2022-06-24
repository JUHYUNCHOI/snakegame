import turtle

class Tails:
    def __init__(self):
        self.tails = []

    def addTail(self, t):
        self.tails.append(t)

class Tail:
    def __init__(self):
        self.tail = turtle.Turtle()
        self.tail.shape('square')
        self.tail.color('blue')
        self.tail.penup()
        self.tail.speed(0)
        self.tail.direction = 'stop'
        self.tail.goto(0, 100)

    def getX(self):
        return self.tail.xcor()

    def getY(self):
        return self.tail.ycor()

    def goto(self, x, y):
        self.tail.goto(x, y)

class Head:
    def __init__(self):
        self.head = turtle.Turtle()
        self.head.shape('square')
        self.head.color('blue')
        self.head.penup()
        self.head.speed(0)
        self.head.direction = 'stop'
        self.head.goto(0, 100)

    def move(self):
        if self.head.direction == 'right':
            x = self.head.xcor()
            self.head.setx(x + 20)
        elif self.head.direction == 'left':
            x = self.head.xcor()
            self.head.setx(x - 20)
        elif self.head.direction == 'up':
            y = self.head.ycor()
            self.head.sety(y + 20)
        elif self.head.direction == 'down':
            y = self.head.ycor()
            self.head.sety(y - 20)

    def move_up(self):
        self.head.direction = 'up'

    def move_down(self):
        self.head.direction = 'down'

    def move_right(self):

        self.head.direction = 'right'

    def move_left(self):

        self.head.direction = 'left'

    def getDistance(self, x, y):
        return self.head.distance(x, y)

    def getX(self):
        return self.head.xcor()

    def getY(self):
        return self.head.ycor()

    def goto(self,x, y):
        self.head.goto(x, y)



