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