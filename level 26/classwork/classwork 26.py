from turtle import *

def walk():
    color("blue")
    forward(200)
    left(90)


def fall_back():
    color("red")
    left(90)
    forward(200)


def all_movement():
    walk()
    fall_back()

all_movement()
all_movement()

exitonclick()