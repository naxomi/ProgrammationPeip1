#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 5 ----- '''

from lireListe import lireListeEntier

reponseUtilisateur = "o"

while reponseUtilisateur == "o":
    listeDeNotes = lireListeEntier("Entrez une liste de notes : ")
    listeDeCoefs = lireListeEntier("Entrez une liste de coefficients pour chaque note : ")
    
    moyennePonderee = 0
    nbNotes = 0
    
    for loop in range(len(listeDeNotes)):
        moyennePonderee += listeDeNotes[loop] * listeDeCoefs[loop]
        nbNotes += listeDeCoefs[loop]
        
    moyennePonderee /= nbNotes
    
    print(f"La moyenne pondérée est : {moyennePonderee}")
    
    reponseUtilisateur = str(input("Voulez-vous continuer ? (o/n) : "))