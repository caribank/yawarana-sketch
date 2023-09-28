from pylingdocs.models import Base

class Phoneme(Base):
    name = "Phoneme"
    cldf_table = "phonemes.csv"
    shortcut = "pnm"

class POS(Base):
    name = "POS"
    cldf_table = "partsofspeech.csv"
    shortcut = "pos"

class Lexeme(Base):
    name = "Lexeme"
    cldf_table = "lexemes.csv"
    shortcut = "lex"


models = [Phoneme(), POS(), Lexeme()]
