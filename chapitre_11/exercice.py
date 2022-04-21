class Nombre:
    MULTIPLICATEUR = 5

    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y
    
    def somme(self):
        return self.__x + self.__y
    
    @classmethod
    def multiplie(cls, a):
        return cls.MULTIPLICATEUR * a

    @staticmethod
    def soustrait(b, c):
        return b - c 

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    @property
    def valeur(self):
        return self.__x, self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y


mon_nombre = Nombre(5, 2)
print(mon_nombre.somme())
print(Nombre.multiplie(10))
print(mon_nombre.soustrait(5, 5))
print(mon_nombre.valeur)

mon_nombre.x = 1
mon_nombre.y = 0

print(mon_nombre.valeur)





    


    