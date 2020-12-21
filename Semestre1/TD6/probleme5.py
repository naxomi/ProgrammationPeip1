#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Problème 5 ----- '''

from turtle import *
import os
from random import randint

def DessineRectangle(longueur, largeur, couleur="black"):
    hideturtle()
    color(couleur)
    begin_fill()
    for loop in range(2):
        forward(longueur)
        left(90)
        forward(largeur)
        left(90)
    end_fill()

def DessinerLaPotence():
    hideturtle()
    up()
    goto(0,-100)
    down()
    setheading(0)
    DessineRectangle(175, 10)

    up()
    goto(150, -100)
    down()
    setheading(90)
    DessineRectangle(250, 10)

    up()
    goto(150, 155)
    down()
    setheading(180)
    DessineRectangle(100, 10)

    up()
    goto(50, 155)
    setheading(270)
    DessineRectangle(40, 10)

def DessinerBonhomme(nbCoupsRates):
    hideturtle()
    if nbCoupsRates == 1:
        #Dessine la tete
        setheading(0)
        up()
        goto(55, 85)
        down()
        circle(15)

    if nbCoupsRates == 2:
        #Dessine le corps
        setheading(0)
        up()
        goto(53,85)
        down()
        setheading(270)
        DessineRectangle(75, 4)

    if nbCoupsRates == 3:
        #Dessine la jambe de droite
        setheading(0)
        up()
        goto(53, 10)
        down()
        setheading(315)
        DessineRectangle(40, 5)

    if nbCoupsRates == 4:
        #Dessine la jambe de gauche
        setheading(0)
        up()
        goto(53, 12)
        down()
        setheading(225)
        DessineRectangle(40, 5)

    if nbCoupsRates == 5:
        #Dessine le bras de droite
        setheading(0)
        up()
        goto(54, 50)
        down()
        setheading(25)
        DessineRectangle(40, 5)

    if nbCoupsRates == 6:
        #Dessine le bras de gauche
        setheading(0)
        up()
        goto(54, 56)
        down()
        setheading(155)
        DessineRectangle(40, 5)

    if nbCoupsRates == 7:
        #Dessine l'oeil de gauche
        setheading(0)
        up()
        goto(50, 100)
        down()
        begin_fill()
        circle(3)
        end_fill()

    if nbCoupsRates == 8:
        #Dessine l'oeil de droite
        setheading(0)
        up()
        goto(60, 100)
        down()
        begin_fill()
        circle(3)
        end_fill()

    if nbCoupsRates == 9:
        #Dessine la bouche
        setheading(0)
        up()
        goto(50, 90)
        down()
        DessineRectangle(10, 2)

def creationDuDictionnaire():

    dictionnaireFichier = open("/Users/raphaelanjou/Desktop/PeiP1/Programmation/dicoFrancais.txt", "rb")
    dictionnaire = dictionnaireFichier.readlines()


    return dictionnaire

tracer(False)

DessinerLaPotence()

#Debut du jeu du pendu

print("########## Début de la partie ##########")
print("Bienvenue au jeu du pendu !")
print("Vous avez le droit à 9 erreurs pour réussir à compléter le mot.\n")

reponseUtilisateur = str(input("Voulez-vous choisir le mot à faire deviner (1) ou alors en deviner un au hasard dans le dictionnaire (2) ? (1/2) : "))

if reponseUtilisateur == "1":
    motADeviner = str(input("Choisissez le mot à faire deviner : "))
else:
    dictionnaire = creationDuDictionnaire()
    motADeviner = str(dictionnaire[randint(0, len(dictionnaire))]).replace("b'", "").replace(r"\r\n'", "")

motDevineParUtilisateur = "_" * len(motADeviner)
nbErreurs = 0
lettreDejaUtilise = ""

finDeLaPartie = False

print("\n" * 20)

while finDeLaPartie != True:

    print("---------- Nouveau tour ----------")

    print("Vous avez fait {0} erreurs (plus que {1}).".format(nbErreurs, 9 - nbErreurs))
    print("Le mot à deviner est : {0}".format(motDevineParUtilisateur.replace("", " ")))


    print("Lettre déjà utilisé :", lettreDejaUtilise.replace("", " "))
    lettreUtilisateur = str(input("Quelle lettre choisissez-vous ? : "))

    listeLettreMotDevineParUtilisateur = list(motDevineParUtilisateur)

    if lettreUtilisateur in motADeviner:

        if lettreUtilisateur in lettreDejaUtilise:
            print("Vous avez déjà essayé la lettre {0}".format(lettreUtilisateur))
        else:
            for index, lettre in enumerate(motADeviner):
                if lettre == lettreUtilisateur:
                    listeLettreMotDevineParUtilisateur[index] = lettre

    else:

        if lettreUtilisateur in lettreDejaUtilise:
            print("Vous avez déjà essayé la lettre {0}".format(lettreUtilisateur))
        else:
            print("La lettre {0} n'est pas dans le mot à deviner.".format(lettreUtilisateur))
            nbErreurs += 1
            DessinerBonhomme(nbErreurs)

        #Update the canva in case the shape didn't appeared
        up()
        goto(0,0)
        down()

    lettreDejaUtilise += lettreUtilisateur
    motDevineParUtilisateur = "".join(listeLettreMotDevineParUtilisateur)

    print("---------- Fin du tour ----------\n")
    
    if nbErreurs == 9:
        print("Vous avez perdu la partie. Le mot à deviner était : '{0}'".format(motADeviner))
        print("########## Fin de la partie ##########")
        finDeLaPartie = True

    if motDevineParUtilisateur == motADeviner:
        print("Bien joué ! Vous avez gagné la partie en devinant le mot '{0}' avec seulement {1} erreur(s) !".format(motADeviner, nbErreurs))
        print("########## Fin de la partie ##########")
        finDeLaPartie = True


exitonclick()