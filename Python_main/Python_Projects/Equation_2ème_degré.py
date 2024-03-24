import cmath  # Module pour traiter les nombres complexes si nécessaire

def resoudre_equation_quadratique(a, b, c):
    # Calcul du discriminant
    discriminant = b**2 - 4*a*c

    # Calcul des solutions
    if discriminant >= 0:
        # Si le discriminant est positif ou nul, il y a deux solutions réelles
        x1 = (-b + (discriminant)**0.5) / (2*a)
        x2 = (-b - (discriminant)**0.5) / (2*a)
        return x1, x2
    else:
        # Si le discriminant est négatif, il y a deux solutions complexes
        # Utilisation de nombres complexes avec le module cmath
        x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return x1, x2

# Exemple d'utilisation
a = 1
b = -3
c = -2

solutions = resoudre_equation_quadratique(a, b, c)
print("Les solutions de l'équation sont :", solutions)
