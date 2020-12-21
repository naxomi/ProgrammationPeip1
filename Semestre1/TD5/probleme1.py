#!/usr/bin/env python
#-*- coding: utf-8 -*- 

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

def test():
    assert (audioActive("1") == "11")
    assert (audioActive("11") == "21")
    assert (audioActive("21") == "1211")
    assert (audioActive("1211") == "111221")
    assert (audioActive("111221") == "312211")
    assert (audioActive("312211") == "13112221")
    assert (audioActive("132221") == "11133211")
    print("Tests passés")

test()