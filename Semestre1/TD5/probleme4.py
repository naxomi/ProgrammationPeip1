#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Problème 4 ----- '''

def Majusculise(texte):
    alphabetMinuscule = "abcdefghijklmnopqrstuvwxyz"
    listeMot = texte.split(" ")
    texteMajusculise = ""
    
    for mot in listeMot:
        if mot[0] in alphabetMinuscule:
            initialeMajuscule = chr(ord(mot[0])-32)
            texteMajusculise = texteMajusculise + initialeMajuscule + mot[1:] + " "
        else:
            texteMajusculise = texteMajusculise + mot + " " 
    
    return texteMajusculise

texte = str(input("Texte à majusculiser : "))
print(Majusculise(texte))