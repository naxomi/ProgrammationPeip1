#!/usr/bin/env python
#-*- coding: utf-8 -*- 

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