''' Exercice 7 '''

from turtle import *

length = int(input("Longueur du côté du triangle équilatéral : "))

for steps in range(3):
    forward(length)
    left(120)