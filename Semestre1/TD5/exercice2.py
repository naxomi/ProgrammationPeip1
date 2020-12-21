#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 2 ----- '''
   
def CalculApparitionLettre(mot, lettre):
    
    i = 0
    nbApparitionLettre = 0
    
    while i < len(mot):
        if mot[i] == lettre:
            nbApparitionLettre += 1
        i += 1
        
    return(nbApparitionLettre)

mot = input("Un mot : ")
lettre = input("Une lettre : ")

print(CalculApparitionLettre(mot, lettre))