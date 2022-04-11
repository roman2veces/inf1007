def inverse(x):
    if x==0:
        # Declarer un ValueError pour etre attrapé dans le bloc try
        raise ValueError("Valeur nulle")
    elif x == 1:
        raise Exception("Exception x == 1") # Declarer une exception pour etre attrapee 
    return 1 / x

try:
    print(inverse(0))
except ValueError as error: # alias pour mon valueError
    print("Error message: ", error)


print('Programme pas arretee')