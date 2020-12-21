#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Problème 3 ----- '''

def PascalFonction(listeDeCoefficients):
    listeNouveauCoefficients = []
    
    for index, coef in enumerate(listeDeCoefficients):
        if index == 0:
            listeNouveauCoefficients.append(1)
        else:
            listeNouveauCoefficients.append(listeDeCoefficients[index - 1] + listeDeCoefficients[index])
    
    listeNouveauCoefficients.append(1)
    
    return listeNouveauCoefficients

def Pascal(rangMax):
    
    listeDeCoefficients = [1]
    
    for loop in range(rangMax+1):
        listeDeCoefficients = PascalFonction(listeDeCoefficients)
        
        ligne = ""
        
        for coef in listeDeCoefficients:
            ligne += str(coef) + " "
        print(ligne)

nbIteration = int(input("Nombre de lignes à afficher : "))

Pascal(nbIteration)