#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 8 ----- '''

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

def DessineTriangle(longueur, startCoord, couleur):
    DessinePolygone(3, longueur, startCoord, couleur)

def DessineCercle(longueur, startCoord, couleur):
    DessinePolygone(360, longueur, startCoord, couleur)

DessineCarre(100, (-50,-50), "red")
DessineTriangle(100, (-50, -50), "blue")
DessineCercle(20, (-50, -50), "green")

exitonclick()