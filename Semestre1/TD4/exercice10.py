#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 10 ----- '''

from turtle import *

def DessinePolygone(nbCote, longueur, startCoord, couleur):
    color(couleur)
    up()
    goto(startCoord)
    down()
    for loop in range(nbCote):
        forward(longueur)
        left(360/nbCote)
        
def DessineCarre(longueur, startCoord, couleur):
    DessinePolygone(4, longueur, startCoord, couleur)

longueur = int(input("Longueur du carré : "))
nbCarre = int(input("Nombre de carrés : "))
facteurDaccroissemment = float(input("Facteur d'accroissemment : "))
coordinates = (-200, -200)

for i in range(nbCarre):
    DessineCarre(longueur, coordinates, "black")
    coordinates = (coordinates[0] + longueur, coordinates[1] + longueur)
    longueur *= facteurDaccroissemment 

exitonclick()