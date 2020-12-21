#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 2 ----- '''

listeAVerifier = [[12,12,15,20,5], [-1,100,18,15,-34,8]]

for liste in listeAVerifier:
    moyenne = 0
    somme = 0
    for nombre in liste:
        somme += nombre
    moyenne = somme / len(liste)
    print(f"La liste {liste} a une moyenne de : {moyenne}")