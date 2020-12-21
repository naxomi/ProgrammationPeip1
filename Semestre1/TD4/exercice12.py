#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 12 ----- '''

def revisionMultiplication(tableAReviser, valeurMax=10):
    
    i = 1
    
    while i <= valeurMax:
        print(f"{i} fois {tableAReviser} = {i * tableAReviser}")
        i += 1
        
continuer = "o"

while continuer == "o":
    tableAReviser = int(input("Quelle table voulez-vous réviser ? : "))

    print("===================")
    print(f"Révision de la table de {tableAReviser} jusqu'à 10.")    

    revisionMultiplication(tableAReviser)
    
    print("Fin de la révision.")
    print("===================")
    
    continuer = str(input("Voulez-vous continuer ? (o/n) : "))