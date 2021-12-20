#tan solo me deja modificar el numero de puntas desde el programa, desgraciadamente no se porque no carga con int(input)
n = 9
from turtle import *
color("red","white")


if n>5:
    setposition(-150,0)
    while True:
        forward(300)
        left((360/n)*5)
        if abs(pos())< 1:
            break