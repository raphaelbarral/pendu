import random
from unidecode import unidecode


def charger_fichier(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print('Entrez un nom de fichier valide ou n\'entrez rien.')
        return False
    else:
        with f:
            mots = f.read().split('\n')
    return mots


def verifier_lettre(lettre, mot, lettres_trouvees):
    succes = False
    i = 0
    for char in mot:
        if char == lettre:
            succes = True
            lettres_trouvees[i] = True
        i += 1
    return succes


def donner_indice(mot, lettres_trouvees):
    lettres_restantes = [mot[i] for i in range(len(mot)) if not lettres_trouvees[i]]
    indice = random.choice(lettres_restantes)
    verifier_lettre(indice, mot, lettres_trouvees)
    print(f'La lettre {indice} vous est donnée comme indice.')


def choisir_mot(mots):
    return unidecode(random.choice(mots))


def main():
    while not (mots := charger_fichier(input('Entrez un nom de fichier pour le charger, sinon laissez vide : ') or 'mots_pendu.txt')):
        continue

    jouer = True
    while jouer:
        nombre_de_chances = 6
        mot = choisir_mot(mots)
        print(mot)
        lettres_trouvees = [False] * len(mot)

        gagner = False
        while nombre_de_chances:
            print('\n' + ''.join(list(map(lambda a, b: b if a else '_', lettres_trouvees, mot))))
            print(f'Nombre de chances restantes : {nombre_de_chances}')

            while not (lettre := unidecode(input('Veuillez entrer une lettre : ')[0])).isalpha():
                continue

            if not verifier_lettre(lettre, mot, lettres_trouvees):
                nombre_de_chances -= 1
                print('La lettre n\'est pas dans le mot')
                if nombre_de_chances == 1:
                    donner_indice(mot, lettres_trouvees)
            else:
                print('La lettre est bien dans le mot')

            if gagner := all(lettres_trouvees):
                break

        if gagner:
            print(f'Bien joué vous avez gagné\nLe mot était bien {mot}.')
        else:
            print(f'La partie est perdu\nLe mot était {mot}.')

        if input('Voulez-vous rejouez? (y/n) ').lower() == 'n':
            jouer = False


main()