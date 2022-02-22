# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:39:20 2020

@author: surenjayasuriy
"""
import nltk
import random
import re
from nltk.corpus import wordnet, swadesh, names
from nltk.book import *

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageChops


# Ask the user for input
a =  input('User: ')

# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up")

GREETING_RESPONSES = ["'sup", "hey", "*nods*", "hey you get my text?"]

APHORISM_RESPONSES = ["It always seems impossible until it's done.", "Happiness is found within.", 
                      "You only fail if you quit.", "Keep looking up.. that's the secret of life."]

#If any of the words in the user's input was a greeting, return a greeting response
def check_for_greeting(sentence):
    for word in sentence.split(" "):
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)
  
# Example: check for a word "dog" and respond to it.  
def check_for_phrase(sentence):
    KEYPHRASES = ["dog"]
    for word in sentence.split(" "):
        if word in KEYPHRASES:
            return "This is my response to dog."
          
# Example: check for a word "cat" and respond to it.  
def check_for_cat(sentence):
    KEYPHRASES = ["cat"]
    for word in sentence.split(" "):
        if word in KEYPHRASES:
            return "This is my response to cat."

# Example: get your chatbot to tell a story. The \n command
# starts a new line (useful to make the ouptut readable.)
def tellstory(sentence):
    KEYPHRASES = ["story", "story."]
    for word in sentence.split(" "):
        if word in KEYPHRASES:
            return "Here is my story.. \n Once upon a midnight dreary, while I pondered, weak and weary,\n Over many a quaint and curious volume of forgotten lore,--\n While I nodded, nearly napping, suddenly there came a tapping,\n As of some one gently rapping, rapping at my chamber door.\n 'T is some visitor.' I muttered, tapping at my chamber door--\n Only this, and nothing more.\n"

# Example: get your chatbot to tell a joke. 
def tell_aphorism(sentence):
    KEYPHRASES = ["aphorism"]
    for word in sentence.split(" "):
        if word in KEYPHRASES:
            return random.choice(APHORISM_RESPONSES)
        
# Example: check for a word "favorite" and "author", and respond to it.  
def check_for_author(sentence):
    KEYPHRASES = ["favorite", "author", "author?"]
    for word in sentence.split(" "):
        if word in KEYPHRASES:
            return "It's Edgar Allen Poe."
        
# Example: check for a "definition" for a word "intelligence", and respond to it.  
def check_for_definition(sentence):
    KEYPHRASES = ["intelligence", "intelligence?"]
    syn = wordnet.synsets('intelligence')
    for word in sentence.split(" "):
        if word in KEYPHRASES:
            return syn[0].definition()

# Example: translate the word "wind" to Italian.  
def translate(sentence):
    KEYPHRASES = ["translate", "italian", "wind"]
    en2it = swadesh.entries(['en', 'it'])
    translate = dict(en2it)
    for word in sentence.split(" "):
        if word in KEYPHRASES:
            return translate['wind']
        
# Example: get your chatbot to tell you a list of books it read.
def tell_booktitle(sentence):
    KEYPHRASES = ["text", "books", "texts", "a list of books", "books?", "read?" ]
    for word in sentence.split(" "):
        if word in KEYPHRASES:
            return texts()
        
# Example: get your chatbot to show love.        
def show_love(sentence):
    KEYPHRASES = ["love", "heart", "mind"]
    for word in sentence.split(" "):
       if word in KEYPHRASES:
           return "\U0001F497"	
       
# Example: get your chatbot to show how it looks like.        
def look_like(sentence):
    KEYPHRASES = ["how do you look like", "look like", "show your body", "your body", "look"]
    for word in sentence.split(" "):
       if word in KEYPHRASES:
           return "  [00] \n      /| \U0001F497 |\  \n        d  b  "	
       
# Example: check for a word "moody", and respond to it. 
def show_hot_choco(sentence):
    KEYPHRASES = ["moody", "bored", "sleepy", "sweet", "sad", "frustrated", "miserable" ]
    for word in sentence.split(" "):
        if word in KEYPHRASES:
            return "Get some hot chocolate :) \n         / / /   \n      ___\_\_\___   \n      /         \ \n      \_________/\n      |         |\n      |         |\n      |   HOT   |\n      |  CHOCO  |\n      |         |\n      |         |\n      \_________/"

# Example: check for a word "fist letter" for male names. 
def gender_features(word):
    return {'first_letter': word[0]}

labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
[(name, 'female') for name in names.words('female.txt')])
random.shuffle(labeled_names)

# Example: check for a word "fist letter" for male names and respond to it. 
def show_gender(sentence):
    featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    KEYPHRASES = ["gender", "gender of this name", "male?", "female?"]
    for word in sentence.split(" "):
        if word in KEYPHRASES:
            return classifier.classify(gender_features('Wally'))
        
# Example: check for a word "city" and respond to it. 
def show_city(sentence):
    KEYPHRASES = ["image", "city", "cities", "images?", "city?", "cities?"]
    for word in sentence.split(" "):
       if word in KEYPHRASES:
           return "Which city do you want to see?"

# Example: check for a word "Florence" and respond to it. 
def show_florence(sentence):
    img = cv2.imread('florence.jpeg')
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    KEYPHRASES = ["florence", "Florence", "Florence?", "florence?"]
    for word in sentence.split(" "):
       if word in KEYPHRASES:
           plt.imshow(img_rgb)
           plt.show()
           return "Check the plots!"

# Example: check for a word "London" and respond to it. 
def show_london(sentence):
    img = cv2.imread('london.jpeg')
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    KEYPHRASES = ["london", "London", "London?", "london?"]
    for word in sentence.split(" "):
       if word in KEYPHRASES:
           plt.imshow(img_rgb)
           plt.show()
           return "Check the plots!"

# Example: check for a word "Seoul" and respond to it. 
def show_seoul(sentence):
    img = cv2.imread('seoul.jpeg')
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    KEYPHRASES = ["seoul", "Seoul", "Seoul?", "seoul?"]
    for word in sentence.split(" "):
       if word in KEYPHRASES:
           plt.imshow(img_rgb)
           plt.show()
           return "Check the plots!"
       
# Example: check for a word "Amsterdam" and respond to it. 
def show_amsterdam(sentence):
    img = cv2.imread('amsterdam.jpeg')
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    KEYPHRASES = ["amsterdam", "Amsterdam", "Amsterdam?", "amsterdam?"]
    for word in sentence.split(" "):
       if word in KEYPHRASES:
           plt.imshow(img_rgb)
           plt.show()
           return "Check the plots!"
       
# Example: check for words "London" and "weather" respond to it. 
def show_weather(sentence):
    img_gray = cv2.imread('london.jpeg', cv2.IMREAD_GRAYSCALE)
    img_rgb = cv2.cvtColor(img_gray, cv2.COLOR_BGR2RGB)
    KEYPHRASES = ["weather?", "weather"]
    for word in sentence.split(" "):
       if word in KEYPHRASES:
           plt.imshow(img_rgb)
           plt.show()
           return "It's very foggy. You might need an umbrella today."
      
# Example: check for words "green" and respond to it. 
def show_greensky(sentence):
    img_green = cv2.imread('london.jpeg', cv2.IMREAD_GRAYSCALE)
    KEYPHRASES = ["green", "green?"]
    for word in sentence.split(" "):
       if word in KEYPHRASES:
           plt.imshow(img_green)
           plt.show()
           return "Of course. I will show you here."

# Example: check for a word "sunset" and respond to it. 
def show_sunset(sentence):
    img = cv2.imread('seoul.jpeg')
    KEYPHRASES = ["sunset", "sunset?"]
    for word in sentence.split(" "):
       if word in KEYPHRASES:
           plt.imshow(img)
           plt.show()
           return "Isn't this beautiful?"
       
# Example: check for a word "bridge" and respond to it. 
def show_bridge(sentence):
    img = cv2.imread('florence.jpeg')
    cropped_img = img[200:600, 100:1300]
    img_rgb = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
    KEYPHRASES = ["bridge", "bridge?"]
    for word in sentence.split(" "):
       if word in KEYPHRASES:
          plt.imshow(img_rgb)
          plt.show()
          return "It's the Ponte Vecchio. It was built in the 14th century."

# Example: check for words "architecture" and "style" and respond to it. 
def show_canal_houses(sentence):
    img = cv2.imread('amsterdam.jpeg')
    cropped_img = img[80:500, 150:900]
    img_rgb = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
    KEYPHRASES = ["architecture", "architecture?", "style", "style?"]
    for word in sentence.split(" "):
       if word in KEYPHRASES:
          plt.imshow(img_rgb)
          plt.show()
          return "The archetectural style is Dutch Baroque. The narrow townhouses line Amsterdam's 17th century canal rings."
       

# Reflections swap the users pronouns back at them. For instance, if the user
# says: "I need you". The response will flip "I -> you", "you -> me", so the 
# bot will say "you need me". 
reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# This function looks for the starting phrase, and then takes the rest of the 
# user's sentence after the phrase and puts it in variable 0
psychobabble = [
    [r'I need (.*)',
     ["Why do you need {0}?",
      "Would it really help you to get {0}?",
      "Are you sure you need {0}?"]],
    
    [r'Who are you?',
     ["Insert Biography"]], 
    
    [r'I like (.*)',
     ["Why do you like {0}?"]],
 
    [r'Why don\'?t you ([^\?]*)\??',
     ["Do you really think I don't {0}?",
      "Perhaps eventually I will {0}.",
      "Do you really want me to {0}?"]],
      
    [r'I want (.*)',
     ["TEST"]],
    # This must be the last block
    [r'(.*)',
     ["Please tell me more.",
      "Let's change focus a bit... Tell me about your family.",
      "Can you elaborate on that?",
      "Why do you say that {0}?",
      "I see.",
      "Very interesting.",
      "{0}.",
      "I see.  And what does that tell you?",
      "How does that make you feel?",
      "How do you feel when you say that?"]],
      
]    
     
def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)
 
def analyze(statement):
    for pattern, responses in psychobabble:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])


## This is the main part of the Chatbot code, checks for phrases, words, and 
## prints responses
while (a.split(" ")[0] != 'bye' and a.split(" ")[0] != 'Bye'):
    spoke = 0
    z =  check_for_greeting(a)
    if z != None:
        print('Bot: ', z)
        spoke = 1
    z = check_for_phrase(a)
    if z!= None:
        print('Bot: ', z)
        spoke = 1
    z = check_for_cat(a)
    if z!= None:
        print('Bot: ', z)
        spoke = 1  
    z = tellstory(a)
    if z!= None:
        print('Bot: ', z)
        spoke = 1
    z = tell_aphorism(a)
    if z!= None:
        print('Bot: ', z)
        spoke = 1
    z = check_for_author(a)
    if z!= None:
        print('Bot: ', z)
        spoke = 1
    z = check_for_definition(a)
    if z!= None:
         print('Bot: ', z)
         spoke = 1
    z = translate(a)
    if z!= None:
         print('Bot: ', z)
         spoke = 1
    z = tell_booktitle(a)
    if z!= None:
         print('Bot: ', z)
         spoke = 1
    z = show_love(a)
    if z!= None:
         print('Bot: ', z)
         spoke = 1
    z = look_like(a)
    if z!= None:
        print('Bot: ', z)
        spoke = 1
    z = show_hot_choco(a)
    if z!= None:
        print('Bot: ', z)
        spoke = 1
    z = show_gender(a)
    if z!= None:
        print('Bot: ', z)
        spoke = 1
    z = show_city(a)
    if z!= None:
        print('Bot: ', z)
        spoke = 1
    z = show_florence(a)
    if z!= None:
        print('Bot: ', z)
        spoke = 1
    z = show_london(a)
    if z!= None:
        print('Bot: ', z)
        spoke = 1
    z = show_seoul(a)
    if z!= None:
        print('Bot: ', z)
        spoke = 1
    z = show_amsterdam(a)
    if z!= None:
        print('Bot: ', z)
        spoke = 1
    z = show_weather(a)
    if z!= None:
         print('Bot: ', z)
         spoke = 1 
    z = show_greensky(a)
    if z!= None:
         print('Bot: ', z)
         spoke = 1 
    z = show_sunset(a)
    if z!= None:
         print('Bot: ', z)
         spoke = 1 
    z = show_bridge(a)
    if z!= None:
         print('Bot: ', z)
         spoke = 1 
    z = show_canal_houses(a)
    if z!= None:
         print('Bot: ', z)
         spoke = 1 
    
    if spoke == 0:
        print('Bot: ', analyze(a))
    
    a = input('User: ')
    
    
    
    
    