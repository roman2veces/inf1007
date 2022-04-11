def sequence_infinie():
    chiffre = 1
    while chiffre < 10:
        yield chiffre
        chiffre += 1  # Quand next est appele


gen = sequence_infinie()  # retourne le generator
print(next(gen))  # fais la toute premiere iteration et retourne dans le yield
print(next(gen))  # recommence a partir du yield (l'etat conserve)
print(next(gen))
print(next(gen))
print(next(gen))

# for i in sequence_infinie(): # Jusqu'à que le generator termine
#     print(i, end=" ")
