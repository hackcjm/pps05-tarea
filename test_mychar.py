import unittest

from mychar import cadena_mas_larga


class TestCadenaMasLarga(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            (["a", "ab", "abc", "dddd", "abcd"], "abcd"),  # Caso normal
            (["zzzz", "aaaa"], "aaaa"),  # Empate alfabético
            ([], ""),  # Lista vacía
            (["único"], "único"),  # Un solo elemento
            (["sol", "sol", "sol"], "sol"),  # Palabras iguales
            (["Pepe", "José", "Ana"], "José"),  # Mayúsculas y acentos
        ]

    def test_funcionamiento_correcto(self):
        """Comprueba los resultados correctos en múltiples casos."""
        for palabras, esperado in self.test_cases:
            with self.subTest(palabras=palabras, esperado=esperado):
                self.assertEqual(cadena_mas_larga(palabras), esperado)

    def test_entrada_no_lista(self):
        """Verifica que se lanza ValueError si el argumento no es lista."""
        with self.assertRaises(ValueError):
            cadena_mas_larga("No lista de palabras.")

    def test_entrada_null(self):
        """Verifica que se lanza ValueError si el argumento None."""
        with self.assertRaises(ValueError):
            cadena_mas_larga(None)

    def test_elementos_invalidos(self):
        """Verifica que se lanza ValueError si hay elementos no cadena."""
        with self.assertRaises(ValueError):
            cadena_mas_larga(["cadena", 123, "cadena2"])

    def test_lista_cadena_vacia(self):
        """Comprueba que las cadenas vacías no generan error."""
        self.assertEqual(cadena_mas_larga(["cadena", "", "cadena2"]), "cadena2")


if __name__ == '__main__':
    unittest.main(verbosity=2)
