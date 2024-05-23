import random  #Pour pouvoir utiliser random.choice
from unicodedata import normalize  #Pour pouvoir gérer les accents


def charger_fichier(filename):  #Cette fonction charge le fichier filename s'il existe et retourne une liste de mots
    try:
        f = open(filename, 'r')
    except FileNotFoundError:  #gere le cas ou le fichier n'existe pas
        print('Entrez un nom de fichier valide ou n\'entrez rien.')
        return False
    else:
        with f:
            mots = f.read().split('\n')  #transforme la chaine de caracteres en liste de mots
    return mots


def verifier_lettre(lettre, mot,
                    lettres_trouvees):  #verifie qu'une lettre se trouve dans le mot caché et renvoie True s une lettre est trouvée
    succes = False
    i = 0
    for char in mot:  #verifie chaque lettre du mot
        if char == lettre:
            succes = True
            lettres_trouvees[i] = True  #actualise la liste contenant si la position est trouvée
        i += 1
    return succes  #retourne True si une lettre a été trouvée


def donner_indice(mot, lettres_trouvees):                   #cette foncction dévoile une lettre du mot
    lettres_restantes = [mot[i] for i in range(len(mot)) if
                         not lettres_trouvees[i]]           #liste des lettres encore non trouvées
    indice = random.choice(lettres_restantes)               #choisie au hasard une des lettre non découvertes
    verifier_lettre(indice, mot, lettres_trouvees)          #utilise la fonction verifier_lettre pour la découvrir
    print(f'La lettre {indice} vous est donnée comme indice.')


def choisir_mot(mots):  #choisi un mot parmi une liste de mots et le retourne sans accent
    return normalize('NFD', random.choice(mots)).encode('ASCII', 'ignore').decode('utf8')


def main():  #fonciton principa du programme
    while not (mots := charger_fichier(input('Entrez un nom de fichier pour le charger, sinon laissez vide : ') or 'mots_pendu.txt')):
        continue    #demande à l'utilisateur d'entrer un nom de fichier si l'utilisateur n'entre rien le programme
                    #charge une liste par défaut

    jouer = True  #variable permettant d'arreter le programme si elle vaut False
    while jouer:
        nombre_de_chances = 6                   #nombre de chances initial
        mot = choisir_mot(mots)                 #choisi un mot parmi la liste de mots
        lettres_trouvees = [False] * len(mot)   #initialise la liste qui mémorise la position des lettre trouvée à False

        while nombre_de_chances:  #tant qu'il reste une chance
            print('\n' + ''.join(list(map(lambda a, b: b if a else '_', lettres_trouvees,
                                          mot))))  #affiche le mot a deviant avec les lettres cachées
            print(f'Nombre de chances restantes : {nombre_de_chances}')

            while not (
                    lettre := normalize('NFD', input('Veuillez entrer une lettre : ')).encode('ASCII', 'ignore').decode(
                        'utf8')).isalpha():
                continue    #demande une lettre à l'utilisateur et enleve les accents
                            #continue de demander tant qu'il n'entre pas une chaine de caractere ou un nombre

            lettre = lettre[0]  #si la chaine de caractere contient plus d'un caractère elle prend le premier

            if not verifier_lettre(lettre, mot, lettres_trouvees):
                nombre_de_chances -= 1  #si la lettre n'est pas valide, enlever une chance
                print('La lettre n\'est pas dans le mot')
                if nombre_de_chances == 1:  #si c'est la derniere chance, donner un indice
                    donner_indice(mot, lettres_trouvees)
            else:
                print('La lettre est bien dans le mot')

            if gagner := all(lettres_trouvees):  #si tout les lettres sont trouvé sortir de la boucle
                break

        if gagner:
            print(f'Bien joué vous avez gagné\nLe mot était bien {mot}.')
        else:
            print(f'La partie est perdu\nLe mot était {mot}.')

        if input(
                'Voulez-vous rejouez? (y/n) ').lower() == 'n':  #si l'utilisateur ne veut pas rejouer jouer prend la valeur False
            jouer = False


main()  #appeler la fonction principale
