#!/usr/bin/env python
#-*- coding: utf-8 -*- 

##########################################################################

''' ----- Exercice 1 ----- '''

def Affine(a,b,x):
    return a*x+b

print(Affine(1, 1, 1))

##########################################################################

''' ----- Exercice 2 ----- '''

def Affine(a,b,x):
    return a*x+b

print(Affine(Affine(1,1,1),1,1))

##########################################################################

''' ----- Exercice 3 ----- '''

def Affine(a,b,x):
    return a*x+b

def FahrenheitToCelsius(temperature):
    return Affine(temperature-32, b=0, x=1/1.8)

def CelsiusToFahrenheit(temperature):
    return Affine(temperature, b=32, x=1.8)

temperature = int(input("Quelle température ? : "))
unite = int(input("Quelle unité ? (°Celsius -> 0 et °Fahrenheit -> 1) : "))

if unite == 0:
    print(f"{temperature}° Celsius vaut {CelsiusToFahrenheit(temperature)}° Fahrenheit.")
elif unite == 1:
    print(f"{temperature}° Fahrenheit vaut {FahrenheitToCelsius(temperature)}° Celsius.")
  
##########################################################################

''' ----- Exercice 4 ----- '''

def SurfaceMur(hauteur,largeur,longueur):
    return((2 * hauteur * largeur) + (2 * hauteur * longueur))

hauteur = float(input("Hauteur de la pièce : "))
largeur = float(input("Largeur de la pièce : "))
longueur = float(input("Longueur de la pièce : "))

print(f"La surface des murs de la pièce est : {SurfaceMur(hauteur, largeur, longueur)} m^2.")

##########################################################################

''' ----- Exercice 5 ----- '''

def SurfaceMur(hauteur,largeur,longueur):
    return((2 * hauteur * largeur) + (2 * hauteur * longueur))

surfaceTotale = 0
nomDeLaPiece = ""

nombreDePieces = int(input("Nombre de pièces : "))
hauteur = float(input("Hauteur des pièces (en m) : "))

for loop in range(nombreDePieces):
    nomDeLaPiece = str(input("Nom de la pièce : "))
    largeur = float(input("Largeur de la pièce (en m) : "))
    longueur = float(input("Longueur de la pièce (en m) : "))
    
    surfacePiece = SurfaceMur(hauteur, largeur, longueur)
    
    surfaceTotale += surfacePiece
    
    print(f"La surface du {nomDeLaPiece} est : {surfacePiece} m^2.")
    
print(f"La surface totale à peindre est : {surfaceTotale} m^2.")
 
##########################################################################

''' ----- Exercice 6 ----- '''
    
from turtle import *

def DessinePolygone(nbCote, longueur, startCoord, couleur):
    color(couleur)
    up()
    goto(startCoord)
    down()
    for loop in range(nbCote):
        forward(longueur)
        left(360/nbCote)
        
nbCote = int(input("Nombre de côtés : "))
longueur = int(input("Longueur des côtés : "))
xCoord = int(input("Coordoonées de départ (x) : "))
yCoord = int(input("Coordoonées de départ (y) : "))
startCoord = (xCoord, yCoord)
couleur = str(input("Couleur : "))

DessinePolygone(nbCote, longueur, startCoord, couleur)

exitonclick()

##########################################################################

''' ----- Exercice 7 ----- '''

from turtle import *

def DessinePolygone(nbCote, longueur, startCoord, couleur):
    color(couleur)
    up()
    goto(startCoord)
    down()
    for loop in range(nbCote):
        forward(longueur)
        left(360/nbCote)
    
hideturtle()    
tracer(False)

DessinePolygone(4, 50, (0,0), "brown")
DessinePolygone(3, 100, (-25,50), "green")

exitonclick()

##########################################################################

''' ----- Exercice 8 ----- '''

from turtle import *

