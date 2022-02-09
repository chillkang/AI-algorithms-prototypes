#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:04:46 2022

@author: seulkeekang
"""
import nltk
import random 

from nltk.corpus import names
def gender_features(word):
    return {'first_letter': word[0]}

from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
[(name, 'female') for name in names.words('female.txt')])
random.shuffle(labeled_names)

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)
# =============================================================================
# >>> from nltk.tokenize import word_tokenize # or use some other tokenizer
# >>> all_words = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
# >>> t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]
# =============================================================================
# =============================================================================
# import random
# import nltk
# 
# from nltk.corpus import movie_reviews
# documents = [(list(movie_reviews.words(fileid)), category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)]
# print(random.shuffle(documents))
# 
#     #define a feature extractor for documents
#     #limit the number of features that the classifier needs to process to 2000 most frequent words
#     #define a feature extractor that simply checks whether each of these words is present in a given document
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
#     #use feature extractor to train a classifier to label new movie reviews. 
# featuresets = [(document_features(d), c) for (d,c) in documents]
# train_set, test_set = featuresets[100:], featuresets[:100]
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# =============================================================================
# =============================================================================
# 
#     #compute its accuracy on the test set
#     #use show_most_informative_features() to find out which features the classifier found to be most informative.
# print(nltk.classify.accuracy(classifier, test_set))
# classifier.show_most_informative_features(5) 
# =============================================================================
