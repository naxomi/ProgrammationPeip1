#!/usr/bin/env python
#-*- coding: utf-8 -*- 

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