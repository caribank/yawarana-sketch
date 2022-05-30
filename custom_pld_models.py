from pylingdocs.models import Entity

class Phoneme(Entity):
    name = "Phoneme"
    cldf_table = "PhonemeTable"
    shortcut = "pnm"

models = [Phoneme]
