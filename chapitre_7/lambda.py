# a = (lambda x, y, z: x + y + z)(5, 6, 5)
# print(a)

noms = ["B De leener", "J Dohen", "M Guy", "K Lapierre"]
# sorted_noms = sorted(noms)
# print(sorted_noms)

sorted_noms = sorted(noms, key=lambda x: x[2]) # trier selon caractere a la position 2

sorted_noms = sorted(noms, key=lambda x: x[2:]) # trier selon caractere a la position 2

print(sorted(range(-5, 6), key=lambda x: x**2))