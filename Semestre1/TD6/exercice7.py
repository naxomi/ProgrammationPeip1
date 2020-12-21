#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 7 ----- '''

from lireListe import lireListeEntier

def RangementListeNombre(listeDeNombres1, listeDeNombres2):
    
    listeComplete = listeDeNombres1 + listeDeNombres2
    listeComplete.sort()
    
    return(listeComplete)
    
listeDeNombres1 = lireListeEntier("Entrez une liste de nombres (séparés par des espaces) : ")
listeDeNombres2 = lireListeEntier("Entrez une autre liste de nombres (séparés par des espaces) : ")
    
print(RangementListeNombre(listeDeNombres1, listeDeNombres2))