class Test:
    def __init__(self, nom) -> None:
        self.nom = nom

    def __str__(self) -> str:
        return f"STR"

    def __repr__(self) -> str:
        return str(self) 

my_test = Test("test_1")
my_test_2 = Test("test_2") 

print([my_test, my_test_2])
