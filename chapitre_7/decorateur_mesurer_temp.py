import numpy as np
import time


def timeit(fonction):
    def _fonction_interne(*args):
        t1 = time.time()
        resultat = fonction(*args)
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
