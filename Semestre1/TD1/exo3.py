''' Exercice 3 '''

from math import ceil

oeufAProduire = int(input("Combien d'oeufs voulez-vous produire ? : "))
nombreDeJours = int(input("En combien de jours ? : "))
moyenneOeufParPoule = 14/5/4
print("En moyenne, une poule pond 0.7 oeufs par jour.")
print("Il vous faut", ceil(oeufAProduire / moyenneOeufParPoule / nombreDeJours) ,"poules pour avoir", oeufAProduire, "oeufs en", nombreDeJours, "jours.")