#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:04:46 2022

@author: seulkeekang
"""
from nltk.corpus import wordnet
synonyms = []
for syn in wordnet.synsets('mind'):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
print(synonyms)