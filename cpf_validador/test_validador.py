
import unittest
from validador import validar_nome, validar_cpf, validar_idade


class TestValidador(unittest.TestCase):
    def test_nome_valido(self):
        self.assertTrue(validar_nome("Maria"))
        self.assertFalse(validar_nome(""))

    def test_cpf_valido(self):
        self.assertTrue(validar_cpf("12345678901"))
        self.assertFalse(validar_cpf("1234"))
        self.assertFalse(validar_cpf("abcdefghijk"))

    def test_idade_valida(self):
        self.assertTrue(validar_idade(25))
        self.assertFalse(validar_idade(-1))
        self.assertFalse(validar_idade(121))


if __name__ == '__main__':
    unittest.main()
