''' --- Exemple 1 --- '''

print(' --- Exemple 1 --- ')

prix = int(input("prix ? "))   #1
if prix > 1000 :          #2 instruction if
    print("trop cher")
    print("j'achète pas")
print("fin des achats")   #3

''' --- Exercice 1 --- '''

print(' --- Exercice 1 --- ')

prix = int(input("Prix : "))
if prix <= 1000:
    print("J'achète !")
    if prix < 100:
        print("C'est donné : ")
    elif prix >= 100 and prix <= 1000:
        print("Même si c'est pas donné")

print("Fin des achats")

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

''' --- Problème --- '''

''' Problème 1 '''

print(' Problème 1 ')

mois = int(input("Quel mois ? (entre 1 et 12) : "))
annee = int(input("Quelle année ? : "))

if mois == 2:
    if annee % 4 == 0 or annee % 100 == 0:
        print(f"Il y a 29 jours dans le mois {mois}")
    else:
        print(f"Il y a 28 jours dans le mois {mois}")
    
elif mois % 2 == 0 and mois < 8:
    print(f"Il y a 30 jours dans le mois {mois}.")
elif mois % 2 != 0 and mois < 8:
    print(f"Il y a 31 jours dans le mois {mois}.")
    
elif mois % 2 == 0 and mois >= 8:
    print(f"Il y a 31 jours dans le mois {mois}.")
elif mois % 2 != 0 and mois >= 8:
    print(f"Il y a 30 jours dans le mois {mois}.")
        
''' Problème 2 '''

print(' Problème 2 ')

age = 85

fumer = str(input("Fumez-vous ? (yes/no) : "))
pressionSanguine = int(input("Quelle est votre pression sanguine ? (mm) : "))
bleuet = int(input("Combien de kilos de bleuets mangez-vous par an ? (kg) : "))

if fumer == "yes":
    age -= 10
if pressionSanguine > 120:
    age -= 2 * (((pressionSanguine-120)%20) + 1 ) 
if bleuet >= 2:
    age += 2
    
print(age)



















