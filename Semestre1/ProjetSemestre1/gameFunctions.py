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
from bullet import shoot_bullet, draw_bullet

def draw_list_bottle(quilles, xForBench, yForBench, lengthBench, bottleAlreadyShot, factor):

	# --- Initiate the turtle for the bullet --- #

	bulletTurtle = Turtle()
	bulletTurtle.hideturtle()
	bulletTurtle.setundobuffer(0)

	# --- Initiate the coordinates --- #
	startCoordinates = [xForBench, yForBench + lengthBench/24]
	x = startCoordinates[0]
	y = startCoordinates[1]
	
	# --- Erase previous bottles --- #
	va(x,y)
	setheading(0)
	draw_rectangle(lengthBench, 195*factor, "SandyBrown")
	
	# --- Draw the bottles --- #
	numberOfBottle = len(quilles)

	widthBottleOriginal = 90 * factor
	factorSizeBottle = 0.55 - (numberOfBottle-5)*0.03

	widthBottleModified = widthBottleOriginal * factorSizeBottle
	intervalBetweenBottle = (lengthBench - widthBottleModified * numberOfBottle) / (numberOfBottle + 1)

	x += intervalBetweenBottle

	for loop in range(numberOfBottle):
		if quilles[loop] == "|":
			setheading(0)
			draw_bottle(x, y, factorSizeBottle)

		else:
			setheading(0)
			
			if loop not in bottleAlreadyShot:
				draw_bottle(x, y, factorSizeBottle)

				shoot_bullet(window_width() / 4, -window_height() / 1.5, x+widthBottleModified/2, y+widthBottleModified/2, factor, factorSizeBottle, bulletTurtle)

				bottleAlreadyShot.append(loop)

				draw_broken_bottle(x, y, factorSizeBottle, True, "SandyBrown")

			else:
				draw_broken_bottle(x, y, factorSizeBottle, False, "SandyBrown")

		update()
		
		x += intervalBetweenBottle + widthBottleModified

	# --- #

	return bottleAlreadyShot

def afficheQuilles(q, n, xForBench, yForBench, lengthBench, bottleAlreadyShot, factor):
	#q est la liste contenant les diffÃ©rentes lignes ([deb,fin])
	#n est le nombre de quilles de depart
	
	#Variable stockant la representation des quilles (au debut pas de quilles)
	quilles = "."*n
	
	for i in range(len(q)):
		deb = q[i][0]         #Rang du debut de la ligne
		fin = q[i][1]+1       #Rang de la fin de la ligne
		#On place des quilles uniquement entre les deux rangs spÃ©cifiÃ©s
		quilles = quilles[0:deb]+"|"*(fin-deb)+quilles[fin:n]
	
	if quilles.count("|") == 0:
		nbLignes = 0
	else:
		nbLignes = len(q)
		
	#Message affiché
	print("Voici les quilles, il y a",nbLignes,"lignes")
	print(quilles)

	#Dessin des quilles
	bottleAlreadyShot = draw_list_bottle(quilles, xForBench, yForBench, lengthBench, bottleAlreadyShot, factor)

	update()

	return bottleAlreadyShot
	
def ordiJoue(q):
	#q est la liste contenant les diffÃ©rentes lignes ([deb,fin])
	
	i = randrange(0,len(q))     #Valeur alÃ©atoire entiÃ¨re dans [0,len(q)[
	p = choice(["G","M","D"])   #Choix alÃ©atoire entre : G, M et D
	
	return str(i)+":"+p

def joueurJoue(q):
	#q est la liste contenant les diffÃ©rentes lignes ([deb,fin])
	
	#L'utilisateur choisit la ligne sur laquelle il souhaite jouer
	saisieValide = False
	while saisieValide == False: #Boucle fonctionnant tant que l'utilisateur n'a pas fait un choix valide
		
		try: #Permet de gerer les erreurs telles que ValueError pouvant venir de l'input
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
			
	#La fonction renvoie les paramÃ¨tres choisis par l'utilisateur 
	return str(i) + ":" + p

	
def jouerMilieu(c,q):
	#c est le choix de la forme i:p
	#q est la liste contenant les diffÃ©rentes lignes ([deb,fin])

	ligne = int(c.split(":")[0]) - 1      #Ligne sur laquelle on va jouer
	deb = q[ligne][0]                   #Rang du dÃ©but de la ligne
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
	#q est la liste contenant les diffÃ©rentes lignes ([deb,fin])
	
	ligne = int(c.split(":")[0])-1      #Ligne sur laquelle on va jouer
	position = c[2]                     #Position du tir (D ou G)
	
	if position=="D":
		q[ligne][1] = q[ligne][1]-1
	else:
		q[ligne][0] = q[ligne][0]+1
	return

def jouer(c,q):
	#c est le choix de la forme i:p
	#q est la liste contenant les diffÃ©rentes lignes ([deb,fin])
	
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