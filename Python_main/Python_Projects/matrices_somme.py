def additionner_matrices_carrees(matrice1, matrice2):
    # Vérifier que les matrices ont la même taille et sont carrées (ordre 3x3)
    if len(matrice1) != 3 or len(matrice2) != 3 or len(matrice1[0]) != 3 or len(matrice2[0]) != 3:
        raise ValueError("Les matrices doivent être d'ordre 3x3.")

    # Initialiser une matrice résultante avec des zéros
    resultat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Additionner les éléments correspondants
    for i in range(3):
        for j in range(3):
            resultat[i][j] = matrice1[i][j] + matrice2[i][j]

    return resultat

# Exemple d'utilisation
matrice_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrice_B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

matrice_resultante = additionner_matrices_carrees(matrice_A, matrice_B)

# Afficher la matrice résultante
for ligne in matrice_resultante:
    print(ligne)
