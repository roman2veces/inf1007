def fonctionExterne(x):
    y = 4
    def fonctionInterne(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z
    return fonctionInterne

for i in range(3):
    fermeture = fonctionExterne(i)
    print(f"fermeture({i+5}) = {fermeture(i+5)}")