from pylingdocs.models import Entity

class Phoneme(Entity):
    name = "Phoneme"
    cldf_table = "PhonemeTable"
    shortcut = "pnm"

class POS(Entity):
    name = "POS"
    cldf_table = "POSTable"
    shortcut = "pos"


models = [Phoneme, POS]
