# Quand on cree de type d'erreur en fait on cree des classes vide
# pour pouvoir l'attraper par son nom
from tables import ComplexCol


class Velo:
    pass


mon_velo = Velo()
mon_autre_velo = Velo()

print(mon_autre_velo == mon_velo)  # CECI EST FAUX

# ------ Constructeur ------


class Velo:
    def __init__(self):  # si pas de constructeur alors il y a un cree par defaut
        self._couleur = "blue"

    # DECORATEURS


mon_velo = Velo()
mon_velo._couleur = "rouge"


# mon_velo = Velo()
# mon_autre_velo = Velo()

# print(mon_autre_velo == mon_velo) # CECI EST FAUX

# -------------------------------
class Compteur:
    c = 0  # Attribut partagé

    def __init__(self):
        self.c = 1  # Modifie le c de l'instance, different du c qui est un attribut partagé

        # Donc on en aura 2 variables c pour l'objet


print("---------- Exemple de nombre complexes -----------")


class Complexe:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def affiche(self):
        print(f"{self.r} + {self.i}j")

    # Definir notre propre fonction d'addition
    def plus(self, c):
        self.r += c.r
        self.i += c.i

    # Surcharger un operateur (IMPORTANT)
    def __add__(self, c):
        if not isinstance(c, Complexe):
            raise TypeError("mauvais type")

        return Complexe(r=self.r + c.r, i=self.i + c.i)


c1 = Complexe(2.4, 2.3)
c2 = Complexe(2.4, 2.3)
c3 = c1 + c2

# attributs avec _ => un attribut protégé (faible protection)
# _attribut c'est le vrai attribut a l'interieur de la classe
# attributs avec __ => un peu plus protege, python change le nom du vrai attribut change à l'interieur


class Personne:
    ESPECE = "Humain"

    def __init__(self) -> None:
        pass

    # Class method n'a pas d'acces aux attributs de l'instance
    @classmethod
    def modifierEspece(cls, valeur):
        cls.ESPECE = valeur  # Modifier un attribut de classc
        # Tous les objets seront modifiés, parce que c'est une class method et un attribut de classe

    # Createur des usines (factory, comme plusieurs types de constructeur)
    @classmethod
    def anniversaire(cls, nom, annee):
        return cls(nom, 2022 - annee)  # retourne une instance de la classe
        # on aurait pu utiliser aussi Personnne(nom, 2022 - annee), mais cls c'est une meilleure pratique

    # Methode statiques: Pas besoin d'une instance de la classe, pas reliée à l'objet
    @staticmethod
    def estAdulte(age):
        return age >= 18


autre_moi = Personne.anniversaire(nom='roman', annee=2000)
