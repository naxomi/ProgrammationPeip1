''' Probleme 3 '''

from turtle import *
import math

#nbCotePoly = int(input("Nombre de cotes : "))
#coteExterieur = int(input("Longueur des cotes : "))
#nbPolygone = int(input("Nombre de polygones : "))
#f = float(input("Facteur de retrecissement des cotes : "))

window = Screen()

nbCotePoly = 5
longueurCote = 100
nbPolygone = 2
f = 0.5

for polygone in range(nbPolygone):
    for cote in range(nbCotePoly):
        forward(longueurCote)
        left(360/nbCotePoly)

    forward(longueurCote * f)
    left(66)
    longueurCote = sin(degrees( (sin(degrees(360/nbCotePoly)) * int(longueurCote * f)) / (int(longueurCote * (1 - f)) + tan(degrees(180 - 360/nbCotePoly + 90))) * sin(degrees(360/nbCotePoly)) * (longueurCote *f) )) * sin(degrees(360/nbCotePoly)) * int(longueurCote * (1 - f))
    print(longueurCote)

window.exitonclick()