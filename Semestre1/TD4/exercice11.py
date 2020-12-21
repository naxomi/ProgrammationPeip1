#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 11 ----- '''

from turtle import *

def DessinePolygone(nbCote, longueur, startCoord=(0,0), couleur="blue"):
    color(couleur)
    up()
    goto(startCoord)
    down()
    for loop in range(nbCote):
        forward(longueur)
        left(360/nbCote)

DessinePolygone(4, 100)

exitonclick()