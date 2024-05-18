import random
from unidecode import unidecode

nombre_de_chances = 6

mots = ['chien', 'chat', 'rat', 'renard', 'wapiti', 'kangourou']


def verifier_lettre(lettre, mot):
    global lettres_trouvees
    succes = False
    i = 0
    for l in mot:
        if l == lettre:
            succes = True
            lettres_trouvees[i] = True
        i += 1

    return succes


def choisir_mot(mots):
    return random.choice(mots)


jouer = True
while jouer:
    mot = choisir_mot(mots)
    taille_mot = len(mot)
    lettres_trouvees = [False] * taille_mot

    gagner = False
    while nombre_de_chances:
        print('\n' + ''.join(list(map(lambda a, b: b if a else '_', lettres_trouvees, mot))))
        print(f'Nombre de chances restantes : {nombre_de_chances}')

        while not (lettre := unidecode(input('Veuillez entrer une lettre : ')[0])).isalpha():
            continue

        if not verifier_lettre(lettre, mot):
            nombre_de_chances -= 1
            print('La lettre n\'est pas dans le mot')
        else:
            print('La lettre est bien dans le mot')

        if gagner := all(lettres_trouvees):
            break

    if gagner:
        print('Bien joué vous avez gagné')
    else:
        print('La partie est perdu')

    if input('Voulez vous rejouez? (y/n) ').lower() == 'n':
        jouer = False
