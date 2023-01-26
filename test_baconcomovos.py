"""
TDD - Test Driven Development

Red
Parte 1 -> Criar o teste e ver falhar

Green
Parte 2 -> Criar o código e ver o teste passar

Refactor
Parte 3 -> Melhorar meu código

=================================================================

1-Receber um número inteiro

2-Saber se o número não é multiplo de 3 e 5:
    Passa Fome

3-Saber se o número é multiplo de 3 e 5:
    -Bacon com ovos

4-Saber se o número é multiplo de 3:
    -Bacon

5-Saber se o número é multiplo de 5:
    Ovos
"""
import unittest
from baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertionerror_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos("string")

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = "Bacon com ovos"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = "Passar fome"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida = "Bacon"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_de_5(self):
        entradas = (5, 10, 20, 25, 35)
        saida = "Ovos"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)


unittest.main(verbosity=2)
