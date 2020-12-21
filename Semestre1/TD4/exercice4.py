#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 4 ----- '''

def SurfaceMur(hauteur,largeur,longueur):
    return((2 * hauteur * largeur) + (2 * hauteur * longueur))

hauteur = float(input("Hauteur de la pièce : "))
largeur = float(input("Largeur de la pièce : "))
longueur = float(input("Longueur de la pièce : "))

print(f"La surface des murs de la pièce est : {SurfaceMur(hauteur, largeur, longueur)} m^2.")