#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 1 ----- '''

l = ["fraise","kiwi",[12,34,56],5.34,"bonjour"]

print(l[1])
print(l[2])
print(l[2][1])
print(l[1:3])
print(l[3:5])
print(l)
l.append("adieu")
print(l)

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

##########################################################################

''' ----- Exercice 3 ----- '''

def Fruits(listeDeFruits):

    resultat = ""
    
    for fruit in listeDeFruits:
        resultat += fruit[0]*fruit[1]
        
    resultat = resultat.replace("F", "*").replace("P", "@").replace("K", "%")
        
    return resultat
        
print(Fruits([["F",2],["K",6],["F",1],["P",3]]))

##########################################################################

''' ----- Exercice 4 ----- '''

from turtle import *

def DessinePolygone(nbCote, longueur, startCoord, couleur="black"):
    color(couleur)
    up()
    goto(startCoord)
    down()
    for loop in range(nbCote):
        forward(longueur)
        left(360/nbCote)


def afficheListePolygone(listeDePolygone):
    for polygone in listeDePolygone:
        DessinePolygone(polygone[0], polygone[1], (polygone[2], polygone[3]))

hideturtle()

afficheListePolygone([[3,150,0,0],[6,50,-100,-100],[8,50,100,100]])

exitonclick()

##########################################################################

''' ----- Exercice 5 ----- '''

from lireListe import lireListeEntier

reponseUtilisateur = "o"

while reponseUtilisateur == "o":
    listeDeNotes = lireListeEntier("Entrez une liste de notes : ")
    listeDeCoefs = lireListeEntier("Entrez une liste de coefficients pour chaque note : ")
    
    moyennePonderee = 0
    nbNotes = 0
    
    for loop in range(len(listeDeNotes)):
        moyennePonderee += listeDeNotes[loop] * listeDeCoefs[loop]
        nbNotes += listeDeCoefs[loop]
        
    moyennePonderee /= nbNotes
    
    print(f"La moyenne pondérée est : {moyennePonderee}")
    
    reponseUtilisateur = str(input("Voulez-vous continuer ? (o/n) : "))

##########################################################################

''' ----- Exercice 6 ----- '''

from lireListe import lireListeEntier

def InsertionNombre(listeDeNombres, nombreAInserer):
    i = 0
    
    while i < len(listeDeNombres) and nombreAInserer > listeDeNombres[i]:
        i += 1
    else:
        listeDeNombres.insert(i, nombreAInserer)

    return listeDeNombres
    
listeDeNombres = lireListeEntier("Entrez une liste de nombres (séparés par des espaces) : ")
nombreAInserer = int(input("Entier à inserer dans la liste : "))

print(InsertionNombre(listeDeNombres, nombreAInserer))

##########################################################################

''' ----- Exercice 7 ----- '''

from lireListe import lireListeEntier

def RangementListeNombre(listeDeNombres1, listeDeNombres2):
    
    listeComplete = listeDeNombres1 + listeDeNombres2
    listeComplete.sort()
    
    return(listeComplete)
    
listeDeNombres1 = lireListeEntier("Entrez une liste de nombres (séparés par des espaces) : ")
listeDeNombres2 = lireListeEntier("Entrez une autre liste de nombres (séparés par des espaces) : ")
    
print(RangementListeNombre(listeDeNombres1, listeDeNombres2))

##########################################################################

''' ----- Problème 1 ----- '''

from lireListe import lireListeEntier

# --- Fonctions du programme ---
def LectureMatrice():
    nbLignes = int(input("Combien de lignes : "))
    nbColonnes = int(input("Combien de colonnes : "))
    matrice = []
    
    print(f"\nLecture d'une matrice de taille ( {nbLignes} , {nbColonnes} )")
    
    for ligne in range(nbLignes):
        ligneActuelle = lireListeEntier(f"Ligne {ligne + 1} de taille {nbColonnes} : ")
        matrice.append(ligneActuelle)
    
    return matrice
    
def LectureVecteur(matrice):
    vecteur = lireListeEntier(f"Vecteur d'entiers de taille {len(matrice[0])} : ")
    return vecteur

def CalculProduit(matrice, vecteur):
    
    produit = []
                        
    for ligne in matrice:
        somme = 0
        for index, nombre in enumerate(ligne):
            somme += nombre * vecteur[index]
        produit.append(somme)
        
    return produit

# --- Debut de l'algorithme
reponseUtilisateur = "o"

print("--- Produits matriciels ---")

