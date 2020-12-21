#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 3 ----- '''

def Fruits(listeDeFruits):

    resultat = ""
    
    for fruit in listeDeFruits:
        resultat += fruit[0]*fruit[1]
        
    resultat = resultat.replace("F", "*").replace("P", "@").replace("K", "%")
        
    return resultat
        
print(Fruits([["F",2],["K",6],["F",1],["P",3]]))