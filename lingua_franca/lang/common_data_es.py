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

from collections import OrderedDict
from enum import Enum

# Undefined articles ["un", "una"] can not be supressed,
# in Spanish, "un caballo" means "a horse" or "one horse".
ARTICLES_ES = ("el", "la", "los", "las", "unos", "unas", "un", "una")

class Gender(Enum):
    FEMENINE = 'a'
    MASCULINE = 'o'

class Number(Enum):
    SINGULAR = ''
    PLURAL = 's'

_STRING_NUM_ES = {
    "cero": 0,
    "un": 1,
    "uno": 1,
    "una": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9,
    "diez": 10,
    "once": 11,
    "doce": 12,
    "trece": 13,
    "catorce": 14,
    "quince": 15,
    "dieciséis": 16,
    "diecisisete": 17,
    "dieciocho": 18,
    "diecinueve": 19,
    "veinte": 20,
    "vent": 20,
    "veintidós": 22,
    "treinta": 30,
    "trent": 30,
    "cuarenta": 40,
    "cuarent": 40,
    "cincuenta": 50,
    "cincuent": 50,
    "sesenta": 60,
    "sesent": 60,
    "setenta": 70,
    "setent": 70,
    "ochenta": 80,
    "ochent": 80,
    "noventa": 90,
    "novent": 90,
    "cien": 100,
    "ciento": 100,
    "doscientos": 200,
    "trecientos": 300,
    "cuatrocientos": 400,
    "quinientos": 500,
    "seiscientos": 600,
    "setecientos": 700,
    "ochocientos": 800,
    "novecientos": 900,
    "mil": 1000,
    "cien mil": 100000,
    "millón": 1000000,
    "millardo": 1000000000,
    "primero": 1,
    "primera": 1,
    "segundo": 2,
    "segunda": 2,
    "medio": 0.5,
    "media": 0.5,
    "par": 2,
    "decena": 10,
    "docena": 12,
    "centena": 100,
    "millar": 1000,
}

_NUM_STRING_ES = {
    0: "cero",
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve",
    10: "diez",
    11: "once",
    12: "doce",
    13: "trece",
    14: "catorce",
    15: "quince",
    16: "dieciséis",
    17: "diecisiete",
    18: "dieciocho",
    19: "diecinueve",
    20: "veinte",
    30: "treinta",
    40: "cuarenta",
    50: "cincuenta",
    60: "sesenta",
    70: "setenta",
    80: "ochenta",
    90: "noventa",
}

_FRACTION_STRING_ES = {
    2: "medio",
    3: "tercio",
    4: "cuarto",
    5: "quinto",
    6: "sexto",
    7: "séptimo",
    8: "octavo",
    9: "noveno",
    10: "décimo",
    11: "onceavo",
    12: "doceavo",
    13: "treceavo",
    14: "catorceavo",
    15: "quinceavo",
    16: "dieciseisavo",
    17: "diecisieteavo",
    18: "dieciochoavo",
    19: "diecinueveavo",
    20: "veinteavo",
}

# fuente: http://tulengua.es/numeros-texto/default.aspx
# 100 puede ser ciento|centena?
# debe decirse en singular o plural?
_LONG_SCALE_ES = OrderedDict(
    [
        (100, "cien"),
        (1000, "mil"),
        (1000000, "millón"),
        (1e9, "millardo"),
        (1e12, "billón"),
        (1e18, "trillón"),
        (1e24, "cuatrillón"),
        (1e30, "quintillón"),
        (1e36, "sextillón"),
        (1e42, "septillón"),
        (1e48, "octillón"),
        (1e54, "nonillón"),
        (1e60, "decillón"),
        (1e66, "undecillón"),
        (1e72, "duodecillón"),
        (1e78, "tredecillón"),
        (1e84, "cuatrodecillón"),
        (1e90, "quindecillón"),
        (1e96, "sexdecillón"),
        (1e102, "septendecillón"),
        (1e108, "octodecillón"),
        (1e114, "novendecillón"),
        (1e120, "vigintillón"),
        (1e306, "unquinquagintillón"),
        (1e312, "duoquinquagintillón"),
        (1e336, "sexquinquagintillón"),
        (1e366, "unsexagintillón"),
    ]
)
# Prueba
_STRING_LONG_SCALE_ES = {
    'cien': 100,
    'mil': 1000,
    'millón': 1000000,
    'millardo': 1e9,
    'billón': 1e12,
    'trillón': 1e18,
    'cuatrillón': 1e24,
    'quintillón': 1e30,
    'sextillón': 1e36,
    'septillón': 1e42,
    'octillón': 1e48,
    'nonillón': 1e54,
    'decillón': 1e60,
    'undecillón': 1e66,
    'duodecillón': 1e72,
    'tredecillón': 1e78,
    'cuatrodecillón': 1e84,
    'quindecillón': 1e90,
    'sexdecillón': 1e96,
    'septendecillón': 1e102,
    'octodecillón': 1e108,
    'novendecillón': 1e114,
    'vigintillón': 1e120,
    'unquinquagintillón': 1e306,
    'duoquinquagintillón': 1e312,
    'sexquinquagintillón': 1e336,
    'unsexagintillón': 1e366

}