while reponseUtilisateur == "o":
    
    matrice = LectureMatrice()
    vecteur = LectureVecteur(matrice)
    produit = CalculProduit(matrice, vecteur)
        
    print(f"Le produit de votre calcul est : {produit}")
    
    reponseUtilisateur = str(input("Voulez-vous continuer ? (o/n) : "))
    
    pass

##########################################################################

''' ----- Problème 2 ----- '''

from random import randint
from lireListe import lireListeMot

def Permute(listeDeMot):
    listeDeMotPermute = []
    
    for mot in listeDeMot:
        indice = randint(1, len(mot) - 1)
        
        for loop in range(indice):
            mot = mot[1:] + mot[0]
            
        listeDeMotPermute.append(mot)

    return listeDeMotPermute

listeDeMot = lireListeMot("Liste de mots à permuter aléatoirement : ")
print(Permute(listeDeMot))

##########################################################################

''' ----- Problème 3 ----- '''

def PascalFonction(listeDeCoefficients):
    listeNouveauCoefficients = []
    
    for index, coef in enumerate(listeDeCoefficients):
        if index == 0:
            listeNouveauCoefficients.append(1)
        else:
            listeNouveauCoefficients.append(listeDeCoefficients[index - 1] + listeDeCoefficients[index])
    
    listeNouveauCoefficients.append(1)
    
    return listeNouveauCoefficients

def Pascal(rangMax):
    
    listeDeCoefficients = [1]
    
    for loop in range(rangMax+1):
        listeDeCoefficients = PascalFonction(listeDeCoefficients)
        
        ligne = ""
        
        for coef in listeDeCoefficients:
            ligne += str(coef) + " "
        print(ligne)

nbIteration = int(input("Nombre de lignes à afficher : "))

Pascal(nbIteration)

##########################################################################

''' ----- Problème 4 ----- '''

def AfficherEleve(listeEleves):
    elevesDeLaClasse = []
    
    for eleve in listeEleves:
        elevesDeLaClasse.append(eleve[1] + " " + eleve[0])
        
    return elevesDeLaClasse
    
def CalculMoyenneClasse(listeEleves):
    moyenneDeLaClasse = 0
    
    for eleve in listeEleves:
        moyenneDeLaClasse += eleve[2]
        
    moyenneDeLaClasse /= len(listeEleves)
    
    return moyenneDeLaClasse

def TrouverLeMajor(listeEleves):
    major = ""
    meilleureNote = 0
    
    for eleve in listeEleves:
        if eleve[2] > meilleureNote:
            meilleureNote = eleve[2]
            major = eleve[1] + " " + eleve[0]
        elif eleve[2] == meilleureNote:
            major += " / " + eleve[1] + " " + eleve[0]
            
    return major
        
listeEleves = [["Collavizza","Hélène",6],["Allais","Alphonse",14],["Reed","Lou",12]]

reponseUtilisateur = 0

while reponseUtilisateur != "4":
    
    print(''' Voulez-vous : 
    1. Afficher les élèves
    2. Calculer la moyenne de la classe
    3. Trouver le major de la promo
    4. Sortir ''')
          
    reponseUtilisateur = str(input("Votre choix ? : "))
                             
    if reponseUtilisateur == "1":
        print("\n Les élèves de la classe sont : ", AfficherEleve(listeEleves), "\n")
    elif reponseUtilisateur == "2":
        print("\n La moyenne de la classe est : ", CalculMoyenneClasse(listeEleves), "\n")
    elif reponseUtilisateur == "3":
        print("\n Le major de la promo est : ", TrouverLeMajor(listeEleves), "\n")

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

##########################################################################

''' ----- Problème 6 ----- '''

#--------------------------------------------------------------

def CreationListeDesCategories(stockDeCD):
    
    listeDesCategories = []
    
    for cdInformation in stockDeCD:
        if cdInformation[2] not in listeDesCategories:
            listeDesCategories.append(cdInformation[2])
    
    return listeDesCategories

#--------------------------------------------------------------

def CreationListeDesChanteurs(stockDeCD):
    
    listeDesChanteurs = []
    
    for index, cdInformation in enumerate(stockDeCD):
        if cdInformation[1] not in listeDesChanteurs:
            listeDesChanteurs.append(cdInformation[1])
    
    return listeDesChanteurs

#--------------------------------------------------------------

def isInStock(stockDeCD, informationCd):
    
    for cdDansStock in stockDeCD:
        if cdDansStock[0:4] == informationCd:
            return True

#--------------------------------------------------------------

def isInPanier(panier, informationCd):
    
    for cdDansPanier in panier:
        if cdDansPanier[0:4] == informationCd:
            return True

