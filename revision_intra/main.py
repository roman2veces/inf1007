noms = ["B De leener", "J Dohen", "M Guy", "K Lapierre"]

liste = [1, 2, ]
copy = noms.copy()  # Copy semi profonde, juste profonde pour un premier niveau
# copy = noms[:] semi profonde, juste profonde pour un premier niveau
copy[0] = 2
print(noms)
print(copy)

# ------------ convertir tranches negatives en positives ------------
a = list(range(3, 22, 2))
print(a[-7:-2:3])
print(a[len(a)-7:len(a)-2:3])

# print(list(range(3,22,2))[-7:-2:3])

# ------------ Match case ------------


# def alarme(elements):
# for i in range(1, len(elements)):
#    print(f'Il est {elements[0]}, il est temps de {elements[i]}')

# match elements:
#     case [heure, action]:
#         print(f'Il est {heure}, il est temps de {action}')
#     case [heure, *actions]:  # IMPORTANT: on peut comparer des structures comme ca
#         for action in actions:
#             print(f'Il est {heure}, il est temps de {action}')

# alarme(['9:00', 'Me réveiller'])
# alarme(['12:00', 'Manger', 'Faire une sieste', 'Étudier INF1007'])

# ------------ function join ------------
# def alarme(elements):
#     # for i in range(1, len(elements)):
#     #    print(f'Il est {elements[0]}, il est temps de {elements[i]}')

#     match elements:
#         case[heure, action]:
#             print(f'Il est {heure}, il est temps {action}')
#         case[heure, *actions]:
#             print(f'Il est {heure}, il est temps', ', '.join(
#                 [f'{action}' for action in actions]))


# alarme(['9:00', 'de me réveiller'])
# alarme(['12:00', 'de manger', 'de faire une sieste', 'd\'étudier INF1007'])

# ------ Exemple ------
c = 0
for i in range(10, 100, 5):
    print(i, c)
    c += i
    i += 1  # Cette ligne ne change pas la sequence d'iterationm

ma_liste = [3, 3]
ma_liste.sort
