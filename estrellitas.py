#tan solo me deja modificar el numero de puntas desde el programa, desgraciadamente no se porque no carga con int(input)
from turtle import *
n =9


def estrella(n):
    color("red","white")
    setposition(-150,0)
    while n>4:
        forward(300)
        left((360/n)*5)
        if abs(pos())< 1:
            break

estrella(n)