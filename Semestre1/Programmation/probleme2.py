#!/usr/bin/env python
#-*- coding: utf-8 -*- 

''' ----- Problème 2 ----- '''

# ----- Definition des fonctions utilisees plus tard dans le programme ----- #

def AnneeValide(annee):
    if annee >= 1600 and annee <= 2018:
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
print("")

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
    
print(f"Vous devez {nbJoursSejour * prix} €")