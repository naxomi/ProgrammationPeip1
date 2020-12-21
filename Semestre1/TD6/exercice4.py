#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 4 ----- '''

from turtle import *

def DessinePolygone(nbCote, longueur, startCoord, couleur="black"):
    color(couleur)
    up()
    goto(startCoord)
    down()
    for loop in range(nbCote):
        forward(longueur)
        left(360/nbCote)


def afficheListePolygone(listeDePolygone):
    for polygone in listeDePolygone:
        DessinePolygone(polygone[0], polygone[1], (polygone[2], polygone[3]))

hideturtle()

afficheListePolygone([[3,150,0,0],[6,50,-100,-100],[8,50,100,100]])

exitonclick()