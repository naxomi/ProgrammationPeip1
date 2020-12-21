''' Exercice 6 '''
    
from turtle import *

length = int(input("Longueur du côté du carré : "))

for steps in range(4):
    forward(length)
    left(90)