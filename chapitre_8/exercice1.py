# REMARQUE: Context manager avec plusieurs fichiers
with open('test.txt') as f1, open('test copy.txt') as f2:
    i = 0
    while True:
        if f1.read(1) != f2.read(1):
            print(f'Le caractère à la position {i} est différent.')
            break
        i += 1

# Pour plus que 2 fichiers:
# with (open('test.txt') as f1, 
#       open('test copy.txt') as f2):