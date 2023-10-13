#### The corpus

A corpus of [texts](texts) forms the basis of this grammar sketch.
They were collected by [Natalia Cáceres-Arandia](https://pages.uoregon.edu/nataliac/) in the course of the NSF funded project ['Documenting Linguistic Structure and Language Change in Yawarana'](https://nsf.gov/awardsearch/showAward?AWD_ID=1500714&HistoricalAwards=false).
They were transcribed in ELAN and enriched with morphological annotation by [uniparser-yawarana](https://github.com/fmatter/uniparser-yawarana/) [psrc](matter2022uniparser)
The following excerpt showcases the features of the corpus:

[ex](ctorat-3)

The first object line is a link to the entire text record ('sentence', 'example'...).
The second line contains links to individual word forms.
The third line contains links to individual morphs.
The fourth line shows POS tags.
The link in parentheses leads to the (con-)text of the record.
Audio associated with the record is shown below it.
Translations are in English (partially auto-translated with [deepl](https://www.deepl.com/translator) and in Spanish.

Words that uniparser-yawarana was unable to parse are glossed with `***` [exref](convrisamaj-28).
Words with multiple possible analyses (where none has been confirmed manually yet) are glossed with `?`.

[ex](convrisamaj-28)

#### The 'dictionary'
The dictionary part of this app contains different kinds of entities.
At the moment, these are morphemes, morphs, and word forms.
They relate to each other as follows: word forms are forms that occur in the annotated corpus or were uttered in elicitation.
Word forms are composed of morphs, which in turn belong to morphemes.
Word forms as well as morphemes and their morphs can have different meanings, depending on the context.


To illustrate: the form [wf](winijse-sleep-pst) 's/he slept' is composed of the morphs [m](winij-sleep) and [m](sepst), which in turn belong to the morphemes [mp](winiki-sleep) and [mp](sepst).
All of the preceding links lead to detail views of these entities, with information like morphological structure, associated word forms, and, most importantly, tokens from the corpus.

#### The grammar
...is under construction and therefore bullet-pointy.
Individual chapters can be browsed under [documents](documents); a PDF version can be found [here](download).
The text is being written with [pylingdocs](https://github.com/fmatter/pylingdocs) ([document source](https://github.com/fmatter/yawarana-sketch)).