from lingua_franca.lang.common_data_es import ARTICLES_ES, Gender, Number


class EsWordNaiveProperties:
    """
    Retruns properties of a given word assuming it is a regular Spanish word.
    Number are gender are assumed from the most common suffixes.
    It does not aim to be exhaustive, but to be able to identify correctly properties of regular words such as numbers.
    """

    def get_word(self):
        return self.__word

    def is_article(self):
        return self.__word in ARTICLES_ES

    def is_numeric(self):
        if self.__is_numeric is not None:
            return self.__is_numeric
        else:
            self.try_get_numeric_value()
            return self.__is_numeric

    def try_get_numeric_value(self):
        if self.__is_numeric is not None and self.__numeric_value is not None:
            return self.__numeric_value
        else:
            try:
                self.__numeric_value = float(self.__word)
                self.__is_numeric = True
            except ValueError:
                self.__numeric_value = self.__word
                self.__is_numeric = False
            return self.__numeric_value

    def get_declination_properties(self):
        if self.__declination is not None:
            return self.__declination
        else:
            self.__declination = EsNaiveDeclinationProperties(self.__word)
            return self.__declination

    def __init__(self, word):
        self.__word = word
        self.__declination = None
        self.__is_numeric = None
        self.__numeric_value = None


class EsNaiveDeclinationProperties:
    """
    A naive implementation of extracting gender and numbers targeted at regular words, such as numbers.
    Number and gender are assumed from the most common suffixes.
    Private fields are calculated after the first call to the getter function.
    """

    def get_word(self):
        return self.__word

    def get_gender(self):
        if self.__gender is not None:
            return self.__gender
        else:
            self.__gender = _identify_gender(self.__word)
            return self.__gender

    def get_number(self):
        if self.__number is not None:
            return self.__number
        else:
            self.__number = _identify_number(self.__word)
            return self.__number

    def get_root(self):
        if self.__root is not None:
            return self.__root
        else:
            self.__root = _get_root_of_word(self.__word)
            return self.__root

    def __init__(self, word):
        self.__word = word
        self.__number = None
        self.__gender = None
        self.__root = None


def _is_plural_word(word):
    return word[-1] == Number.PLURAL.value


def _is_femenine_word(word):
    singular = _get_singular_of_word(word)
    return singular[-1] == Gender.FEMENINE.value


def _identify_number(word):
    return Number.PLURAL if _is_plural_word(word) else Number.SINGULAR


def _identify_gender(word):
    return Gender.FEMENINE if _is_femenine_word(word) else Gender.MASCULINE


def _get_singular_of_word(word):
    return word[:-1] if _is_plural_word(word) else word


def _get_root_of_word(word):
    singular = _get_singular_of_word(word)
    return singular[:-1] if _is_femenine_word(word) or singular[-1] == Gender.MASCULINE.value else singular
