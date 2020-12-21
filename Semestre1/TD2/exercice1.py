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