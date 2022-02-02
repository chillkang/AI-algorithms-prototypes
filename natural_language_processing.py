# -*- coding: utf-8 -*-

import nltk
nltk.download('book')

#from nltk.book import *
#text1.concordance("monstrous")

#text1.similar("monstrous")
#text2.similar("monstrous")

#text2.common_contexts(["monstrous", "very"])

from nltk.corpus import wordnet
# =============================================================================
# syn = wordnet.synsets('pain')
# print(syn[0].definition())
# print(syn[0].examples())
# =============================================================================

# =============================================================================
# synonyms = []
# for syn in wordnet.synsets('pain'):
#         for lemma in syn.lemmas():
#             synonyms.append(lemma.name())
# 
# print(synonyms)
# =============================================================================

antonyms = []
for syn in wordnet.synsets('pain'):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

print(antonyms)
