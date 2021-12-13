#1)
matrice_list = [[0, 0, 0, 2, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 3], [0, 0, 2, 0, 0]]

def repr_matrice_list():
    for a in range(5):
        for b in range(5):
            print(matrice_list[b][a], end="\n" if b == 4 else " ")

#2)
def matrice_list_dict():
    matrice_dict = {}
    for a in range(5):
        for b in range(5):
            val = matrice_list[b][a]
            if val != 0:
                matrice_dict[(b+1, a+1)] =val
    return matrice_dict

#3)
"""
le dictionnaire ne contient pas toute les valeurs
Donc si on teste d'accéder a une position de la matrice qui n'existe pas,
on aura un porblème
"""

#4) 5)
def test_pos_matrice_dict(x, y):
    return bool(matrice_list_dict().get((x, y), False))
