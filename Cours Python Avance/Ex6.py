liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]

nom_a_chercher = "Julie"
nouveau_nom = "Julien"

liste = [x.replace(nom_a_chercher, nouveau_nom) for x in liste]
print(liste)

####
employes = {}

liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]

i = 1

for element in liste:
    if not str(element).isdigit():
        employes["id-{:02d}".format(i)] = element
        i += 1

####

# Longueur maximale à afficher
n = 8
symbole = '*'
l =['']
l = [l[i-1][:len(l[i-1]-1)] if i>n else symbole for i in range(0,n*2-1)]

import random

liste_random = [str(random.choice(range(2))) for _ in range(8)]


def join(*args):
    resultat = ""

    separateur = args[0]
    elements = args[1:]

    for element in elements:
        resultat += element + separateur

    return resultat[:-1]

