f = open('chapitre_8/test1')
print(f.readline(), end="")
print(f.readline(), end="") # Pas d'erreur si pas d'autre ligne 
print(f.readline()) # Affiche une ligne vide si pas d'autre ligne
print(f.readline()) 

# Attention: /n dupliqué quand on fait print readline (/n de la ligne et celui du print)

# TODO: Comprendre le nombre de caracteres total avec le fonction de lectures (read, readlines) 
# car je sais pas si /n est compté comme un caractere 

# Remarque: fichier contient tout ce qu'il y avait au moment de l'ouverture, s'il y a de modifications
# entre temps il tiendra pas compte dans la lecture

# TODO: verifier manipulation d'un fichier ailleur quand on a le context manager

print("-------- FAIRE PLUSIEURS ACTIONS DANS UN FICHIER (+) --------")
# Pas besoin de fermer le fichier quand on utilise le context manager (with as)
# with open("test.txt", "w+r") as fichier: # TODO: debugger
#     fichier.write("Hello world!")        
#     fichier.read()


print("-------- LIRE METEO --------")
with open("chapitre_8/meteo.txt", "r") as fichier:
    #donnees = fichier.readlines()
    donnees = fichier.read()
    lignes = donnees.split('\n')
    for ligne in lignes:
        print(ligne.split())

print("-------- LIRE CSV --------")
import csv
with open("chapitre_8/anniversaire.csv", "r") as fichier:
    lecteur = csv.reader(fichier, delimiter=',')
    for ligne in lecteur:
        print(ligne)

print("-------- ECRIRE DANS CSV --------")
with open("chapitre_8/anniversaires.csv", "a") as fichier:
    w = csv.writer(fichier, delimiter=',')
    w.writerow(['Eliot', 'décemb'])

print("-------- DictReader CSV --------") # Retourne les lignes sous forme de dictionnaire
with open("chapitre_8/anniversaires.csv", "r") as fichier:
    lecteur = csv.DictReader(fichier, delimiter=',')
    for ligne in lecteur:
        print(ligne)

print("-------- ECRIRE DANS JSON --------")
import json

x = {"name": "John", "age": 30, "city": "New York"}
with open('chapitre_8/donnees.json', 'w') as f:
    json.dump(x, f)

# Remarque: quand on fait la lecture dans fichier JSON, etant donne qu'il a de type de donnees,
# il se peut qu'on ne recoit pas une structure particulier de python par exemple 

print("-------- CONVERTIR JSON (DICT) EN STRING --------")
x = {'a': [1, 2, 3], 'autre': 'hello', 'dict': {'hello': [1, 2, 3, 4, 5, 6], 'valeur': True, False: 'autre_valeur'}}
v = json.dumps(x)
print(type(v))

print("-------- CONVERTIR STRING EN JSON (OU BIEN DICT) --------")
autre_variable = json.loads(v)
print(type(autre_variable))

print("-------- FICHIERS PICKLE --------")
import pickle
# Juste lisibles par python
couleurs = {"lion": " jaune", " chat": " noir"}
pickle.dump(couleurs, open("sauvegarde.benjamin", "wb"))

couleurs = pickle.load(open("sauvegarde.benjamin", "rb"))
