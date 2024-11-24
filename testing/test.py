import unittest
from funciones import es_primo, es_par

class TestEsPrimo(unittest.TestCase):
    def test_primo(self):
        self.assertTrue(es_primo(7))  # 7 es primo
        self.assertTrue(es_primo(13))  # 13 es primo

    def test_no_primo(self):
        self.assertFalse(es_primo(4))  # 4 no es primo
        self.assertFalse(es_primo(1))  # 1 no es primo
        self.assertFalse(es_primo(0))  # 0 no es primo

    def test_numeros_negativos(self):
        self.assertFalse(es_primo(-7))  # Los negativos no son primos

class TestEsPar(unittest.TestCase):
    def test_par(self):
        self.assertTrue(es_par(2))  # 2 es par
        self.assertTrue(es_par(100))  # 100 es par

    def test_impar(self):
        self.assertFalse(es_par(3))  # 3 no es par
        self.assertFalse(es_par(101))  # 101 no es par

if __name__ == "__main__":
    unittest.main()

