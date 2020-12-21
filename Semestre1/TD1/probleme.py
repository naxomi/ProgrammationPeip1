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