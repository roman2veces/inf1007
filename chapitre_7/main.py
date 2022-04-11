def ma_fonction():
    # ma_deuxieme_fonction() 
    # Bug ici, python est interpreté donc il lit ligne par ligne
    # et ici ma_deuxieme_fonction() n'est pas encore declaree
    return print("hola")

ma_variable = ma_fonction() # Print sera quand même execute
print(ma_variable) # Print retourne un none

ma_fonction()

def ma_deuxieme_fonction():
    print('ca marche pas')

def somme(a, b, c):
    print(f"{a + b + c}")

# somme(12, 10, b=1) bug, quand on mixe params nommee et non nommee il faut dabord respecter lordre
somme(b=12, a=10, c=1) # tous nommee => peu importe lordre

def sommeParDefaut(a, b, c=10): # C = param avec valeur par defaut 
    print(f"{a + b + c}") 

sommeParDefaut(5, 5) 

def sommeParamsInfini(*nombres): # Recoit un tuple avec un nombre illimite de params
    somme = 0
    for nombre in nombres:
        somme += nombre
    print(f"Somme infinie: {somme}") 

sommeParamsInfini(4,5,4,3,4,5,5,6,6,1000)

def addition(x, y):
     return x + y

def multiplication(x, y):
     return x * y

def operateur(x, y, f): # f est une fonction passee en param
    return f(x, y)  

print("---------- Fonctions passees en params ----------")

print(operateur(10, 5, addition))
print(operateur(10, 5, multiplication))

def modification_de_liste(l):
    if l[0] == 15:
        l[1] = 'Non!!!'
    return l

print("---------- Reference de l'addresse dune liste est aussi passee en params ----------")
ma_liste = [15, 2, 3, 4, 5]
ma_liste_modifiée = modification_de_liste(ma_liste)
print(ma_liste)
print(ma_liste_modifiée)
print(id(ma_liste), id(ma_liste_modifiée))
