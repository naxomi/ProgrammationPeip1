#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        
    if numeroCategorie <= len(listeDesCategories):
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
    
    if numeroChanteur <= len(listeDesChanteurs):
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
        
        if nbExemplaireCd >= nbExemplaireCommande:
    
            validiteChoixUtilisateur = True    
        
            if isInPanier(panier, informationCdCommande):
                for index, cdDansPanier in enumerate(panier):
                    if cdDansPanier[0:4] == informationCdCommande:        
                        panier[index][4] += nbExemplaireCommande
            else:
                panier.append(stockDeCD[realNumeroCdCommande][:])
                panier[-1][4] = nbExemplaireCommande
                        
                stockDeCD[realNumeroCdCommande][4] = nbExemplaireCd - nbExemplaireCommande
    
            print(f"Le CD n°{numeroCdCommande} a été ajouté à votre panier en {nbExemplaireCommande} exemplaires.\n")
            
        else:
            print(f"Il ne reste que {nbExemplaireCd} exemplaires de ce CD alors que vous avez essayé d'en commander {nbExemplaireCommande}.\n")
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
    
        if nbExemplaireCdPanier >= nbExemplaireSupprime:
        
            validiteChoixUtilisateur = True
                    
            if isInStock(stockDeCD, informationCdSupprime):
                for index, cdDansStock in enumerate(stockDeCD):
                    if cdDansStock[0:4] == informationCdSupprime:            
                        stockDeCD[index][4] += nbExemplaireSupprime
                        
                else:
                    stockDeCD.append(panier[realNumeroCdSupprime][:])
                        
                panier[realNumeroCdSupprime][4] = nbExemplaireCdPanier - nbExemplaireSupprime
                
                print(f"{nbExemplaireSupprime} exemplaires du CD n°{numeroCdSupprime} ont été supprimés de votre panier.\n")
            
            else:
                print(f"Il ne reste que {nbExemplaireCdPanier} exemplaires de ce CD alors que vous avez essayé d'en supprimer {nbExemplaireSupprime}.\n")
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


