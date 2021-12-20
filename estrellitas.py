from turtle import *
color("red","white")

setposition(-150,0)
while True:
    forward(300)
    left(170)
    if abs(pos())< 1:
        break