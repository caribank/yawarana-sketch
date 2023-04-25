from pylingdocs.models import Entity

class Phoneme(Entity):
    name = "Phoneme"
    cldf_table = "phonemes.csv"
    shortcut = "pnm"

class POS(Entity):
    name = "POS"
    cldf_table = "partsofspeech.csv"
    shortcut = "pos"

class Lexeme(Entity):
    name = "Lexeme"
    cldf_table = "lexemes.csv"
    shortcut = "lex"


models = [Phoneme, POS, Lexeme]
