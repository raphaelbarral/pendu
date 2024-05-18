import random
from unidecode import unidecode

with open('mots_pendu.txt', 'r') as f:
    mots = f.read().split('\n')


def verifier_lettre(lettre, mot):
    global lettres_trouvees
    succes = False
    i = 0
    for char in mot:
        if char == lettre:
            succes = True
            lettres_trouvees[i] = True
        i += 1

    return succes


def choisir_mot(mots):
    return random.choice(mots)


jouer = True
while jouer:
    nombre_de_chances = 6
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
        print(f'La partie est perdu\nLe mot était {mot}.')

    if input('Voulez-vous rejouez? (y/n) ').lower() == 'n':
        jouer = False
