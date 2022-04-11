def compute_pi(p):
    result = 0
    n = 0
    old_result = 1
    precision = 10 ** -p

    # TODO calculer la valeur de pi d'après la formule donnée dans l'énoncé
    i = 0
    while (abs(result - old_result) >= precision):
        # print(f"Ecart = {calculer_terme(i+1) - (calculer_terme(i))}")
        old_result = result
        result += calculer_terme(i)
        i += 1

    return result, i


def calculer_terme(i):
    return (4 * ((-1)**i))/((2*i)+1)


if __name__ == '__main__':
    # Calcul de π (pi)
    pi = 3.141592653589793
    p = 5
    computed_pi, nb_iter = compute_pi(p)
    print("La valeur réel de pi est : {}".format(pi))
    print("La valeur approché de pi à 10e-{} est : {}".format(p, computed_pi))
    print("Résultat obtenu après {} itérations".format(nb_iter))
