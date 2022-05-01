print("-------- FICHIERS PICKLE --------")
import pickle
# Juste lisibles par python
# couleurs = {"lion": " jaune", " chat": " noir"}
# pickle.dump(couleurs, open("sauvegarde.benjamin", "wb"))

couleurs = pickle.load(open("sauvegarde.benjamin", "rb"))
print(couleurs)