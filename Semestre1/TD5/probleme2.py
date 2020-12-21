#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Problème 2 ----- '''

def algoCesar(mot, code):
    '''

    Parameters
    ----------
    mot : str
        Le mot à traduire.
    code : int
        Le nombre indiquant le décalage dans l'alphabet.

    Returns
    -------
    motCode : str
      Le mot codé.

    '''
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    motCode = ""
    
    for lettre in mot:
        if lettre in alphabet:
            indexLettre = alphabet.index(lettre)
            motCode += alphabet[(indexLettre + code) % 26]
        else:
            motCode += lettre

    return(motCode)

mot = str(input("Mot a coder : "))
code = int(input("Code à utiliser : "))

print(algoCesar(mot, code))