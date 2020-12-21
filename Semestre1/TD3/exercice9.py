''' Exercice 9 '''

from turtle import *

length = int(input("Longueur du côté du carré : "))
nombreCarre = int(input("Nombre de carrés à dessiner : "))

x = -350
y = -300

up()
goto(x,y)
down()

# --- Version 1 ---
for loop in range(nombreCarre):
    for steps in range(4):
        fd(length)
        left(90)
    x += length
    y += length
    
    up()
    goto(x,y)
    down()

# --- Version 2 ---
for loop in range(nombreCarre):
    for steps in range(6):
        fd(length)
        left(90)
    right(180)