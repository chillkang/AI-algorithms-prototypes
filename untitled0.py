#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:04:46 2022

@author: seulkeekang
"""
from nltk.corpus import wordnet
from nltk.book import *

synonyms = []
for syn in wordnet.synsets('mind'):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
print(synonyms)

antonyms = []
for syn in wordnet.synsets('mind'):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
print(antonyms)

text7.concordance("artifical intelligence")