phrase = 'Phrase en camel case'

phrase2=''
compteur = False

for i, valeur in enumerate(phrase.lower()):
    if(valeur == ' '):
        compteur = True
    else:
        if(compteur == True):
            phrase2 += valeur.upper()
            compteur = False
        else:
            phrase2 += valeur


print(phrase2)

phrase = 'Phrase en camel case'
mots = phrase.lower().split(' ')
phrase = mots[0]
for mot in mots[1:]:
    phrase += mot.capitalize()
print(phrase)