from cmath import sqrt
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


# Ball object 1
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("circle")
ball1.color("white")
#ball1.penup()
ball1.goto(200, 0)

# Ball object 2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("circle")
ball2.color("red")
ball2.penup()
ball2.goto(0, 0)


#variables
t = 0
x_speed1 = 0
y_speed1 = 1.4
x_speed2 = 0
y_speed2 = 0
TIMER_VALUE = 1000//FPS
xpos1 = 0
ypos1 = 0
xpos2 = 50
ypos2 = 50
A = -9.8
square = math.sqrt
cos = math.cos
sin = math.sin
weird_tan = math.atan2
m1 = 1
m2 = 3*(10**12)
G = 6.6743*(10**(-11))
F = 0



 
def update_position():
    global xpos1, ypos1, y_speed1, x_speed1, t, xpos2, ypos2, y_speed2, x_speed2, r, F, theta, Fx, Fy, dx, dy, Ax1, Ax2, Ay1, Ay2, m1, m2
    t += TIMER_VALUE*(.0001)
    
    dx = xpos2 - xpos1
    dy = ypos2 - ypos1
    radius = square((dx**2) + (dy**2))
    F = (G*m1*m2)/(radius**2)
    theta = weird_tan(dy,dx)
    Fx = F*cos(theta)
    Fy = F*sin(theta)
    Ax1 = Fx/m1
    Ax2 = Fx/m2
    Ay1 = Fy/m1
    Ay2 = Fy/m2
    
    
    x_speed1 += Ax1*t
    y_speed1 += Ay1*t
    xpos1 = (ball1.xcor() + x_speed1*t + ((Ax1*(t**2))/2))
    ypos1 = (ball1.ycor() + y_speed1*t + ((Ay1*(t**2))/2))

    x_speed2 += Ax2*t
    y_speed2 += Ay2*t
    xpos2 = (ball2.xcor() + x_speed2*t + ((Ax2*(t**2))/2))
    ypos2 = (ball2.ycor() + y_speed2*t + ((Ay2*(t**2))/2))

    ball1.goto(xpos1, ypos1) #ball position update
    if ball1.ycor() < -400: #ball1 y bounce
        ball1.sety(-400)
        y_speed1 *= -1
    if ball1.ycor() > 400:
        ball1.sety(400)
        y_speed1 *= -1

    if ball1.xcor() > 400: #ball1 x bounce
        ball1.setx(400)
        x_speed1 *= -1
    if ball1.xcor() < -400:
        ball1.setx(-400)
        x_speed1 *= -1
    print(F, theta, Ax2)

    ball2.goto(xpos2, ypos2) # ball position update
    if ball2.ycor() < -400: #ball2 y bounce
        ball2.sety(-400)
        y_speed2 *= -1
    if ball2.ycor() > 400:
        ball2.sety(400)
        y_speed2 *=-1
    
    if ball2.xcor() > 400: #ball2 x bounce
        ball2.setx(400)
        x_speed2 *= -1
    if ball2.xcor() < -400:
        ball2.setx(-400)
        x_speed2 *= -1
    #print(xpos2, ypos2, t)

    wn.ontimer(update_position, TIMER_VALUE)

wn.ontimer(update_position,TIMER_VALUE)



while True:
    wn.update()