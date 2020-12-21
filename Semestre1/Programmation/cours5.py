#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 1 ----- '''

mot = input("un mot : ")
i = 0

while i < len(mot):
   print(mot[i])
   i = i + 2

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

##########################################################################

''' ----- Exercice 3 ----- '''

def CalculApparitionLettre(mot, lettre):
    
    i = 0
    nbApparitionLettre = 0
    
    while i < len(mot):
        if mot[i] == lettre:
            nbApparitionLettre += 1
        i += 1
        
    return(nbApparitionLettre)

reponseUtilisateur = "o"

while reponseUtilisateur == "o":
    mot = input("Un mot : ")
    lettre = input("Une lettre : ")
    
    print(CalculApparitionLettre(mot, lettre))

    reponseUtilisateur = str(input("Voulez-vous continuer ? (o/n) : "))

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

##########################################################################

''' ----- Exercice 5 ----- '''

def Renverse(mot):
    motRenverse = ""
    
    for lettre in mot:
        motRenverse = lettre + motRenverse
        
    return motRenverse

mot = str(input("Un mot : "))
print(Renverse(mot))

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

##########################################################################

''' ----- Problème 1 ----- '''
    
def audioActive(terme):

    chiffreActuel = terme[0]
    compteurDeChiffres = 0
    nouveauTerme = ""
    
    for chiffre in terme:
        if chiffre == chiffreActuel:
            compteurDeChiffres += 1
        else:
            nouveauTerme += str(compteurDeChiffres) + chiffreActuel
            chiffreActuel = chiffre
            compteurDeChiffres = 1
    
    nouveauTerme += str(compteurDeChiffres) + chiffreActuel
    
    return nouveauTerme
        
nbIteration = int(input("Combien de termes (>= 2) ? : "))

terme = "1"
print("Terme 1 : ", terme)

for loop in range(1, nbIteration):
    terme = audioActive(terme)
    print(f"Terme {loop + 1} : ", terme)
    
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

##########################################################################     