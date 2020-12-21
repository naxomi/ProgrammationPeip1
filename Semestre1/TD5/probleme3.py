#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Problème 3 ----- '''

def CryptographieV2(mot, clef):
    '''

    Parameters
    ----------
    mot : str
        Texte à crypter.
    clef : str
        Chaine de caractère permettant de coder le texte.

    Returns
    -------
    motCrypte : str
        Texte crypté.

    '''
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    nouvelAlphabet = ""
    lettreUtilisee = ""
    motCrypte = ""
    
    # -- Create the new alphabet using the key --
    # - Add all differents letters present in the key to the alphabet -
    for lettre in clef:
        if lettre in alphabet and lettre not in lettreUtilisee:
            nouvelAlphabet += lettre
            lettreUtilisee += lettre
    
    #Add all letters not in the key to the alphabet
    for lettre in alphabet:
        if lettre not in nouvelAlphabet:
            nouvelAlphabet += lettre
            
    #Starts encrypting the text
    for lettreACoder in mot:
        motCrypte += nouvelAlphabet[alphabet.index(lettreACoder)]
        
    return motCrypte
            
mot = str(input("Mot a crypter : "))
clef = str(input("Clef à utiliser pour crypter : "))

print(CryptographieV2(mot, clef))