#!/usr/bin/env python
# coding: utf-8

# In[1]:

from drawingFunctions import *
from drawBottle import draw_bottle, test_sizes_bottle
from drawSaloon import draw_saloon, draw_many_saloons

from time import sleep
from turtle import *

hideturtle()
tracer(False)
colormode(255)

height = 1080
width = 1920

screen = Screen()
screen.setup(width, height)

#Groupe 1 : Jaime Alba Pastor et Raphael Anjou

from random import choice, randrange

#Definition des fonctions

def afficheQuilles(q,n):
    #q est la liste contenant les différentes lignes ([deb,fin])
    #n est le nombre de quilles de depart
    
    #Variable stockant la representation des quilles (au debut pas de quilles)
    quilles = "."*n
    
    for i in range(len(q)):
        deb = q[i][0]         #Rang du debut de la ligne
        fin = q[i][1]+1       #Rang de la fin de la ligne
        #On place des quilles uniquement entre les deux rangs spécifiés
        quilles = quilles[0:deb]+"|"*(fin-deb)+quilles[fin:n]
    
    if quilles.count("|") == 0:
        nbLignes = 0
    else:
        nbLignes = len(q)
        
    #Message affiché
    print("Voici les quilles, il y a",nbLignes,"lignes")
    print(quilles)

    clear()
    draw_list_bottle(quilles)
    update()
    
    return
 
def ordiJoue(q):
    #q est la liste contenant les différentes lignes ([deb,fin])
    
    i = randrange(0,len(q))     #Valeur aléatoire entière dans [0,len(q)[
    p = choice(["G","M","D"])   #Choix aléatoire entre : G, M et D
    
    return str(i)+":"+p

def joueurJoue(q):
    #q est la liste contenant les différentes lignes ([deb,fin])
    
    #L'utilisateur choisit la ligne sur laquelle il souhaite jouer
    saisieValide = False
    while saisieValide == False: #Boucle fonctionnant tant que l'utilisateur n'a pas fait un choix valide
        
        try: #Permet de gérer les erreurs telles que ValueError pouvant venir de l'input
            i = int(input("Quelle ligne? "))-1 
            
            if 0 <= i < len(q):
                saisieValide = True
            else:
                print("Vérifiez que vous avez bien écrit un nombre compris entre 1 et ", len(q), ".")
            
        except:
            print("La valeur que vous avez rentré n'est pas valide.")
    
    #L'utilisateur choisit où il veut jouer
    saisieValide = False
    while saisieValide == False: #Boucle fonctionnant tant que l'utilisateur n'a pas fait un choix valide

        p = str(input("Gauche, Milieu ou Droite ? (G ,M ou D) "))

        if p not in ["G", "M", "D"]:
            print("Vérifiez que vous avez bien écrit l'un des caractères suivant : 'G | M | D'.")
        else:
            saisieValide = True
            
    #La fonction renvoie les paramètres choisis par l'utilisateur 
    return str(i) + ":" + p

    
def jouerMilieu(c,q):
    #c est le choix de la forme i:p
    #q est la liste contenant les différentes lignes ([deb,fin])

    ligne = int(c.split(":")[0]) - 1      #Ligne sur laquelle on va jouer
    deb = q[ligne][0]                   #Rang du début de la ligne
    fin = q[ligne][1]                   #Rang de la fin de la ligne

    #Deux cas possibles :
    if (deb + fin) % 2 == 1:        #Nombre pair de quilles
        ip = 2 
    else:                       #Nombre impair de quilles
        ip = 1

    q[ligne][1] = ((deb + fin) // 2) - 1
    q.insert(ligne+1, [((deb+fin)//2)+ip,fin])

    return

def jouerCote(c,q):
    #c est le choix de la forme i:p
    #q est la liste contenant les différentes lignes ([deb,fin])
    
    ligne = int(c.split(":")[0])-1      #Ligne sur laquelle on va jouer
    position = c[2]                     #Position du tir (D ou G)
    
    if position=="D":
        q[ligne][1] = q[ligne][1]-1
    else:
        q[ligne][0] = q[ligne][0]+1
    return

def jouer(c,q):
    #c est le choix de la forme i:p
    #q est la liste contenant les différentes lignes ([deb,fin])
    
    if c.split(":")[1] == "M":
        jouerMilieu(c, q)
    else:
        jouerCote(c, q)
    
    #On verifie si une ligne doit etre supprimee
    for L in q:
        if L[1]==L[0]-1:
            q.remove(L)
            
    return

def compterQuilles(q):
    #q est la liste content les differentes lignes ([deb,fin])
    
    nbDeQuilles = 0
    for L in q:
        nbDeQuilles = L[1] - L[0] + 1
    
    return nbDeQuilles

#        - MOTEUR DU JEU -

def draw_list_bottle(quilles):
    x = -575
    y = -200

    for loop in range(len(quilles)):
        if quilles[loop] == "|":
            setheading(0)
            draw_bottle(x, y, 1)
            update()

        else:
            setheading(0)
            va(x, y)
            draw_rectangle(90, 200, "red")
            update()

        x += 125

nbInitial = randrange(4,10)                 #Tirer un nombre aléatoire de quilles
nbDeQuilles = nbInitial

quilles=[[0,nbInitial-1]]
afficheQuilles(quilles, nbInitial)

gagnant = False

while not gagnant:                              #Tant qu'il n'y a pas de gagnant :
    
    #Faire jouer le joueur
    choix = joueurJoue(quilles)
    jouer(choix, quilles)
        
    nbDeQuilles = compterQuilles(quilles)            #Mettre à jour le nombre de quilles
    
    afficheQuilles(quilles, nbInitial)      #Afficher les quilles
    
    if nbDeQuilles == 0:                           #S'il n'y a plus de quilles : le joueur a gagné
        print("Tu as gagné!")
        sleep(5)    
        gagnant = True
    
    else:
        sleep(1)                                   #S'il reste des quilles :   
        print("Le robot joue !!!!!")
        jouer(ordiJoue(quilles),quilles)    #Faire jouer l'ordinateur
        
        nbDeQuilles = compterQuilles(quilles)        #Mettre à jour le nombre de quilles
              
        afficheQuilles(quilles, nbInitial)  #Afficher les quilles
        
        if nbDeQuilles == 0:                        #S'il n'y a plus d'allumettes, l'ordinateur a gagné                      
            print("Tu as perdu!") 
            sleep(5)
            gagnant = True
        
        

