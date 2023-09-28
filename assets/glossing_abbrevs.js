var abbrev_dict={'1': 'first person', '2': 'second person', '3': 'third person', '1+2': 'first person inclusive', '1+3': 'first person exclusive', 'a': 'agent-like argument', 'abs': 'absolutive', 'all': 'allative', 'anim': 'animate', 'circ': 'circumstantive', 'cncs': 'concessive', 'concl': 'conclusive', 'contrast': 'contrastive', 'cop': 'copula', 'dat': 'dative', 'dem': 'demonstrative', 'des': 'desiderative', 'detrz': 'detransivizer', 'dim': 'diminutive', 'dist': 'distal', 'emp': 'emphatic', 'erg': 'ergative', 'ess': 'essive', 'fut': 'future', 'hsy': 'hearsay evidentiality', 'imn': 'imminent', 'imp': 'imperative', 'inan': 'inanimate', 'inf': 'infinitive', 'ins': 'instrumental', 'intr': 'intransitive', 'ints': 'intensifier', 'ipfv': 'imperfective', 'lk': 'linker', 'loc': 'locative', 'med': 'medial', 'mot': 'motion', 'motimp': 'motion imperative', 'neg': 'negation', 'nmlz': 'nominalizer', 'npert': 'unpossessed', 'nposs': 'nonpossessed', 'p': 'patient-like argument', 'pert': 'pertensive', 'pfv': 'perfective', 'pl': 'plural', 'plur': 'pluractional', 'poss': 'possession', 'priv': 'privative', 'pro': 'pronoun', 'prob': 'probabilitive', 'prog': 'progressive', 'proh': 'prohibitive', 'prox': 'proximal', 'pst': 'past', 'quot': 'quotative', 'rst': 'restrictive', 's': 'intransitive argument', 'sg': 'singular', 'tr': 'transitive', 'vbz': 'verbalizer', 'acnnmlz': 'action nominalizer', 'acnmlz': 'action nominalizer', 'agtnmlz': 'agent nominalizer', 'ptcp': 'participle', 'sup': 'supine', 'purp': 'purposive', 'cvb': 'converb', 'advz': 'adverbializer', 'nzr': 'nominalizer', 'gno': 'gnomic', 'ctmp': 'contemporative', 'cond': 'conditional', 'perl': 'perlative', 'rel': 'relativizer', 'juss': 'jussive', 'ctrf': 'counterfactive', 'cess': 'cessative', 'ad': 'ad-form', 'postp': 'postposition', 'aux': 'auxiliary', 'adv': 'adverb', 'prop': 'proprietive', 'ana': 'anaphoric', 'mod': 'modal', 'com': 'comitative', 'pos': 'possessed', 'emph': 'emphatic', 'restr': 'restrictive', 'cnfrm': 'confirmative', 'md': 'medial', 'an': 'animate', 'px': 'proximal', 'in': 'inanimate', 'perf': 'perfective', 'inm': 'immediate', 'voc': 'vocative', 'o': 'object', 'rm': 'remote?', 'sit': 'situational?', 'np': 'noun phrase', 'pred': 'predicative', 'subj': 'subject', 'part': 'particle', 'psn': 'person?', 'caus': 'causative', 'cntr': 'unknown abbreviation', 'surp': 'unknown abbreviation', 'exist': 'unknown abbreviation', 'eval': 'unknown abbreviation', 'foc': 'focus', 'fmr': 'unknown abbreviation', 'm': 'masculine', 'irr': 'irrealis', 'q': 'question particle/marker', 'k': 'unknown abbreviation', 'hes': 'unknown abbreviation', 'e': 'unknown abbreviation', 'hort': 'unknown abbreviation', 'pol': 'unknown abbreviation', 'c': 'unknown abbreviation', 'j': 'unknown abbreviation', 'obl': 'oblique', 'post': 'unknown abbreviation', 'r': 'unknown abbreviation', 'ill': 'unknown abbreviation', 'aq': 'unknown abbreviation', 'y': 'unknown abbreviation', '_a': 'unknown abbreviation', 'n': 'neuter', 'h': 'unknown abbreviation', 't': 'unknown abbreviation', 'pst.abs.nmlz': 'unknown abbreviation', '3p': 'unknown abbreviation', '1a': 'unknown abbreviation', '2a': 'unknown abbreviation', 'np~subj~': 'unknown abbreviation'}; for (var key in abbrev_dict){
var targets = document.getElementsByClassName('gloss-'+key)
for (var i = 0; i < targets.length; i++) {
    targets[i].innerHTML = abbrev_dict[key];
}
};