#--------------------------------------------------------------
  
def AfficherCd(stockDeCD):
    
    print("\n--- Liste des CD ---\n")
    
    for index, cdInformation in enumerate(stockDeCD):
        print(f"CD n°{index + 1} : {cdInformation[0]} / Chanteur : {cdInformation[1]} / Catégorie : {cdInformation[2]} / Prix : {cdInformation[3]} € / Nombre d'exemplaires : {cdInformation[4]}")
        
    print("\n--- Fin de la liste des CD ---\n")

#--------------------------------------------------------------

def AfficherCdCategorie(stockDeCD, numeroCategorie, listeDesCategories):
        
    if numeroCategorie <= len(listeDesCategories) and numeroCategorie > 0:
        categorie = listeDesCategories[numeroCategorie - 1]
    else:
        print(f"\nVous devez rentrer une valeur comprise entre 1 et {len(listeDesCategories)}.")
        return False
        
    print(f"\n--- Liste des CD de la catégorie {categorie}\n")
        
    idCd = 0
    for cdInformation in stockDeCD:
        if categorie == cdInformation[2]:
            idCd += 1
            print(f"CD n°{idCd} : {cdInformation[0]} / Chanteur : {cdInformation[1]} / Genre : {cdInformation[2]} / Prix : {cdInformation[3]} € / Nombre d'exemplaires : {cdInformation[4]}")

    print(f"\n--- Fin de la liste des CD de la catégorie {categorie}\n")

#--------------------------------------------------------------

def AfficherCdGroupe(stockDeCD, numeroChanteur, listeDesChanteurs):
    
    if numeroChanteur <= len(listeDesChanteurs) and numeroChanteur > 0:
        chanteur = listeDesChanteurs[numeroChanteur - 1]
    else:
        print(f"\nVous devez rentrer une valeur comprise entre 1 et {len(listeDesChanteurs)}.")
        return False
        
    print(f"\n--- Liste des CD du chanteur(se) : {chanteur}\n")
        
    idCd = 0
    for cdInformation in stockDeCD:
        if chanteur == cdInformation[1]:
            idCd += 1
            print(f"CD n°{idCd} : {cdInformation[0]} / Chanteur : {cdInformation[1]} / Genre : {cdInformation[2]} / Prix : {cdInformation[3]} € / Nombre d'exemplaires : {cdInformation[4]}")

    print(f"\n--- Fin de la liste des CD du chanteur(se) : {chanteur}\n")

#--------------------------------------------------------------

def CommanderCd(stockDeCD, panier, numeroCdCommande, nbExemplaireCommande):
    
    if numeroCdCommande < 1 or (numeroCdCommande - 1) > len(stockDeCD):
        print("Vous avez essayé de commander un CD qui n'était pas disponible.")
        validiteChoixUtilisateur = False
    else:
        realNumeroCdCommande = numeroCdCommande - 1    
        nbExemplaireCd = stockDeCD[realNumeroCdCommande][4]
        
        informationCdCommande = stockDeCD[realNumeroCdCommande][0:4]
        
        if numeroCdCommande < 1 or realNumeroCdCommande > len(stockDeCD):
            print("Vous avez essayé de commander un CD qui n'était pas disponible.")
            validiteChoixUtilisateur = False    
            
        elif nbExemplaireCommande <= 0:
            print(f"Vous ne pouvez pas commander {nbExemplaireCommande} exemplaires.")
            validiteChoixUtilisateur = False
            
        elif nbExemplaireCd >= nbExemplaireCommande:
        
            validiteChoixUtilisateur = True    
        
            if isInPanier(panier, informationCdCommande):
                for index, cdDansPanier in enumerate(panier):
                    if cdDansPanier[0:4] == informationCdCommande:        
                        panier[index][4] += nbExemplaireCommande
                        
                stockDeCD[realNumeroCdCommande][4] = nbExemplaireCd - nbExemplaireCommande
            else:
        
                panier.append(stockDeCD[realNumeroCdCommande][:])
                panier[-1][4] = nbExemplaireCommande
                        
                stockDeCD[realNumeroCdCommande][4] = nbExemplaireCd - nbExemplaireCommande
    
            print(f"Le CD n°{numeroCdCommande} a été ajouté à votre panier en {nbExemplaireCommande} exemplaires.\n")
            
        else:
            print(f"Il ne reste que {nbExemplaireCd} exemplaires de ce CD alors que vous avez essayé d'en commander {nbExemplaireCommande}.")
            validiteChoixUtilisateur = False
        
        if stockDeCD[realNumeroCdCommande][4] == 0:
            del stockDeCD[realNumeroCdCommande]
    
    return (panier, stockDeCD, validiteChoixUtilisateur)

