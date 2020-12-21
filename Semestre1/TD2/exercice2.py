''' --- Exercice 2 --- '''
  
print(' --- Exercice 2 --- ')

print("Location de vélos !")
      
duration = int(input("Combien d'heures souhaitez-vous louer ? : "))
subscription = str(input("Avez-vous un abonnement ? (oui/non) : "))

if duration <= 2:
    price = 3 * duration
elif duration > 2 and duration <= 8:
    price = 3 * 2 + (duration - 2) * 5
else:
    print("Error !!!!!!")
    
if subscription == "non":
    price += 2
    
print(f"Le montant prévisionnel pour {duration} heures de location est de {price} euros.")