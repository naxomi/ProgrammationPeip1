#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 6 ----- '''
    
from turtle import *

def DessinePolygone(nbCote, longueur, startCoord, couleur):
    color(couleur)
    up()
    goto(startCoord)
    down()
    for loop in range(nbCote):
        forward(longueur)
        left(360/nbCote)
        
nbCote = int(input("Nombre de côtés : "))
longueur = int(input("Longueur des côtés : "))
xCoord = int(input("Coordoonées de départ (x) : "))
yCoord = int(input("Coordoonées de départ (y) : "))
startCoord = (xCoord, yCoord)
couleur = str(input("Couleur : "))

DessinePolygone(nbCote, longueur, startCoord, couleur)

exitonclick()