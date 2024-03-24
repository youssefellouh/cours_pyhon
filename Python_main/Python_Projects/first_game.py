import random

def jeu_de_devinette():
    print("Bienvenue dans le jeu de devinette!")
    nombre_a_deviner = random.randint(1, 100)
    tentative = 0

    while True:
        tentative += 1
        proposition = int(input("Devinez le nombre (entre 1 et 100) : "))

        if proposition < nombre_a_deviner:
            print("Trop bas. Essayez encore.")
        elif proposition > nombre_a_deviner:
            print("Trop haut. Essayez encore.")
        else:
            print(f"Bravo ! Vous avez deviné le nombre en {tentative} tentatives.")
            break

# Lancer le jeu
jeu_de_devinette()
