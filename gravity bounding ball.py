import turtle
import random
import math
import time

# sets up screenspace
wn = turtle.Screen()
wn.setup(width=1000, height=1000)
wn.title("Bouncing Ball")
wn.bgcolor("black")
#wn.bgpic("IMG_8968.JPG")
turtle.hideturtle() # screen initially starts with an arrown, this hides that arrow
turtle.speed(0)
turtle.tracer(0,0)

# statics
r = random
FPS = 60


# Ball object
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#variables
t = 0
x_speed = 5
y_speed = 0
TIMER_VALUE = 1000//FPS
xpos = 0
ypos = 200
A = -4.9


 
def update_position():
    global xpos, ypos, y_speed, x_speed, t 
    t += TIMER_VALUE*(.0001)
    y_speed += A*t
    xpos = (ball.xcor() + x_speed)
    ypos = (ball.ycor() + y_speed*t + A*(t**2))

    ball.goto(xpos, ypos)
    if ball.ycor() > 400 or ball.ycor() < -400:
        ball.sety(-400)
        y_speed *= -1
    
    if ball.xcor() > 400 or ball.xcor() < -400:
        
        x_speed *= -1
    print(xpos, ypos, t)
    wn.ontimer(update_position, TIMER_VALUE)

wn.ontimer(update_position,TIMER_VALUE)



while True:
    wn.update()