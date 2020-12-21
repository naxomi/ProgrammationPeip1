#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 6 ----- '''

from lireListe import lireListeEntier

def InsertionNombre(listeDeNombres, nombreAInserer):
    i = 0
    
    while i < len(listeDeNombres) and nombreAInserer > listeDeNombres[i]:
        i += 1
    else:
        listeDeNombres.insert(i, nombreAInserer)

    return listeDeNombres
    
listeDeNombres = lireListeEntier("Entrez une liste de nombres (séparés par des espaces) : ")
nombreAInserer = int(input("Entier à inserer dans la liste : "))

print(InsertionNombre(listeDeNombres, nombreAInserer))