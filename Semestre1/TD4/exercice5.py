#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 5 ----- '''

def SurfaceMur(hauteur,largeur,longueur):
    return((2 * hauteur * largeur) + (2 * hauteur * longueur))

surfaceTotale = 0
nomDeLaPiece = ""

nombreDePieces = int(input("Nombre de pièces : "))
hauteur = float(input("Hauteur des pièces (en m) : "))

for loop in range(nombreDePieces):
    nomDeLaPiece = str(input("Nom de la pièce : "))
    largeur = float(input("Largeur de la pièce (en m) : "))
    longueur = float(input("Longueur de la pièce (en m) : "))
    
    surfacePiece = SurfaceMur(hauteur, largeur, longueur)
    
    surfaceTotale += surfacePiece
    
    print(f"La surface du {nomDeLaPiece} est : {surfacePiece} m^2.")
    
print(f"La surface totale à peindre est : {surfaceTotale} m^2.")