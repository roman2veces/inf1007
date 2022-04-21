import io
import pstats
import cProfile
import argparse
from pstats import SortKey
import timeit
from time import time
print("---------- Mesurer le temps dune fonction --------")


def some_function():
    some_list = [i for i in range(10000)]

    new_list = []
    for elem in some_list:
        new_list.append([i for i in range(elem)])


if __name__ == "__main__":
    begin = time()
    some_function()
    end = time()

    print(f'Cela a pris {end - begin} secondes!')


print("---------- Mesurer le temps dune fonction avec DECORATEUR --------")


def decorateur_temps(func):
    def wrapper(*args, **kwargs):
        begin = time()
        resultat = func(*args, **kwargs)
        end = time()
        print(f'Cela a pris {end - begin} secondes!')
        return resultat
    return wrapper


@decorateur_temps
def some_function():
    some_list = [i for i in range(10000)]

    new_list = []
    for elem in some_list:
        new_list.append([i for i in range(elem)])


some_function()

print("---------- REVISER CE CODE ET COMPRENDRE DIFFERENCE AVEC PRECEDANT --------")


def decorateur_temps(func):
    repetitions = 100

    def wrapper(*args, **kwargs):
        temps = []
        for _ in range(repetitions):
            begin = time()
            resultat = func(*args, **kwargs)
            end = time()
            temps.append(end-begin)
        print(f'Cela a pris {sum(temps)/repetitions} secondes!')
        return resultat
    return wrapper


@decorateur_temps
def some_function():
    some_list = [i for i in range(1000)]

    new_list = []
    for elem in some_list:
        new_list.append([i for i in range(elem)])


some_function()

print("---------- REVISER CE CODE ET COMPRENDRE DIFFERENCE AVEC PRECEDANT (decorateur avec de parametres) --------")


def temps_repeat(repetitions):
    def decorateur_temps(func):
        def wrapper(*args, **kwargs):
            temps = []
            for _ in range(repetitions):
                begin = time()
                resultat = func(*args, **kwargs)
                end = time()
                temps.append(end-begin)
            print(f'Cela a pris {sum(temps)/repetitions} secondes!')
            return resultat
        return wrapper
    return decorateur_temps


@temps_repeat(repetitions=100)
def some_function():
    some_list = [i for i in range(1000)]

    new_list = []
    for elem in some_list:
        new_list.append([i for i in range(elem)])


some_function()

print("---------- MESURER TEMPS DEXECUTION AVEC Timeit --------")
setup_code = """
name = "Pylenin"
result_list = []
"""
main_code = """
for char in name:
    result_list.append(char)
"""
print(timeit.timeit(stmt=main_code,
                    setup=setup_code,
                    number=10000))

print("---------- PROFILAGE --------")
# Mesurer temps dexecution ligne par ligne

pr = cProfile.Profile()
pr.enable()

some_list = [i for i in range(1000)]
new_list = []
for elem in some_list:
    new_list.append([i for i in range(elem)])

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

print("---------- PASSER DES ARGUMENTS DANS LA LIGNE DE COMMANDES --------")

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
print(args.accumulate(args.integers))

# Commande: python bacasable.py 1 2 3 4 --sum

# NOTES :

# 1 Dès que l'erreur est attrapé le reste du code dans le try n'est pas executé

# 2 Des qu'un erreur est attrapé, l'interpreteur n'essaie pas d'en attraper d'autres (TESTER)
