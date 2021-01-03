# coding: utf-8

'''
Fichier contenant toutes les fonctions necessaires au fonctionnement du jeu
'''

# --- Imports --- #
#from turtle import setheading, update, textinput
from turtle import *
from random import choice, randrange

from drawBottle import draw_bottle, draw_broken_bottle
from drawingFunctions import va, draw_rectangle
from bullet import shoot_bullet

#Definition des fonctions

def draw_list_bottle(quilles, length, height, factor):
    # 400*factor est la longueur du banc
    # 400*factor/24 est la largeur du banc
	startCoordinates = [length/20, -height/4 + 400*factor/24]
	x = startCoordinates[0]
	y = startCoordinates[1]
    
    #Erase previous bottles
	va(x,y)
	setheading(0)
	draw_rectangle(400*factor,100*factor,"SandyBrown")
    
    #Draw the bottles
	x += 400*factor/len(quilles)/4     #Pour centrer les bouteilles
	for loop in range(len(quilles)):
		if quilles[loop] == "|":
			setheading(0)
			draw_bottle(x, y, factor/4)

		else:
			setheading(0)
			draw_broken_bottle(x,y, factor/4, "SandyBrown")

		update()

		x += (400*factor/len(quilles))

def afficheQuilles(q, n, length, height, factor):
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
        
    #Message affich�
    print("Voici les quilles, il y a",nbLignes,"lignes")
    print(quilles)

    #Dessin des quilles
    draw_list_bottle(quilles, length, height, factor)

    update()
   	
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
            i = int(textinput(" ","Quelle ligne? "))-1 
            
            if 0 <= i < len(q):
                saisieValide = True
            else:
                print("Verifiez que vous avez bien ecrit un nombre compris entre 1 et ", len(q), ".")
            
        except:
            print("La valeur que vous avez rentre n'est pas valide.")
    
    #L'utilisateur choisit où il veut jouer
    saisieValide = False
    while saisieValide == False: #Boucle fonctionnant tant que l'utilisateur n'a pas fait un choix valide

        p = textinput(" ","Gauche, Milieu ou Droite ? (G ,M ou D) ")

        if p not in ["G", "M", "D"]:
            print("Verifiez que vous avez bien ecrit l'un des caracteres suivant : 'G | M | D'.")
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
        nbDeQuilles += L[1] - L[0] + 1
    
    return nbDeQuilles