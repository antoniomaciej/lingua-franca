import unittest
from lingua_franca.lang.common_data_es import Gender, Number
from lingua_franca.lang.utils.es_word_properties import EsWordNaiveProperties, EsNaiveDeclinationProperties


class TestEsWordProperties(unittest.TestCase):

    def test_word_is_stored_and_accesible(self):
        word = 'hola'
        self.assertEqual(EsWordNaiveProperties(word).get_word(), word)

    def test_word_properties_knows_word_is_article(self):
        positive_examples = ('la', 'un', 'el')
        self.assertTrue(all(map(lambda example: EsWordNaiveProperties(
            example).is_article(), positive_examples)))
        not_an_article = 'perro'
        self.assertFalse(EsWordNaiveProperties(not_an_article).is_article())

    def test_word_properties_knows_gender_and_number_of_word(self):
        example = EsWordNaiveProperties('example')
        self.assertEqual(
            'example', example.get_declination_properties().get_word())

    def test_get_declination_is_idempotent(self):
        example = EsWordNaiveProperties('example')
        self.assertEqual(
            example.get_declination_properties().get_word(),
            example.get_declination_properties().get_word())

    def test_is_number(self):
        positive_examples = ('22', '2.3', '0')
        negative_examples = ('string', 'alphaNum3r1c', 'ejemplo', '2,5', '0,0')
        for example in positive_examples:
            self.assertTrue(EsWordNaiveProperties(
                example).is_numeric())
        for example in negative_examples:
            self.assertFalse(EsWordNaiveProperties(
                example).is_numeric())

    def test_is_number_idempotency(self):
        example = EsWordNaiveProperties('22')
        self.assertEqual(example.is_numeric(), example.is_numeric())
        self.assertEqual(example.try_get_numeric_value(), 22.0)

    def test_is_try_get_numeric_value(self):
        positive_examples = (('22', 22.0), ('2.3', 2.3), ('0', 0.0))
        negative_examples = ('string', 'alphaNum3r1c', 'ejemplo', '2,5', '0,0')
        for example in positive_examples:
            self.assertEqual(EsWordNaiveProperties(
                example[0]).try_get_numeric_value(), example[1])
        for example in negative_examples:
            self.assertEqual(EsWordNaiveProperties(
                example).try_get_numeric_value(), example)


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
            self.assertEqual(EsNaiveDeclinationProperties(
                example[0]).get_root(), example[1])

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
