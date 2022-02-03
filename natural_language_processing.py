# -*- coding: utf-8 -*-

#Exercise 1

import nltk
# =============================================================================
# nltk.download('book')
# 
# from nltk.book import *
# print(text1, text2, text3, text4, text5, text6, text7, text8, text9)
# =============================================================================
# =============================================================================
# 
# #enable us to see words in context
# #shows every occurrence of a given word together with some context 
# text1.concordance("monstrous")
# 
# #words in similar range of contexts
# text1.similar("monstrous")
# text2.similar("monstrous")
# 
# #contexts shared by two or more words
# text2.common_contexts(["monstrous", "very"])
# 
# #finding definitions and usage of words in Wordnet
# from nltk.corpus import wordnet
# syn = wordnet.synsets('pain')
# print(syn[0].definition())
# print(syn[0].examples())
# 
# #synonyms
# synonyms = []
# for syn in wordnet.synsets('pain'):
#         for lemma in syn.lemmas():
#             synonyms.append(lemma.name())
# print(synonyms)
# 
# #antonyms
# antonyms = []
# for syn in wordnet.synsets('pain'):
#         for l in syn.lemmas():
#             if l.antonyms():
#                 antonyms.append(l.antonyms()[0].name())
# print(antonyms)
# 
# #comparative wordlist
# #NLTK includeing Swadesh wordlists (lists of about 200 common words in several languages) 
# #The languages are identified using an ISO 639 two-letter code.
# from nltk.corpus import swadesh
# print(swadesh.fileids())
# print(swadesh.words('en'))
# 
# #access cognate words from multiple languages using the entries() method, 
# #convert this into a simple dictionary 
# fr2en = swadesh.entries(['fr', 'en'])
# print(fr2en)
# translate = dict(fr2en)
# print(translate['chien'])
# print(translate['jeter'])
# 
# 
# #build classifiers that will automatically tag new documents with appropriate category labels
# import random
# 
# from nltk.corpus import movie_reviews
# documents = [(list(movie_reviews.words(fileid)), category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)]
# print(random.shuffle(documents))
# 
# #define a feature extractor for documents
# #limit the number of features that the classifier needs to process to 2000 most frequent words
# #define a feature extractor that simply checks whether each of these words is present in a given document
# all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# word_features = list(all_words)[:2000] 
# 
# def document_features(document): 
#     document_words = set(document) 
#     features = {}
#     for word in word_features:
#         features['contains({})'.format(word)] = (word in document_words)
#     return features
# print(document_features(movie_reviews.words('pos/cv957_8737.txt'))) 
# 
# #use feature extractor to train a classifier to label new movie reviews. 
# featuresets = [(document_features(d), c) for (d,c) in documents]
# train_set, test_set = featuresets[100:], featuresets[:100]
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# 
# #compute its accuracy on the test set
# #use show_most_informative_features() to find out which features the classifier found to be most informative.
# print(nltk.classify.accuracy(classifier, test_set))
# classifier.show_most_informative_features(5) 
# 
# =============================================================================

#Exervise 2
# =============================================================================
# text1.concordance("however")
# text2.concordance("however")
# text3.concordance("however")
# text4.concordance("however")
# text5.concordance("however")
# text6.concordance("however")
# text7.concordance("however")
# text8.concordance("however")
# text9.concordance("however")
# =============================================================================

#Exercise 4

from nltk.corpus import swadesh
en2it = swadesh.entries(['en', 'it'])
#print(fr2en)
translate = dict(en2it)
print(translate['mountain']) #montagna
print(translate['wind']) #vento
print(translate['eat']) #mangiare
print(translate['forest']) #foresta








