''' Exercice 8 '''

from turtle import *

length = int(input("Longueur du côté de l'hexagone : "))

for steps in range(6):
    forward(length)
    left(60)