_SHORT_SCALE_ES = OrderedDict(
    [
        (100, "cien"),
        (1000, "mil"),
        (1000000, "millón"),
        (1e9, "billón"),
        (1e12, "trillón"),
        (1e15, "cuatrillón"),
        (1e18, "quintillón"),
        (1e21, "sextillón"),
        (1e24, "septillón"),
        (1e27, "octillón"),
        (1e30, "nonillón"),
        (1e33, "decillón"),
        (1e36, "undecillón"),
        (1e39, "duodecillón"),
        (1e42, "tredecillón"),
        (1e45, "cuatrodecillón"),
        (1e48, "quindecillón"),
        (1e51, "sexdecillón"),
        (1e54, "septendecillón"),
        (1e57, "octodecillón"),
        (1e60, "novendecillón"),
        (1e63, "vigintillón"),
        (1e66, "unvigintillón"),
        (1e69, "uuovigintillón"),
        (1e72, "tresvigintillón"),
        (1e75, "quattuorvigintillón"),
        (1e78, "quinquavigintillón"),
        (1e81, "qesvigintillón"),
        (1e84, "septemvigintillón"),
        (1e87, "octovigintillón"),
        (1e90, "novemvigintillón"),
        (1e93, "trigintillón"),
        (1e96, "untrigintillón"),
        (1e99, "duotrigintillón"),
        (1e102, "trestrigintillón"),
        (1e105, "quattuortrigintillón"),
        (1e108, "quinquatrigintillón"),
        (1e111, "sestrigintillón"),
        (1e114, "septentrigintillón"),
        (1e117, "octotrigintillón"),
        (1e120, "noventrigintillón"),
        (1e123, "quadragintillón"),
        (1e153, "quinquagintillón"),
        (1e183, "sexagintillón"),
        (1e213, "septuagintillón"),
        (1e243, "octogintillón"),
        (1e273, "nonagintillón"),
        (1e303, "centillón"),
        (1e306, "uncentillón"),
        (1e309, "duocentillón"),
        (1e312, "trescentillón"),
        (1e333, "decicentillón"),
        (1e336, "undecicentillón"),
        (1e363, "viginticentillón"),
        (1e366, "unviginticentillón"),
        (1e393, "trigintacentillón"),
        (1e423, "quadragintacentillón"),
        (1e453, "quinquagintacentillón"),
        (1e483, "sexagintacentillón"),
        (1e513, "septuagintacentillón"),
        (1e543, "ctogintacentillón"),
        (1e573, "nonagintacentillón"),
        (1e603, "ducentillón"),
        (1e903, "trecentillón"),
        (1e1203, "quadringentillón"),
        (1e1503, "quingentillón"),
        (1e1803, "sexcentillón"),
        (1e2103, "septingentillón"),
        (1e2403, "octingentillón"),
        (1e2703, "nongentillón"),
        (1e3003, "millinillón"),
    ]
)

# TODO: female forms.
_ORDINAL_STRING_BASE_ES = {
    1: "primero",
    2: "segundo",
    3: "tercer",
    4: "cuarto",
    5: "quinto",
    6: "sexto",
    7: "séptimo",
    8: "octavo",
    9: "noveno",
    10: "décimo",
    11: "undécimo",
    12: "duodécimo",
    13: "decimotercero",
    14: "decimocuarto",
    15: "decimoquinto",
    16: "decimosexto",
    17: "decimoséptimo",
    18: "decimoctavo",
    19: "decimonoveno",
    20: "vigésimo",
    30: "trigésimo",
    40: "cuadragésimo",
    50: "quincuagésimo",
    60: "sexagésimo",
    70: "septuagésimo",
    80: "octogésimo",
    90: "nonagésimo",
    10e3: "centésimó",
    1e3: "milésimo",
}

