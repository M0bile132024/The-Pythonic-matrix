# Fire Vs Water REBOOT
# Author:M0bile132025
# Date: 28/09/2025
# Description:Reboot of the orginal Fire Vs Water I made like 5 or so years ago.Don't expect a full series or anything.
''' A simple program to demonstrate the use of loops in Python using the turtle graphics library. 
'''
from turtle import *
from random import randint

# Constants
DIAMOND_SHAPE = ((0, 10), (10, 0), (0, -10), (-10, 0))


def Vertical_line(steps):
    write(steps, font=("Arial", 16, "normal"),align="center")
    right(90)
    forward(10)
    pendown()
    forward(280)
    penup()
    backward(290)
    left(90)
    forward(50)
def horizontal_line(steps):
    if steps != 0:
        backward(10)
        write(steps, font=("Arial", 16, "normal"),align="center")
        forward(10)
    backward(20)
    pendown()
    forward(280)
    penup()
    backward(260)
    right(90)
    forward(50)
    left(90)

    
# Main program
title("Fire Vs Water REBOOT")
speed(0)
hideturtle()
pencolor("black")
penup()
goto(-140,140)
for steps in range(6):
    Vertical_line(steps)
goto(-140,140)
for steps in range(6):
    horizontal_line(steps)

fire = Turtle()
fire.color("red")
fire.shape("circle")
fire.penup()
fire.goto(-160,120)
fire.pendown()
fire.pensize(3)




water = Turtle()
water.color("blue")
water.shape("square")
water.penup()
water.goto(-160,60)
water.pendown()
water.pensize(3)

earth = Turtle()
earth.color("green")
earth.shape("triangle")
earth.penup()
earth.goto(-160,0)
earth.pendown()
earth.pensize(3)

air = Turtle()
air.color("purple")
register_shape("diamond", DIAMOND_SHAPE)
air.shape("diamond")
air.penup()
air.goto(-160,-60)
air.pendown()
air.pensize(3)
for turn in range(100):
    fire.forward(randint(0,5))
    water.forward(randint(0,5))
    earth.forward(randint(0,5))
    air.forward(randint(0,5))
# Marks the end of the turtle graphics program
done()
