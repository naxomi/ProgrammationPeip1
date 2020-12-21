#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 6 ----- '''

from math import ceil

def Palindrome(mot):
    i = 0
    
    while i < (ceil(len(mot) / 2)): #On fait varier i que jusqu'à la moitié de la longueur du mot.
        if mot[i] == mot[-i-1]: #On vérifier que les deux lettres opposées par rapport au milieu du mot son égales.
            i += 1
        else:
            return False 
        
    else: 
        return True

mot = str(input("Un mot : "))

if Palindrome(mot) == True:
    print(f"Le mot {mot} est un palindrome.")
else:
    print(f"Le mot {mot} n'est pas un palindrome.")