#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 7 ----- '''

from turtle import *

def DessinePolygone(nbCote, longueur, startCoord, couleur):
    color(couleur)
    up()
    goto(startCoord)
    down()
    for loop in range(nbCote):
        forward(longueur)
        left(360/nbCote)
    
hideturtle()    
tracer(False)

DessinePolygone(4, 50, (0,0), "brown")
DessinePolygone(3, 100, (-25,50), "green")

exitonclick()