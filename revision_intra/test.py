# def est_bissextile(annee):
#     #     # On suppose que annee > 0
#     estBisextile = False
#     if (annee % 400 == 0):
#         estBisextile = True
#     elif (annee % 100 == 0):
#         estBisextile = False
#     elif (annee % 4 == 0):
#         estBisextile = True

# #     return estBisextile


# # print(est_bissextile(1999))
# # print(est_bissextile(2400))
# # print(est_bissextile(2100))
# # print(est_bissextile(2020))

# def compresse(donnees):
#     if len(donnees) == 0:  # TODO: Cas d'une liste vide
#         return None  # TODO: On arrête la fonction
#     i = 1
#     valeur = donnees[0]
#     position = 0
#     compteur = 1
#     while True:
#         if i == len(donnees):  # TODO: Si on est arrivé à la fin de la liste
#             del donnees[position:]
#             donnees.append((valeur, compteur))
#             break  # TODO: Arrêt de la boucle
#         if donnees[i] == valeur:  # TODO: Si on trouve la même valeur que précédemment
#             compteur += 1  # TODO: On incrémente le compteur
#             i += 1
#         else:  # TODO: Si on trouve une autre valeur
#             del donnees[position:i]
#             donnees.insert(position, (valeur, compteur))
#             compteur = 1
#             position += 1
#             valeur = donnees[position]
#             i = position + 1


# # donnees = [21, 21, 22, 23, 23, 25, 27, 27, 27, 1]
# # compresse(donnees)
# # print(donnees)
# valeurs = [0 for j in range(98)]
# valeurs.insert(1, 51)
# valeurs.insert(50, 52)
# for i in range(len(valeurs)):
#     print(len(valeurs))
#     print("---------")
#     if valeurs[i] > 50:
#         del valeurs[i]


print("bONJOUR" > "Bonjour")
