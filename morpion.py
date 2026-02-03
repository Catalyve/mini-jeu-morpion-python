"""
Morpion (Tic-Tac-Toe)
---------------------

Implémentation complète du jeu du morpion en console, avec :
- mode 2 joueurs
- mode contre robot aléatoire
- mode contre robot stratégique (blocage et coups gagnants)
- limite de temps pour les tours du joueur

"""

import random
import time


def initialiser_tableau():
    """
    Initialise un tableau 3x3 vide.

    Retour :
        list[list[str]] : tableau rempli de '-'.
    """
    return [['-' for _ in range(3)] for _ in range(3)]


def afficher_tableau(tableau):
    """
    Affiche le tableau sous une forme lisible.

    Paramètre :
        tableau (list[list[str]]): tableau à afficher.
    """
    for ligne in tableau:
        print(' | '.join(ligne))
    print()


def jouer_tour_humain_temps(tableau, joueur, temps_limite):
    """
    Permet au joueur humain de jouer dans un délai donné.
    Si le temps est dépassé, un coup aléatoire est joué automatiquement.

    Paramètres :
        tableau (list[list[str]])
        joueur (str) : 'X' ou 'O'
        temps_limite (int) : secondes
    """
    debut = time.time()

    while True:
        print(f"C'est au tour de {joueur} (temps restant : {temps_limite}s)")
        try:
            ligne = int(input("Ligne (0-2) : "))
            colonne = int(input("Colonne (0-2) : "))

            if time.time() - debut > temps_limite:
                print("Temps écoulé. Coup automatique.")
                jouer_tour_ordinateur_aleatoire(tableau, joueur)
                return

            if 0 <= ligne < 3 and 0 <= colonne < 3 and tableau[ligne][colonne] == '-':
                tableau[ligne][colonne] = joueur
                return

            print("Entrée invalide.")
        except ValueError:
            print("Veuillez entrer des chiffres entre 0 et 2.")


def jouer_tour_ordinateur_aleatoire(tableau, joueur):
    """
    Joue un coup aléatoire valide.

    Paramètres :
        tableau (list[list[str]])
        joueur (str)
    """
    while True:
        ligne = random.randint(0, 2)
        colonne = random.randint(0, 2)
        if tableau[ligne][colonne] == '-':
            tableau[ligne][colonne] = joueur
            return


def jouer_tour_ordinateur_strategique(tableau, joueur):
    """
    Robot basique :
    - joue un coup gagnant si possible
    - bloque un coup gagnant adverse
    - sinon joue aléatoirement

    Paramètres :
        tableau (list[list[str]])
        joueur (str)
    """
    adversaire = 'O' if joueur == 'X' else 'X'

    for i in range(3):
        for j in range(3):
            if tableau[i][j] == '-':
                tableau[i][j] = joueur
                if verifier_victoire(tableau)[0]:
                    return
                tableau[i][j] = '-'

    for i in range(3):
        for j in range(3):
            if tableau[i][j] == '-':
                tableau[i][j] = adversaire
                if verifier_victoire(tableau)[0]:
                    tableau[i][j] = joueur
                    return
                tableau[i][j] = '-'

    jouer_tour_ordinateur_aleatoire(tableau, joueur)


def verifier_victoire(tableau):
    """
    Vérifie si le jeu est terminé.

    Paramètre :
        tableau (list[list[str]])

    Retour :
        tuple(bool, str) :
            bool = True si victoire ou match nul
            str  = gagnant ('X','O') ou 'NUL'
    """
    for i in range(3):
        if tableau[i][0] == tableau[i][1] == tableau[i][2] != '-':
            return True, tableau[i][0]
        if tableau[0][i] == tableau[1][i] == tableau[2][i] != '-':
            return True, tableau[0][i]

    if tableau[0][0] == tableau[1][1] == tableau[2][2] != '-':
        return True, tableau[0][0]

    if tableau[0][2] == tableau[1][1] == tableau[2][0] != '-':
        return True, tableau[0][2]

    for ligne in tableau:
        if '-' in ligne:
            return False, ''

    return True, 'NUL'


def morpion():
    """
    Fonction principale du jeu.
    Gère la sélection du mode, l'alternance des joueurs,
    l'affichage du plateau et la détection de victoire.
    """
    print("=== MORPION ===")
    mode = input("Modes : \n1) Deux joueurs  \n2) IA aléatoire  \n3) IA stratégique\n - ")

    tableau = initialiser_tableau()
    afficher_tableau(tableau)

    joueur = 'X'
    temps_limite = 10 

    while True:
        if mode == '1':
            jouer_tour_humain_temps(tableau, joueur, temps_limite)

        elif mode == '2':
            if joueur == 'X':
                jouer_tour_humain_temps(tableau, joueur, temps_limite)
            else:
                jouer_tour_ordinateur_aleatoire(tableau, joueur)

        elif mode == '3':
            if joueur == 'X':
                jouer_tour_humain_temps(tableau, joueur, temps_limite)
            else:
                jouer_tour_ordinateur_strategique(tableau, joueur)

        else:
            print("Mode invalide.")
            return

        afficher_tableau(tableau)

        fin, gagnant = verifier_victoire(tableau)
        if fin:
            if gagnant == 'NUL':
                print("Match nul.")
            else:
                print(f"Le joueur {gagnant} a gagné.")
            return

        joueur = 'O' if joueur == 'X' else 'X'


continuer = "o"
while continuer == "o":
    morpion()
    continuer = input("Rejouer 'o'/'n'? ")


print("A bientôt !")
