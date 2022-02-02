# -*- coding: utf-8 -*-

import nltk
#nltk.download('book')

#from nltk.book import *
#text1.concordance("monstrous")

#text1.similar("monstrous")
#text2.similar("monstrous")

#text2.common_contexts(["monstrous", "very"])

#from nltk.corpus import wordnet
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

# =============================================================================
# antonyms = []
# for syn in wordnet.synsets('pain'):
#         for l in syn.lemmas():
#             if l.antonyms():
#                 antonyms.append(l.antonyms()[0].name())
# 
# print(antonyms)
# =============================================================================

# =============================================================================
# from nltk.corpus import swadesh
# =============================================================================
# =============================================================================
# print(swadesh.fileids())
# print(swadesh.words('en'))
# =============================================================================

# =============================================================================
# fr2en = swadesh.entries(['fr', 'en'])
# print(fr2en)
# translate = dict(fr2en)
# print(translate['chien'])
# print(translate['jeter'])
# =============================================================================
import random
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

print(random.shuffle(documents))
