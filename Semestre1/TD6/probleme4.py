#!/usr/bin/env python
#-*- coding: utf-8 -*- 

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