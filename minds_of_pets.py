#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 21:50:19 2022

@author: seulkeekang
"""

dog = {
       'name': 'Aji',
       'weight': 6,
       'photo': 'O o O',
       'talk': 'baffs',
       'energy': 10
       }

pig = {
       'name': 'Cheese',
       'weight': 5,
       'photo': '^ oo ^',
       'talk': 'oinks',
       'energy': 5
       }

duck = {
        'name': 'Doo',
        'weight': 4,
        'photo': 'O > O',
        'talk': 'quacks',
        'energy': 3
        }

def feed(pet):
    pet['weight'] = pet['weight'] + 1
    print(f"My pet, {pet['name']} eats and becomes {pet['weight']}kg.")
    return pet['weight']
    
def walk(pet):
    pet['weight'] = pet['weight'] - 1
    return pet['weight']
    
def sleep(pet):
    pet['energy'] = pet['energy'] + 10
    return pet['energy']
    
def wake_up(pet):
    print(f"My pet, {pet['name']} wakes up and", pet['talk'], "!")
    return pet['talk']
    
def play(pet):
    pet['energy'] = pet['energy'] - 5
    return pet['energy']
    
feed(dog)
feed(dog)
wake_up(dog)