def DessinePolygone(nbCote, longueur, startCoord, couleur):
    color(couleur)
    up()
    goto(startCoord)
    down()
    for loop in range(nbCote):
        forward(longueur)
        left(360/nbCote)
        
def DessineCarre(longueur, startCoord, couleur):
    DessinePolygone(4, longueur, startCoord, couleur)

def DessineTriangle(longueur, startCoord, couleur):
    DessinePolygone(3, longueur, startCoord, couleur)

def DessineCercle(longueur, startCoord, couleur):
    DessinePolygone(360, longueur, startCoord, couleur)

DessineCarre(100, (-50,-50), "red")
DessineTriangle(100, (-50, -50), "blue")
DessineCercle(20, (-50, -50), "green")

exitonclick()
    
##########################################################################

''' ----- Exercice 9 ----- '''

def revisionMultiplication(tableAReviser, valeurMax):
    
    i = 1
    
    while i <= valeurMax:
        print(f"{i} fois {tableAReviser} = {i * tableAReviser}")
        i += 1
        
        
continuer = "o"

while continuer == "o":
    tableAReviser = int(input("Quelle table voulez-vous réviser ? : "))
    valeurMax = int(input("Jusqu'à quelle valeur ? : "))

    print("===================")
    print(f"Révision de la table de {tableAReviser} jusqu'à {valeurMax}")    

    revisionMultiplication(tableAReviser, valeurMax)
    
    print("Fin de la révision.")
    print("===================")
    
    continuer = str(input("Voulez-vous continuer ? (o/n) : "))
    
##########################################################################

''' ----- Exercice 10 ----- '''

from turtle import *

def DessinePolygone(nbCote, longueur, startCoord, couleur):
    color(couleur)
    up()
    goto(startCoord)
    down()
    for loop in range(nbCote):
        forward(longueur)
        left(360/nbCote)
        
def DessineCarre(longueur, startCoord, couleur):
    DessinePolygone(4, longueur, startCoord, couleur)

longueur = int(input("Longueur du carré : "))
nbCarre = int(input("Nombre de carrés : "))
facteurDaccroissemment = float(input("Facteur d'accroissemment : "))
coordinates = (-200, -200)

for i in range(nbCarre):
    DessineCarre(longueur, coordinates, "black")
    coordinates = (coordinates[0] + longueur, coordinates[1] + longueur)
    longueur *= facteurDaccroissemment 

exitonclick()

##########################################################################

''' ----- Exercice 11 ----- '''

from turtle import *

def DessinePolygone(nbCote, longueur, startCoord=(0,0), couleur="blue"):
    color(couleur)
    up()
    goto(startCoord)
    down()
    for loop in range(nbCote):
        forward(longueur)
        left(360/nbCote)

DessinePolygone(4, 100)

exitonclick()

##########################################################################

''' ----- Exercice 12 ----- '''

def revisionMultiplication(tableAReviser, valeurMax=10):
    
    i = 1
    
    while i <= valeurMax:
        print(f"{i} fois {tableAReviser} = {i * tableAReviser}")
        i += 1
        
continuer = "o"

while continuer == "o":
    tableAReviser = int(input("Quelle table voulez-vous réviser ? : "))

    print("===================")
    print(f"Révision de la table de {tableAReviser} jusqu'à 10.")    

    revisionMultiplication(tableAReviser)
    
    print("Fin de la révision.")
    print("===================")
    
    continuer = str(input("Voulez-vous continuer ? (o/n) : "))

##########################################################################

''' ----- Problème 1 ----- ''' 

def anneeValide(annee):
    if annee >= 1600 and annee <= 2018:
        return True
    
def moisValide(mois):
    if mois >= 1 and mois <= 12:
        return True  
    
