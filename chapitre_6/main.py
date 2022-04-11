# ---------- Traitement de listes ---------
import copy
panier = [1, 2, 3, 4, 5, 6, 7]

# panier.extend([7, 8, 9])
print(panier)


print(panier[1:6:2])
print(panier[slice(1, 7, None)])
print(panier[-3:-1])

liste1 = [1, 2]
print(liste1 + [0, 3])

# ---------- Deep copy de listes ---------

# Premiere methode
liste2 = [1, 2, 3]
liste3 = liste2[:]
liste3[0] = 10
print(liste2)
print(liste3)

# Deuxieme methode
liste2 = [1, 2, 3]
liste3 = copy.deepcopy(liste2)
liste3[0] = 10
print(liste2)
print(liste3)

# ---------- Comprehension de listes ---------
print("---------- Comprehension de listes ---------")
liste4 = [(lambda x: x**2)(item) for item in range(10) if item % 2 == 0]
liste5 = [item**2 for item in range(10) if item % 2 == 0]  # Equivalent !!!

# [ <appel de fonction avec iterateur de la boucle> <boucle> <condition sur chaque iteration> ]
print(liste4)
print(liste5)

# ---------- Comprehension de listes avec conditions ---------
print("---------- Comprehension de listes avec conditions ---------")
liste6 = [item if item % 2 == 0 else 0 for item in range(10)]

print(liste6)

# ---------- Comprehension de listes dans listes ---------
print("---------- Comprehension de listes avec conditions ---------")
liste7 = [[col for col in range(10)] for ligne in range(10)]
for ligne in liste7:
    print(ligne)


# ---------- Ensembles (SET) ---------

print("---------- Ensemble (SET) ---------")
y = {1, 2, "holaaaa", 2, "qkweqkw", 2, 3, 3, 4}
print(list(y))  # Ordre change a chaque execution


# keys = my_dict.keys()