#--------------------------------------------------------------

def AfficherPanier(panier):
    
    print("\n--- Votre panier")
    
    nbCd = 0
    for index, cdInformation in enumerate(panier):
        print(f"CD n°{index + 1} : {cdInformation[0]} / Chanteur : {cdInformation[1]} / Genre : {cdInformation[2]} / Prix : {cdInformation[3]} € / Nombre d'exemplaires : {cdInformation[4]}")
        nbCd += cdInformation[4]
            
    print(f"\nIl y a {nbCd} CD dans votre panier.\n")

#--------------------------------------------------------------

def SupprimerElementPanier(stockDeCD, panier, numeroCdSupprime, nbExemplaireSupprime):

    if numeroCdSupprime < 1 or (numeroCdSupprime - 1) > len(panier):
        print("Vous avez essayé de supprimer un CD qui n'était pas dans votre panier.")
        validiteChoixUtilisateur = False
    else:
        
        realNumeroCdSupprime = numeroCdSupprime - 1    
        nbExemplaireCdPanier = panier[realNumeroCdSupprime][4]
        
        informationCdSupprime = panier[realNumeroCdSupprime][0:4]
            
        if numeroCdSupprime < 1 or realNumeroCdSupprime > len(panier):
            print("Vous avez essayé de supprimer un CD qui n'était pas dans votre panier.")
            validiteChoixUtilisateur = False
        
        elif nbExemplaireSupprime <= 0:
            print(f"Vous ne pouvez pas supprimer {nbExemplaireSupprime} exemplaires.")
            validiteChoixUtilisateur = False
        
        elif nbExemplaireCdPanier >= nbExemplaireSupprime:
            
            validiteChoixUtilisateur = True
                    
            if isInStock(stockDeCD, informationCdSupprime):
                
                for index, cdDansStock in enumerate(stockDeCD):
                    if cdDansStock[0:4] == informationCdSupprime:            
                        stockDeCD[index][4] += nbExemplaireSupprime
            else:
                stockDeCD.append(panier[realNumeroCdSupprime][:])
                stockDeCD[-1][4] = nbExemplaireSupprime
                    
            panier[realNumeroCdSupprime][4] = nbExemplaireCdPanier - nbExemplaireSupprime
            
            print(f"{nbExemplaireSupprime} exemplaires du CD n°{numeroCdSupprime} ont été supprimés de votre panier.\n")
            
        else:
            print(f"Il ne reste que {nbExemplaireCdPanier} exemplaires de ce CD alors que vous avez essayé d'en supprimer {nbExemplaireSupprime}.")
            validiteChoixUtilisateur = False
        
        if panier[realNumeroCdSupprime][4] == 0:
            del panier[realNumeroCdSupprime]
    
    return (panier, stockDeCD, validiteChoixUtilisateur)

#--------------------------------------------------------------

stockDeCD = [["Suites violoncelle seul","Bylsma","classique",23.50,1], 
             ["No love","Eminem","rap",25.60,5], 
             ["J'appuie sur la gâchette","NTM","rap",13.50,10], 
             ["Symphonie du nouveau monde","Dvorak","classique",30.70,1], 
             ["Adieu tristesse","Arthur H.", "chanson francaise",15.2,10], 
             ["Mister mystère","M","chanson francaise",25.2,3], 
             ["Je dis M","M","chanson francaise",25.2,3],
             ["Pacific 231","Raphaël","chanson francaise",28.6,8]]

panier = []

reponseUtilisateur = 0