def jourValide(jour, mois, annee):
    
    jourValide = False
    jourMax = False
        
    #Verification pour fevrier    
    if mois == 2:

        #Verification bissextille
        if annee % 4 == 0 and annee % 100 != 0 or annee % 100 == 0:
            if jour <= 29 and jour >= 1:
                jourValide = True
                jourMax = 29
            else:
                jourValide = False
        else:
            if jour <= 28 and jour >= 1:
                jourMax = 28
                jourValide = True
            else:
                jourValide = False
            
    #Verification pour les mois differents de fevriers
    elif mois % 2 == 0 and mois < 8:
        if jour <= 30 and jour >= 1:
            jourMax = 30
            jourValide = True
            
    elif mois % 2 != 0 and mois < 8:
        if jour <= 31 and jour >= 1:
            jourMax = 31
            jourValide = True
        
    elif mois % 2 == 0 and mois >= 8:
        if jour <= 31 and jour >= 1:
            jourMax = 31
            jourValide = True        
        
    elif mois % 2 != 0 and mois >= 8:
        if jour <= 30 and jour >= 1:
            jourMax = 30
            jourValide = True 
    
    else:
        jourValide = False
      
    #Output un tuple contenant la validite du jour ainsi que le jour max pour le mois en cours
    return (jourValide, jourMax)

#Debut de l'algorithme

annee = int(input("Année : "))

while anneeValide(annee) != True: 
    print("L'annee n'est pas valide.")
    annee = int(input("Année : "))
    
else:
    mois = int(input("Mois : "))
    
    while moisValide(mois) != True:
        print("Le mois n'est pas valide.")
        mois = int(input("Mois : "))
             
    else:
        jour = int(input("Jour : "))

        while jourValide(jour, mois, annee)[0] != True:
            print("Le jour n'est pas valide.")
            jour = int(input("Jour : "))
                
        else:
            print("La date est valide.")

jourMax = jourValide(jour, mois, annee)[1]

if jour < jourMax:
    print(f"La date du lendemain du {jour}/{mois}/{annee} est le : {jour + 1}/{mois}/{annee}.")
else :
    if mois < 12:
        print(f"La date du lendemain du {jour}/{mois}/{annee} est le : 1/{mois + 1}/{annee}.")
    else:
        print(f"La date du lendemain du {jour}/{mois}/{annee} est le : 1/1/{annee+1}.")

##########################################################################
 
''' ----- Problème 2 ----- '''

# ----- Definition des fonctions utilisees plus tard dans le programme ----- #

def AnneeValide(annee):
    if annee >= 1600 and annee <= 2020:
        return True
    
def MoisValide(mois):
    if mois >= 1 and mois <= 12:
        return True  

def JourValide(jour, mois, annee):
    jourValide = False
        
    #Verification pour fevrier    
    if mois == 2:
        #Verification bissextille
        if annee % 4 == 0 and annee % 100 != 0 or annee % 100 == 0:
            if jour <= 29 and jour >= 1:
                jourValide = True
            else:
                jourValide = False
        else:
            if jour <= 28 and jour >= 1:
                jourValide = True
            else:
                jourValide = False
            
    #Verification pour les mois differents de fevriers
    elif mois % 2 == 0 and mois < 8:
        if jour <= 30 and jour >= 1:
            jourValide = True
            
    elif mois % 2 != 0 and mois < 8:
        if jour <= 31 and jour >= 1:
            jourValide = True
        
    elif mois % 2 == 0 and mois >= 8:
        if jour <= 31 and jour >= 1:
            jourValide = True        
        
    elif mois % 2 != 0 and mois >= 8:
        if jour <= 30 and jour >= 1:
            jourValide = True 
    
    else:
        jourValide = False
      
    #Output un tuple contenant la validite du jour ainsi que le jour max pour le mois en cours
    return (jourValide)
    
def JourMaxDuMois(mois, annee):
    if mois == 2:
        if annee % 4 == 0 and annee % 100 != 0 or annee % 100 == 0:
            return 29
        else:
            return 28
    
    elif (mois % 2 == 0 and mois < 8) or (mois % 2 != 0 and mois >= 8):
        return 30
    else:
        return 31

