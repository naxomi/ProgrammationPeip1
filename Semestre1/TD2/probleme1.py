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