def est_but(etat, but):
    return etat == but


def successeurs(etat):
    mouvement = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    vide = etat.index(0)
    i, j = divmod(vide, 3)  # Correction de la variable
    successeurs_list = []

    for di, dj in mouvement:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            nvcase = ni * 3 + nj
            nvetat = list(etat)
            nvetat[vide], nvetat[nvcase] = nvetat[nvcase], nvetat[vide]  # Correction de l'échange
            successeurs_list.append(nvetat)

    return successeurs_list


def recherche(etat_initiale, but):
    noeuds_a_traiter = [(etat_initiale, [], 0)]
    visite = set()

    while noeuds_a_traiter:
        etat, chemin, cout = noeuds_a_traiter.pop(0)

        if est_but(etat, but):  # Correction des paramètres
            return chemin, cout

        for succ in successeurs(etat):
            if tuple(succ) not in visite:
                visite.add(tuple(succ))  # Correction du nom de la variable (visited -> visite)
                noeuds_a_traiter.append((succ, chemin + [succ], cout + 1))  # Correction de l'ajout dans la liste

    return None, None


def afficher_puzzle(etat):
    for i in range(0, 9, 3):
        print("\t".join(map(str, etat[i:i + 3])))
    print("\n")


# Exemple d'exécution
etat_initiale = [7, 0, 1, 2, 3, 5, 4, 8, 6]
etat_but = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print("État initial :")
afficher_puzzle(etat_initiale)

chemin, cout = recherche(etat_initiale, etat_but)
if chemin is not None:
    print("Solution trouvée")
    print("Nombre d'actions effectuées :", cout)
    for etat in chemin:  # Correction de la variable i -> etat
        afficher_puzzle(etat)
else:
    print("Aucun chemin trouvé")

#Exemple d'execution
etat_initiale = [7,0,1,2,3,5,4,8,6]
etat_but = [0,1,2,3,4,5,6,7,8]
print("Etat initale : ")
afficher_puzzle(etat_initiale)
chemin , cout = recherche(etat_initiale , etat_but)
if chemin is not None :
    print("Solution trouvé")
    print("NOmbre d'action effectuées : ",cout)
    for i in chemin :
        afficher_puzzle(etat)
else :
    print("Aucun chemin trouvé ")
