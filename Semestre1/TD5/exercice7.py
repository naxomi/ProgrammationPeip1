#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 7 ----- '''

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

mot = ""
nbPalindromes = 0
nbMots = 0

while mot != "fin":
    mot = str(input("Un mot : "))
    
    if Palindrome(mot) == True:
        nbPalindromes += 1
    
    nbMots += 1
    
nbMots -= 1 #Car le mot fin n'est pas comptabilisé comme un des mots entré
    
print(f"Vous avez entrez {nbMots} mots dont {nbPalindromes} palindromes.")