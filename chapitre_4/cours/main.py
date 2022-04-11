nombre_a_deviner = 50
nombre_utilisateur = int(input("Rentrez un nombre"))

while nombre_utilisateur != nombre_a_deviner:
    if nombre_a_deviner > nombre_utilisateur:
        print("Plus grand")
    else:
        print("Plus petit")
    nombre_utilisateur = int(input("Rentrez un nombre"))
print("Bravo !")

# variable = 5
# match variable:
#     case 5:
#         print('je suis 5')

# Pass ne fait rien (declarer une structure mais ne rien faire dedans)
# Continue passe a la prochaine iteration
# Break casse la boucle