_STRING_ORDINAL_BASE_ES = {
    'primer': 1,
    'primero': 1,
    'primera': 1,
    'segundo': 2,
    'segunda': 2,
    'tercer': 3,
    'tercero': 3,
    'tercera': 3,
    'cuarto': 4,
    'cuarta': 4,
    'quinto': 5,
    'quinta': 5,
    'sexto': 6,
    'sexta': 6,
    'séptimo': 7,
    'séptima': 7,
    'octavo': 8,
    'octava': 8,
    'noveno': 9,
    'novena': 9,
    'décimo': 10,
    'décima': 10,
    'undécimo': 11,
    'undécima': 11,
    'duodécimo': 12,
    'duodécima': 12,
    'decimotercer': 13,
    'decimotercero': 13,
    'decimotercera': 13,
    'decimocuarto': 14,
    'decimocuarta': 14,
    'decimoquinto': 15,
    'decimoquinta': 15,
    'decimosexto': 16,
    'decimosexta': 16,
    'decimoséptimo': 17,
    'decimoséptima': 17,
    'decimoctavo': 18,
    'decimoctava': 18,
    'decimonoveno': 19,
    'decimonovena': 19,
    'vigésimo': 20,
    'vigésima': 20,
    'trigésimo': 30,
    'trigésima': 30,
    'cuadragésimo': 40,
    'cuadragésima': 40,
    'quincuagésimo': 50,
    'quincuagésima': 50,
    'sexagésimo': 60,
    'sexagésima': 60,
    'septuagésimo': 70,
    'septuagésima': 70,
    'octogésimo': 80,
    'octogésima': 80,
    'nonagésimo': 90,
    'nonagésima': 90,
    'centésimo': 10e3,
    'centésima': 10e3,
    'milésimo': 1e3,
    'milésima': 1e3
}

_SHORT_ORDINAL_STRING_ES = {
    1e6: "millonésimo",
    1e9: "milmillonésimo",
    1e12: "billonésimo",
    1e15: "milbillonésimo",
    1e18: "trillonésimo",
    1e21: "miltrillonésimo",
    1e24: "cuatrillonésimo",
    1e27: "milcuatrillonésimo",
    1e30: "quintillonésimo",
    1e33: "milquintillonésimo"
    # TODO > 1e-33
}

_STRING_SHORT_ORDINAL_ES = {
    'millonésimo': 1e6,
    'millonésima': 1e6,
    'milmillonésimo': 1e9,
    'milmillonésima': 1e9,
    'billonésimo': 1e12,
    'billonésima': 1e12,
    'milbillonésimo': 1e15,
    'milbillonésima': 1e15,
    'trillonésimo': 1e18,
    'trillonésima': 1e18,
    'miltrillonésimo': 1e21,
    'miltrillonésima': 1e21,
    'cuatrillonésimo': 1e24,
    'cuatrillonésima': 1e24,
    'milcuatrillonésimo': 1e27,
    'milcuatrillonésima': 1e27,
    'quintillonésimo': 1e30,
    'quintillonésima': 1e30,
    'milquintillonésimo': 1e33,
    'milquintillonésima': 1e33
    # TODO > 1e-33
}
_SHORT_ORDINAL_STRING_ES.update(_ORDINAL_STRING_BASE_ES)

_STRING_SHORT_ORDINAL_ES.update(_STRING_ORDINAL_BASE_ES)

#  para i> 10e12 solo se modifica el final: se solucionará al final
# de la depuración
_LONG_ORDINAL_STRING_ES = {
    1e6: "millonésimo",
    1e12: "billonésimo",
    1e18: "trillonésimo",
    1e24: "cuatrillonésimo",
    1e30: "quintillonésimo",
    1e36: "sextillonésimo",
    1e42: "septillonésimo",
    1e48: "octillonésimo",
    1e54: "nonillonésimo",
    1e60: "decillonésimo"
    # TODO > 1e60
}
_LONG_ORDINAL_STRING_ES.update(_ORDINAL_STRING_BASE_ES)
