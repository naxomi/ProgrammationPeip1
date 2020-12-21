#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 9 ----- '''

def revisionMultiplication(tableAReviser, valeurMax):
    
    i = 1
    
    while i <= valeurMax:
        print(f"{i} fois {tableAReviser} = {i * tableAReviser}")
        i += 1
        
        
continuer = "o"

while continuer == "o":
    tableAReviser = int(input("Quelle table voulez-vous réviser ? : "))
    valeurMax = int(input("Jusqu'à quelle valeur ? : "))

    print("===================")
    print(f"Révision de la table de {tableAReviser} jusqu'à {valeurMax}")    

    revisionMultiplication(tableAReviser, valeurMax)
    
    print("Fin de la révision.")
    print("===================")
    
    continuer = str(input("Voulez-vous continuer ? (o/n) : "))