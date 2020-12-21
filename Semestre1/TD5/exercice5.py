#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 5 ----- '''

def Renverse(mot):
    motRenverse = ""
    
    for lettre in mot:
        motRenverse = lettre + motRenverse
        
    return motRenverse

mot = str(input("Un mot : "))
print(Renverse(mot))