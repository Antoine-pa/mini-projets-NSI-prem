import random

def couleur():
    return ["pique", "coeur", "carreau", "trèfle"]

def valeur():
    return ["as", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi"]

def creer_jeu():
    liste_carte = []
    for c in couleur():
        for v in valeur():
            liste_carte.append((v, c))
    return liste_carte

def melange(jeu):
    random.shuffle(jeu)
    return jeu

def distribue_1_carte(jeu: list, joueurs:dict):
    for joueur in joueurs.items():
        joueurs[joueur[0]].append(jeu[0])
        jeu = jeu[1:]
    return jeu, joueurs

def distribue(jeu, n):
    joueurs = {}
    for i in range(n):
        joueurs[i] = []
    while len(jeu) >= len(joueurs):
        jeu, joueurs = distribue_1_carte(jeu, joueurs)
    reste = jeu
    return joueurs, reste

print(distribue(melange(creer_jeu()), 3))
