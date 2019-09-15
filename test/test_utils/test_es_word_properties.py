import unittest
from lingua_franca.lang.common_data_es import Gender, Number
from lingua_franca.lang.utils.es_word_properties import EsWordNaiveProperties, EsNaiveDeclinationProperties


class TestEsWordProperties(unittest.TestCase):

    def test_word_is_stored_and_accesible(self):
        word = 'hola'
        self.assertEqual(EsWordNaiveProperties(word).get_word(), word)

    def test_properties_knows_word_is_article(self):
        positive_examples = ('la', 'un', 'el')
        self.assertTrue(all(map(lambda example: EsWordNaiveProperties(
            example).is_article(), positive_examples)))
        not_an_article = 'perro'
        self.assertFalse(EsWordNaiveProperties(not_an_article).is_article())

    def test_properties_knows_number_of_word(self):
        negative_examples = ('la', 'un', 'perro', 'el')
        self.assertFalse(all(map(lambda example: EsWordNaiveProperties(
            example).is_plural(), negative_examples)))
        positive_examples = ('las', 'unos', 'perros', 'los')
        self.assertTrue(all(map(lambda example: EsWordNaiveProperties(
            example).is_plural(), positive_examples)))

    def test_properties_knows_gender_of_word(self):
        pass


class TestEsWordCase(unittest.TestCase):
    def test_word_is_stored_and_accesible(self):
        word = 'hola'
        self.assertEqual(EsNaiveDeclinationProperties(word).get_word(), word)

    def test_word_case_knows_number(self):
        singular_examples = ('segundo', 'perro', 'amiga')
        self.assertTrue(all(map(lambda example: EsNaiveDeclinationProperties(
            example).get_number() == Number.SINGULAR, singular_examples)))
        plural_examples = ('segundas', 'albercas', 'novecientas')
        self.assertTrue(all(map(lambda example: EsNaiveDeclinationProperties(
            example).get_number() == Number.PLURAL, plural_examples)))

    def test_word_case_knows_gender(self):
        masculine_examples = ('segundo', 'perro', 'sapos',
                              'el', 'un', 'los', 'uno', 'unos')
        self.assertTrue(all(map(lambda example: EsNaiveDeclinationProperties(
            example).get_gender() == Gender.MASCULINE, masculine_examples)))
        femenine_examples = ('segunda', 'lucha', 'ranas',
                             'la', 'las', 'una', 'unas')
        self.assertTrue(all(map(lambda example: EsNaiveDeclinationProperties(
            example).get_gender() == Gender.FEMENINE, femenine_examples)))

    def test_word_case_can_get_root_of_word(self):
        examples = (
            ('segundo', 'segund'),
            ('perro', 'perr'),
            ('sapos', 'sap'),
            ('camión', 'camión'),
            ('segundo', 'segund'),
            ('segunda', 'segund'))
        for example in examples:
            self.assertEqual(EsNaiveDeclinationProperties(example[0]).get_root(), example[1])

    def test_value_of_getters_is_idempotent(self):
        example = EsNaiveDeclinationProperties("caminos")
        self.assertEqual(example.get_gender(), Gender.MASCULINE)
        self.assertEqual(example.get_gender(), Gender.MASCULINE)
        self.assertEqual(example.get_number(), Number.PLURAL)
        self.assertEqual(example.get_number(), Number.PLURAL)
        self.assertEqual(example.get_root(), 'camin')
        self.assertEqual(example.get_root(), 'camin')

if __name__ == '__main__':
    unittest.main()
