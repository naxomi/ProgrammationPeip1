''' Exercice 1 '''

# print("Quotient de 3124 par 6 : " + str(3124 // 6))
# print("Reste de 3124 par 6 : " + str(3124  % 6))
# print("Type de 123*(1.56 -3) :", type(123*(1.56 - 3)))
# print("Valeur de 123*(1.56 -3) :", 123*(1.56 - 3))

# ''' Exercice 2 '''

# v1 = int(input("Donnez l'entier à diviser : "))
# v2 = int(input("Donnez le diviseur : "))
# print("Division euclidienne de {0} par {1} : ".format(v1,v2))
# print(v1, "=", v1 // v2, "*", v2, "+", v1 % v2)

''' Exercice 3 '''

# from math import ceil

# oeufAProduire = int(input("Combien d'oeufs voulez-vous produire ? : "))
# nombreDeJours = int(input("En combien de jours ? : "))
# moyenneOeufParPoule = 14/5/4
# print("En moyenne, une poule pond 0.7 oeufs par jour.")
# print("Il vous faut", ceil(oeufAProduire / moyenneOeufParPoule / nombreDeJours) ,"poules pour avoir", oeufAProduire, "oeufs en", nombreDeJours, "jours.")

''' Exercice 4 '''

''' Version "legit" '''

# initiales = str(input("Donnez vos initiales : "))
# line = int(input("Nombre de lignes : "))
# column = int(input("Nombre de columns : "))

# #Create the first and last lines at the same time because they are the same
# firstAndLastLines = (initiales + " ") * (column - 1) + initiales
# #Create one line from in between the ends
# inBetweenLine = (initiales + (" " * (column - 1) + (" " * (column - 2)) * len(initiales)) + initiales)

# print(firstAndLastLines)
# print((inBetweenLine + "\n") * (line - 3) + inBetweenLine) 
# print(firstAndLastLines)

''' Version "tricheur" '''

# initiales = str(input("Donnez vos initiales : "))
# line = int(input("Nombre de lignes : "))
# column = int(input("Nombre de colonnes : "))

# for loop in range(line):
#     if loop % (line - 1) == 0:
#         print((initiales + " ") * (column - 1) + initiales)
#     else:
#         print(initiales + (" " * (column - 1) + (" " * (column - 2)) * len(initiales)) + initiales)

''' Exercice 5 '''

#print(1<3 or (5<2 and 8>1))

''' Problème '''

distanceParcourue = float(input("Distance parcourure (km) : "))
tempsParcouru = int(input("Temps parcouru (min) : "))
distanceRestante = int(input("Distance restante (km) : "))
heureArret = int(input("Heure arrêt (hh) : "))
minuteArret = int(input("Minute arrêt (mm) : "))

vitesseMoyenne = distanceParcourue / ( tempsParcouru / 60 )
tempsRestant = (distanceRestante / vitesseMoyenne) * 60

sommeMinutesArret = heureArret * 60 + minuteArret
sommeMinutesArrivee = sommeMinutesArret + tempsRestant

heureArrivee = sommeMinutesArrivee // 60
minuteArrivee = sommeMinutesArrivee % 60

print("Heure de départ : {0}h{1}".format(heureArret, minuteArret))
print("Distance parcourue : {0} kilomètres.".format(distanceParcourue))
print("Temps mis : {0} minutes.".format(tempsParcouru))
print("Vous avez parcouru {0} kilomètres en {1} minutes.".format(distanceParcourue, tempsParcouru))
print("Vous avez roulé à la vitesse moyenne de {0} km/h".format(vitesseMoyenne))
print("En roulant à cette vitesse, pour faire les {0} km restants, il vous faudra {1} minutes".format(distanceRestante, tempsRestant))
print("Heure d'arrivée : {0}h{1}".format(int(heureArrivee), int(minuteArrivee)))








