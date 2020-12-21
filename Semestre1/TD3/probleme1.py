''' Problème 1  '''

from turtle import *
import turtle
up()

window = turtle.Screen()

hauteur = window_height()
largeur = window_width()

hauteur = 720
largeur = 675

print(largeur, hauteur)

longMarche = int(input("Longueur des marches : "))
largMarche = int(input("Largeur des marches : "))
nbMarche = int(input("Nombre de marches : "))

turtle.goto(int(-(largeur-20) / 2), int((hauteur-20) / 2))
turtle.write("Départ")

print("hey")

turtle.done()
turtle.bye()

window.exitonclick()