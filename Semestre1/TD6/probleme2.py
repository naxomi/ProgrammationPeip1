#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Problème 2 ----- '''

from random import randint
from lireListe import lireListeMot

def Permute(listeDeMot):
    listeDeMotPermute = []
    
    for mot in listeDeMot:
        indice = randint(1, len(mot) - 1)
        
        for loop in range(indice):
            mot = mot[1:] + mot[0]
            
        listeDeMotPermute.append(mot)

    return listeDeMotPermute

listeDeMot = lireListeMot("Liste de mots à permuter aléatoirement : ")
print(Permute(listeDeMot))