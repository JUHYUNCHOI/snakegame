import turtle
import snake
import food
import time


screen = turtle.Screen()

screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.bgcolor('#ffcbcb')

screen.tracer(0)

head = snake.Head()


screen.listen()

screen.onkeypress(head.move_up, 'w')
screen.onkeypress(head.move_down, 's')
screen.onkeypress(head.move_left, 'a')
screen.onkeypress(head.move_right, 'd')


score = 0
high_score = 0
food = food.Food()


pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write('Score: 0, High Score: 0', align="center", font=('candara', 24, 'bold'))

while True:
    screen.update()

    x = food.getX()
    y = food.getY()
    if head.getDistance(x, y) < 20:
        food.goToRandom(-280, 280, -280, 280)
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write('Score: {}, High Score: {}'.format(score, high_score), align="center", font=('candara', 24, 'bold'))

    hx = head.getX()
    hy = head.getY()

    if hx > 300 or hx < -300 or hy < -300 or  hy > 300:
        score = 0
        head.goto(0, 0)

        pen.clear()
        pen.write('Score: {}, High Score: {}'.format(score, high_score), align="center", font=('candara', 24, 'bold'))

    head.move()
    time.sleep(0.1)