def VerificationValiditeDate(date):
    jour = int(date[0:2])
    mois = int(date[3:5])
    annee = int(date[6:10])
    
    if AnneeValide(annee) != True:
        return "L'année n'est pas valide. (1600 à 2018)", False
    
    elif MoisValide(mois) != True:
        return "Le mois n'est pas valide. (1 à 12) ", False
    
    elif JourValide(jour, mois, annee) != True:
        return "Le jour n'est pas valide. (1 à 28-29-30-31 en fonction des mois)", False

    else:
        return "La date est valide.", True
    
# ----- Debut de l'algorithme ----- #
    
prix = int(input("Prix de la nuitée : "))

# ----- Vérification de la validite des dates d'arrivee et de depart ----- #

#Test de la validite de la date d'arrivee : 
dateEntreeValide = False

while dateEntreeValide != True:
    
    dateEntree = str(input("Entrez la date du départ de l'hôtel (jj/mm/aaaa) : ")) 
    
    validiteDeLaDate = VerificationValiditeDate(dateEntree)
    print(validiteDeLaDate[0])
    
    if validiteDeLaDate[1] == True:
        dateEntreeValide = True    

#Test de la validite de la date du depart : 
dateSortieValide = False

while dateSortieValide != True:
    
    dateSortie = str(input("Entrez la date du départ de l'hôtel (jj/mm/aaaa) : ")) 
    
    validiteDeLaDate = VerificationValiditeDate(dateSortie)
    print(validiteDeLaDate[0])
    
    if validiteDeLaDate[1] == True:
        dateSortieValide = True

# ----- Calcul du nombre de jours passes a l'hotel ----- #

dateEnCours = dateEntree
nbJoursSejour = 0

while dateEnCours != dateSortie:
    
    jourEnCours = int(dateEnCours[0:2])
    moisEnCours = int(dateEnCours[3:5])
    anneeEnCours = int(dateEnCours[6:10])
    
    jourMax = JourMaxDuMois(moisEnCours, anneeEnCours)
    
    if jourEnCours < jourMax:
        
        if jourEnCours + 1 < 10:
            dateEnCours = dateEnCours.replace("0" + str(jourEnCours), "0" + str(jourEnCours + 1), 1)
        elif jourEnCours + 1 == 10:
            dateEnCours = dateEnCours.replace("0" + str(jourEnCours), str(jourEnCours + 1), 1)
        else:
            dateEnCours = dateEnCours.replace(str(jourEnCours), str(jourEnCours + 1), 1)
    
    else:
        
        if moisEnCours < 12:
            
            if moisEnCours + 1 < 10:
                dateEnCours = dateEnCours.replace("0" + str(moisEnCours), "0" + str(moisEnCours + 1), 1)
                dateEnCours = dateEnCours.replace(str(jourEnCours), "01", 1)
            elif moisEnCours + 1 == 10:
                dateEnCours = dateEnCours.replace("0" + str(moisEnCours), str(moisEnCours + 1), 1)
                dateEnCours = dateEnCours.replace(str(jourEnCours), "01", 1)                
            else:
                dateEnCours = dateEnCours.replace(str(moisEnCours), str(moisEnCours + 1), 1)
                dateEnCours = dateEnCours.replace(str(jourEnCours), "01", 1)
        
        else:
            dateEnCours = dateEnCours.replace(str(anneeEnCours), str(anneeEnCours + 1), 1)
            dateEnCours = dateEnCours.replace(str(moisEnCours), "01", 1)
            dateEnCours = dateEnCours.replace(str(jourEnCours), "01", 1)
    
    nbJoursSejour += 1
    
print(nbJoursSejour)
print(f"Vous devez {nbJoursSejour * prix} €")
    
    
    
    
    
    
    
    
    
    
    
    
    










 
    