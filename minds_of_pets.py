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
    print(f"My pet {pet['name']} takes a walk becomes {pet['weight']}kg.")
    return pet['weight']
    
def sleep(pet):
    pet['energy'] = pet['energy'] + 10
    print(f"My pet {pet['name']}\'s energy level got {pet['energy']} during sleep.")
    return pet['energy']
    
def wake_up(pet):
    print(f"My pet {pet['name']} wakes up and {pet['talk']}!")
    return pet['talk']

def show_photo(pet):
    print(f"My pet {pet['name']} shows a photograph of her '{pet['photo']}'.")
    return pet['photo']
    
def play(pet):
    pet['energy'] = pet['energy'] - 5
    print(f"My pet {pet['name']} plays with {pet['friend']} outside.")
    return pet['friend']
    


#unit test
pet = dog
assert feed(pet) == 7, "pet feed function failed"
assert walk(pet) == 6, "pet walk function failed"
assert sleep(pet) == 20, "pet sleep function failed"
assert wake_up(pet) == 'baffs', "pet wake_up function failed"
assert show_photo(pet) == 'O o O', "pet show_photo function failed"
assert play(pet) == 'Cheese', "pet play function failed"




