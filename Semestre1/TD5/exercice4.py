#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 4 ----- '''

def Renverse(mot):
    motRenverse = ""
    i = 0
    
    while i < len(mot):
        motRenverse += mot[-i-1]
        i += 1
    
    return motRenverse

texte = str(input("Un mot : "))
texteRenverse = Renverse(texte)

if Renverse(texteRenverse) != texte:
    print("Aïe aïe aïe, une erreur...")
else:
    print("À l'envers", texteRenverse)