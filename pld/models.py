from lingdocs.models import Base, Morpheme

class Phoneme(Base):
    name = "Phoneme"
    cldf_table = "phonemes.csv"
    shortcut = "pnm"

class POS(Base):
    name = "POS"
    cldf_table = "partsofspeech.csv"
    shortcut = "pos"

class Lexeme(Morpheme):
    name = "Lexeme"
    cldf_table = "lexemes.csv"
    shortcut = "lex"

class Stem(Lexeme):
    name = "Stem"
    cldf_table = "stems.csv"
    shortcut = "stem"

class DerivationalProcess(Base):
    name = "Derivational process"
    cldf_table = "derivationalprocesses.csv"
    shortcut = "dproc"

models = [Phoneme, POS, Lexeme, Stem, DerivationalProcess]