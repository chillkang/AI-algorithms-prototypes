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
       'energy': 10,
       'friend': 'Cheese'
       }

pig = {
       'name': 'Cheese',
       'weight': 5,
       'photo': '^ oo ^',
       'talk': 'oinks',
       'energy': 5,
       'friend': 'Doo'
       }

duck = {
        'name': 'Doo',
        'weight': 4,
        'photo': 'O > O',
        'talk': 'quacks',
        'energy': 3,
        'friend': 'Aji'
        }

def feed(pet):
    pet['weight'] = pet['weight'] + 1
    print(f"My pet {pet['name']} eats and becomes {pet['weight']}kg.")
    return pet['weight']
    
def walk(pet):
    pet['weight'] = pet['weight'] - 1
    print(f"My pet {pet['name']} takes a walk with {pet['friend']} and becomes {pet['weight']}kg.")
    return pet['weight'], pet['friend']
    
def sleep(pet):
    pet['energy'] = pet['energy'] + 10
    print(f"My pet {pet['name']}\'s energy level got {pet['energy']} during sleep.")
    return pet['energy']
    
def wake_up(pet):
    print(f"My pet {pet['name']} wakes up and {pet['talk']}!")
    return pet['talk']

def show_photo(pet):
    print(f"My pet {pet['name']}\'s friend {pet['friend']} visits and she shows a photograph of her '{pet['photo']}'.")
    return pet['friend'], pet['photo']
    
def play(pet):
    pet['energy'] = pet['energy'] - 5
    print(f"My pet {pet['name']} {pet['talk']}! It's because her energy level got {pet['energy']} and became hungry after playing.")
    return pet['energy']
    
feed(dog)
walk(dog)
sleep(dog)
wake_up(dog)
show_photo(dog)
play(dog)



