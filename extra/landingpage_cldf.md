# A digital sketch grammar of Yawarana
This is a **corpus-based, data-rich digital grammar**[^1] sketch of [Yawarana](yaba1248) developed and written by [Florian Matter](https://fl.mt) in collaboration with [Natalia Cáceres-Arandia](https://pages.uoregon.edu/nataliac/) and [Spike Gildea](https://cas.uoregon.edu/directory/linguistics/all/spike).
It is based on a corpus of [texts](texts), collected by Cáceres-Arandia and annotated using [uniparser-yawarana](https://github.com/fmatter/uniparser-yawarana/).

This is the [CLLD](https://clld.org/) version of the grammar, which aims to make accessible all three components of a Boasian trilogy.

Other available formats:

- [mkdocs](https://caribank.github.io/yawarana-sketch)
- [PDF (LaTeX)](https://github.com/caribank/yawarana-sketch/blob/main/output/latex/main.pdf)

Visit the [github repo](https://github.com/caribank/yawarana-sketch) for bundled releases and the markup source.

[^1]: Work in progress: [a guide to create your own](https://fl.mt/digital-grammar-tutorial).

## The grammar sketch
...is still under construction and therefore bullet-pointy.
It is divided into chapters, browsable under [description](description).

## The corpus
The annotated texts are browsable under [corpus](corpus), the results of annotating them under [morphosyntax](morphosyntax).
Example [exref](ctorat-3) illustrates the current features of the corpus:

[ex](ctorat-3)

The first object line is a link to the entire text record ('sentence', 'example'...).
The second line contains links to individual word forms.
The third line contains links to individual morphs.
The fourth line shows POS tags.
The link in parentheses leads to the (con-)text of the record.
Audio associated with the record is shown below it.
There is both an English (partially auto-translated with [deepl](https://www.deepl.com/translator)) and the original Spanish translation.

Words that uniparser-yawarana was unable to parse are glossed with `***` [exref](convrisamaj-28).
Words with multiple possible analyses (where none has been confirmed manually yet) are glossed with `?`.

[ex](convrisamaj-28)

## The 'dictionary'
The dictionary component of this project is not that sophisticated, since the focus lies on the grammatical description.
The [lg](yab) lexicon is modeled using four kinds of entities: morphemes, morphs, lexemes, and stems, browsable under [lexicon](lexicon).
Word forms (in [morphosyntax](morphosyntax)) are forms that occur in the annotated corpus or were uttered in elicitation.
They are composed of morphs, which in turn belong to morphemes.
Where applicable they contain a stem, which in turn belongs to a lexeme.
To illustrate: the wordform [wf](winijse-sleep-pst?nt) 's/he slept' is composed of the morphs [m](winij-sleep?nt) and [m](sepst?nt), which in turn belong to the morphemes [mp](winiki-sleep) and [mp](sepst).
The form belongs to the lexeme [lex](winiki-sleep).