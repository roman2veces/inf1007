resultat = 1

def factorielle(n):
    if n != 0:
        global resultat # Si on ne faisait pas appel a la var global
        resultat *= n # Dans ce ligne il y aurait un bug parce qu'il assume que resultat est locale
        factorielle(n - 1)

factorielle(4)
print(resultat)