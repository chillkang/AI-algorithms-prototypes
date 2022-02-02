# -*- coding: utf-8 -*-

import nltk
nltk.download('book')

#from nltk.book import *
#text1.concordance("monstrous")

#text1.similar("monstrous")
#text2.similar("monstrous")

#text2.common_contexts(["monstrous", "very"])

from nltk.corpus import wordnet
syn = wordnet.synsets('pain')
print(syn[0].definition())
print(syn[0].examples())
