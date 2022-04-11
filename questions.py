# ---------- QUESTION 1 ------------
# Difference entre ces deux fonctions lambda de tri ?

noms = ["J Dohen", "B De leener", "M Guy", "K Lapierre"]

# Trier juste en fonction de 2 caractere
# sorted_noms = sorted(noms, key=lambda x: x[2])

# Trier en fonction de 2 caractere et ce qui suivent
sorted_noms = sorted(noms, key=lambda x: x[2:])
print(sorted_noms)

# liste = [1, 2, ]
# copy = noms.copy()  # Copy semi profonde, juste profonde pour un premier niveau
# # copy = noms[:] semi profonde, juste profonde pour un premier niveau
# copy[0] = 2
# print(noms)
# print(copy)

# ---------- QUESTION 2 ------------