while reponseUtilisateur != "7":
    
    print(''' Voulez-vous : 
    1. Afficher tous les CD
    2. Afficher les CD d'une catégorie donnée
    3. Afficher les CD d'un groupe
    4. Commander un CD
    5. Voir votre panier
    6. Supprimer un élément de votre panier
    7. Sortir ''')
          
    reponseUtilisateur = str(input("Votre choix ? : "))
                             
    #---------------------------------------------
    if reponseUtilisateur == "1":
        AfficherCd(stockDeCD)
        
    #---------------------------------------------
    elif reponseUtilisateur == "2":
                
        listeDesCategories = CreationListeDesCategories(stockDeCD)
        
        print("Voici les catégories disponibles : ")
        for index, categorie in enumerate(listeDesCategories):
            print(f"     {index + 1}. {categorie}")
        
        while True:
            try:
                validiteChoixUtilisateur = False
                
                while validiteChoixUtilisateur == False:
                    numeroCategorie = int(input("Choisissez la catégorie : "))
                    validiteChoixUtilisateur =  AfficherCdCategorie(stockDeCD, numeroCategorie, listeDesCategories)

                    if validiteChoixUtilisateur != False:
                        validiteChoixUtilisateur == True
                
                break
            except:
                print(f"\n### Erreur ###\nLa valeur que vous avez rentrez est invalide.\nVous devez rentrer une valeur comprise entre 1 et {index + 1}.")
                
    #---------------------------------------------
    elif reponseUtilisateur == "3":

        listeDesChanteurs = CreationListeDesChanteurs(stockDeCD)
        
        print("Voici les chanteurs disponibles : ")
        for index, chanteur in enumerate(listeDesChanteurs):
            print(f"    {index + 1}. {chanteur}")
        
        while True:
            try:
                validiteChoixUtilisateur = False
                
                while validiteChoixUtilisateur == False:
                    numeroChanteur = int(input("Choisissez le chanteur : "))
                    validiteChoixUtilisateur = AfficherCdGroupe(stockDeCD, numeroChanteur, listeDesChanteurs)
    
                    if validiteChoixUtilisateur != False:
                        validiteChoixUtilisateur == True
                        
                break
            except:
                print(f"\n### Erreur ###\nLa valeur que vous avez rentrez est invalide.\nVous devez rentrer une valeur comprise entre 1 et {index + 1}.")
    
    #---------------------------------------------
    elif reponseUtilisateur == "4":

        print("\n--- Commande de CD")
        print("Voici la liste des CD disponibles à l'achat : ")
        AfficherCd(stockDeCD)        

        tailleStockDeCd = len(stockDeCD)

        if tailleStockDeCd == 0:
            print("Le magasin n'a malheureusement plus de stock.\n")

        else:
            while True:
                try:
                    validiteChoixUtilisateur = False                    
                    
                    while validiteChoixUtilisateur == False:
                        numeroCdCommande = int(input("Quel CD choisissez vous ? (indiquez le numéro) : "))
                        nbExemplaireCommande = int(input("En combien d'exemplaires ? : "))
                
                        panierAndSTockAndValidity = CommanderCd(stockDeCD, panier, numeroCdCommande, nbExemplaireCommande)
                                
                        panier = panierAndSTockAndValidity[0]
                        stockDeCD = panierAndSTockAndValidity[1]
                        validiteChoixUtilisateur = panierAndSTockAndValidity[2]
                        
                        if validiteChoixUtilisateur != False:
                            validiteChoixUtilisateur = True
                    
                    break
                except:
                    print("\n### Erreur ###\nLa valeur que vous avez rentrez est invalide.\nVérifiez que le numéro du CD choisi est correct ainsi que le nombre de ce CD disponible en stock.")
            
        print("--- Fin de la commande de CD\n")
    
    #---------------------------------------------
    elif reponseUtilisateur == "5":
        
        AfficherPanier(panier)
    
    #---------------------------------------------
    elif reponseUtilisateur == "6":

        print("\n--- Supprimer un article du panier")
        print("Voici la liste des CD dans votre panier : ")
        AfficherPanier(panier)

        if len(panier) == 0:
            print("Votre panier est déjà vide.\n")

        else:
            while True:
                try:
                    validiteChoixUtilisateur = False
                    
                    while validiteChoixUtilisateur == False:
                        numeroCdSupprime = int(input("Quel CD voulez-vous enlever ? (indiquez le numéro) : "))    
                        nbExemplaireSupprime = int(input("En combien d'exemplaires ? : "))
                
                        panierAndSTockAndValidity = SupprimerElementPanier(stockDeCD, panier, numeroCdSupprime, nbExemplaireSupprime)
                                
                        panier = panierAndSTockAndValidity[0]
                        stockDeCD = panierAndSTockAndValidity[1]
                        validiteChoixUtilisateur = panierAndSTockAndValidity[2]
                        
                        if validiteChoixUtilisateur != False:
                            validiteChoixUtilisateur = True
                    
                    break
                except:
                    print("\n### Erreur ###\nLa valeur que vous avez rentrez est invalide.\nVérifiez que le numéro du CD choisi est correct ainsi que le nombre de ce CD dans le panier.")
                    
            
        print("--- Fin de la suppression d'un article de votre panier\n")

    #---------------------------------------------

print("--- Merci d'avoir visiter notre magasin ---")

#Fin du programme
