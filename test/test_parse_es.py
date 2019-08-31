# -*- coding: utf-8 -*-
#
# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import unittest

from lingua_franca.parse import normalize, extract_number


class TestNormalize(unittest.TestCase):
    """
        Test cases for Spanish parsing
    """

    def test_articles_es(self):
        self.assertEqual(normalize("esta es la prueba", lang="es",
                                   remove_articles=True),
                         "esta es prueba")
        self.assertEqual(normalize("y otra prueba", lang="es",
                                   remove_articles=True),
                         "y otra prueba")

    def test_numbers_es(self):
        self.assertEqual(normalize("esto es un uno una", lang="es"),
                         "esto es 1 1 1")
        self.assertEqual(normalize("esto es dos tres prueba", lang="es"),
                         "esto es 2 3 prueba")
        self.assertEqual(normalize("esto es cuatro cinco seis prueba",
                                   lang="es"),
                         "esto es 4 5 6 prueba")
        self.assertEqual(normalize(u"siete mï¿½s ocho mï¿½s nueve", lang="es"),
                         u"7 mï¿½s 8 mï¿½s 9")
        self.assertEqual(normalize("diez once doce trece catorce quince",
                                   lang="es"),
                         "10 11 12 13 14 15")
        self.assertEqual(normalize(u"dieciséis diecisiete", lang="es"),
                         "16 17")
        self.assertEqual(normalize(u"dieciocho diecinueve", lang="es"),
                         "18 19")
        self.assertEqual(normalize(u"veinte treinta cuarenta", lang="es"),
                         "20 30 40")
        self.assertEqual(normalize(u"treinta y dos caballos", lang="es"),
                         "32 caballos")
        self.assertEqual(normalize(u"cien caballos", lang="es"),
                         "100 caballos")
        self.assertEqual(normalize(u"ciento once caballos", lang="es"),
                         "111 caballos")
        self.assertEqual(normalize(u"había cuatrocientas una vacas",
                                   lang="es"),
                         u"había 401 vacas")
        self.assertEqual(normalize(u"dos mil", lang="es"),
                         "2000")
        self.assertEqual(normalize(u"dos mil trescientas cuarenta y cinco",
                                   lang="es"),
                         "2345")
        self.assertEqual(normalize(
            u"ciento veintitrés mil cuatrocientas cincuenta y seis",
            lang="es"),
            "123456")
        self.assertEqual(normalize(
            u"quinientas veinticinco mil", lang="es"),
            "525000")
        self.assertEqual(normalize(
            u"treintaidos", lang="es"),
            "treintaidos")
        self.assertEqual(normalize(
            u"novecientos noventa y nueve mil novecientos noventa y nueve",
            lang="es"),
            "999999")

    def test_isFractional_es(self):
        self.assertEqual(extract_number(
            "un par",
            lang="es"),
            1.0)
        self.assertEqual(extract_number(
            "dos enteros",
            lang="es"),
            2.0)
        self.assertEqual(extract_number(
            "tres cuartos",
            lang="es"),
            3.0 / 4.0)
        self.assertEqual(extract_number(
            "una tercera parte",
            lang="es"),
            1.0 / 3.0)
        self.assertEqual(extract_number(
            "una vigésima parte",
            lang="es"),
            1.0 / 20.0)
        self.assertEqual(extract_number(
            "siete excepciones",
            lang="es"),
            7.0)
        self.assertEqual(extract_number(
            "seis helados",
            lang="es"),
            6.0)
        self.assertEqual(extract_number(
            "siete doceavos",
            lang="es"),
            7.0 * (1.0 / 12.0))
        self.assertEqual(extract_number(
            "tres trigésimas de segundo",
            lang="es"),
            3.0 / 30.0)
        self.assertEqual(extract_number(
            "tres milésimas de segundo",
            lang="es"),
            3.0 / 1000.0)
        # According to RAE, this form is wrong.
        # On such composite ordinals, one should use the -avo -ava suffix.
        # Therefor, it get's filtered.
        # However, although gramatically wrong, it could be accepted, as the intent is clear.
        # Then, the expected output should be 3.0 / 35.0
        # http://lema.rae.es/dpd/srv/search?key=fraccionarios&submit.x=0&submit.y=0
        self.assertEqual(extract_number(
            "tres trigésimoquintas de segundo",
            lang="es"),
            3.0)
        self.assertEqual(extract_number(
            "tres octavos",
            lang="es"),
            3.0 / 8.0)
        # self.assertEqual(extract_number(
        #     "tres treintaidosavos",
        #     lang="es"),
        #     3.0 / 32.0)

    # def test_isOrdinal_es(self):
    #     self.assertEqual(extract_number(
    #         "el vigésimo lugar",
    #         lang="es"),
    #         20)


if __name__ == "__main__":
    unittest.main()
