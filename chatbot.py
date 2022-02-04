# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:39:20 2020

@author: surenjayasuriya
"""

import random
import re
import nltk


# Ask the user for input
a =  input('User: ')

# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup", "hey", "*nods*", "hey you get my text?"]

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
    KEYPHRASES = ["story"]
    for word in sentence.split(" "):
        if word in KEYPHRASES:
            return "Here is my story \n It was a dark and stormy night..."
          
   
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
while (a.split(" ")[0] != 'quit' and a.split(" ")[0] != 'Quit'):
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
    
    if spoke == 0:
        print('Bot: ', analyze(a))
    
    a = input('User: ')