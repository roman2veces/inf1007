import unittest

def est_pair(nbr):
    return nbr % 2 == 0

class MonTestUnit(unittest.TestCase):
    def setUp(self):
        self.liste = list(range(100)) # c'est comme si on ajoute l'attribut liste à self

    def test_est_pair(self):
        for n in self.liste:
            self.assertTrue(est_pair(n), n % 2 == 0)

unittest.main()