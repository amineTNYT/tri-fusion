def tri_fusion(tableau):
    if len(tableau) <= 1:
        return
    mid = len(tableau) // 2
    gauche = tableau[:mid]
    droite = tableau[mid:]
    tri_fusion(gauche)
    tri_fusion(droite)
    
    i = j = k = 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            tableau[k] = gauche[i]
            i += 1
        else:
            tableau[k] = droite[j]
            j += 1
        k += 1
    
    while i < len(gauche):
        tableau[k] = gauche[i]
        i += 1
        k += 1
    
    while j < len(droite):
        tableau[k] = droite[j]
        j += 1
        k += 1

# Exemple d'utilisation
T = [8, 3, 7, 4, 2, 6, 5, 1]
tri_fusion(T)
print(T)  # [1, 2, 3, 4, 5, 6, 7, 8]
