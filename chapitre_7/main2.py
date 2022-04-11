import module
import numpy as np
from lib2to3.pgen2.pgen import generate_grammar
import time


def fois_deux(a):
    return a * 2

# Meme chose mais avec lambda


def f(a): return a * 2


print(f(4))
# ---------- Trier avec lambda -------------
# Lambda est utilise souvent dans les algorithmes de tri (trier)

données = ["B De Leener", "J Cohen", "M Guy"]


def ma_fonction(c):
    return c[2]


print(sorted(données, key=ma_fonction))


données = ["B De Leener", "J Cohen", "M Guy"]
print(sorted(données, key=lambda c: c[2]))

# ---------- Comment comprendre l'appel dans key -------------

données = ["B De Leener", "J Cohen", "M Guy"]


def ma_fonction(element):
    return element[2:]


print(sorted(données, key=ma_fonction))


# ma_fonction(données[0]) > ma_fonction(données[1]) ce qui se passe derriere

# ---------- Comment comprendre l'appel dans key -------------

données = ["B De Leener", "J Cohen", "M Guy"]


def ma_fonction(element):
    return element[2:]


print(sorted(données, key=lambda element: element[2:]))


# key(données[0]) > key(données[1]) ce qui se passe derriere

# ---------- Fonction internes  (ou imbriquees) -------------
# Elles permettent d'empecher laccess a la fonction interne
def fonction_externe(qui):
    def fonction_interne():
        print(f"Hello, {qui}!")
    fonction_interne()

# fonction_interne() pas possible de appeler depuis l,exterieur

# ---------- Faire de la fermeture avec fonctions imbriquees) -------------


def fonction_externe(x):
    y = 4

    def fonction_interne(z):
        return x + y + z
    return fonction_interne


fermeture = fonction_externe(3)

print(fermeture(4))

# ---------- Generateur de puissances avec fermeture -------------


def generer_puissance(exposant):
    def puissance(base):
        return base ** exposant
    return puissance


puissance_deux = generer_puissance(2)
puissance_trois = generer_puissance(3)
print(puissance_deux(4), puissance_deux(2))  # definition de la base ici
print(puissance_trois(4), puissance_trois(2))  # definition de la base ici


# ---------- Decorateur avec fonction imbriquees -------------
# Decorateur: a comprendre
def affiche_appel(fonction):
    def _affiche_appel():
        print("La fonction commence...")
        fonction()
        print("La fonction est terminée...")
    return _affiche_appel


@affiche_appel
def hello():
    print('Bonjour!')

# hello()

# ---------- Decorateur avec fonction imbriquees et parametres arbitraires -------------


def affiche_appel(fonction):
    def _affiche_appel(*args, **kwargs):
        print("La fonction commence...")
        fonction()
        print("La fonction est terminée...")
    return _affiche_appel


@affiche_appel
def hello(qui):
    print(f'Bonjour {qui}!')


hello('Benjamin')

# ---------- Mesurer le temps qui mettent 2 fonctions avec fonctions internes -------------


def timeit(fonction):
    def _fonction_interne(*args, **kwargs):
        t1 = time.time()
        resultat = fonction(*args, **kwargs)
        t2 = time.time()
        print(f"Ma fonction a pris {t2-t1} secondes.")
        return resultat
    return _fonction_interne


@timeit
def somme(nombres):
    resultat = 0
    for element in nombres:
        resultat += element
    return resultat


@timeit
def somme_numpy(nombres):
    return np.sum(nombres)


ma_liste = np.array(list(range(10000000)))

somme(ma_liste)
somme_numpy(ma_liste)

# ---------- Fonction generatrices -------------
# Stockees en memoire
# yield est associee aux iterateurs
# yield retourne la valeur mais quand on appelle encore la fonction il recommence au moment ou il etait rendu


def sequence_infinie():
    chiffre = 0
    while True:
        yield chiffre
        chiffre += 1


generateur = sequence_infinie()
print(next(generateur))
print(generateur.__next__())
print(next(generateur))
print(next(generateur))
print(next(generateur))
print(next(generateur))

# ---------- Exemple de portee de variables -------------
# meme si la variable "a" local a le meme nom que "a" global
# elle est une variable differente, car elle a ete creee dans une espace differente, avec une portabilite differente

a = 10  # variable globale


def f():
    a = 20  # variable locale
    print(a)


f()  # --> 20
print(a)  # --> 10

# ---------- Tester modifier une variable global dans une fonction -------------
b = 10  # variable globale


def f():
    global a
    a = 20  # variable locale
    print(a)


f()  # --> 20
print(a)  # --> 10

# ---------- Comportement de variables -------------
# il fera une copie profonde car c;est un type immuable


def f(c):
    c = 14


g = 10
f(g)
print(g)

# ---------- Comportement de variables -------------
# cas avec un type muable


def f(c):
    c.append(14)


g = [1, 2, 3]
f(g)
print(g)

# ---------- Importations -------------
module.ma_module_fonction()

print(module.mon_module_variable)

# from module import ma_module_fonction
