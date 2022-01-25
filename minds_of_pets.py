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
        'energy': 3,
        }

def feed(pet):
    pet['weight'] = pet['weight'] + 1
    print(f"{pet['name']} eats and becomes {pet['weight']}kg.")
    return pet['weight']
    
def walk(pet):
    pet['weight'] = pet['weight'] - 1
    print(f"{pet['name']} takes a walk outside becomes {pet['weight']}kg.")
    return pet['weight']
    
def sleep(pet):
    pet['energy'] = pet['energy'] + 10
    print(f"{pet['name']}\'s energy level got {pet['energy']} during sleep and {pet['name']} is ready to play.")
    return pet['name'], pet['energy']
    
def wake_up(pet):
    print(f"{pet['name']} wakes up and {pet['talk']}!")
    return pet['name'], pet['talk']

def show_photo(pet):
    print(f"{pet['name']} shows a photograph of her '{pet['photo']}'.")
    return pet['name'], pet['photo']
    
def play(pet, pet2):
    pet['energy'] = pet['energy'] - 3
    print("%s plays with her friend %s outside and got hungry because her enerygy level got %s." %(pet['name'], pet2['name'], pet['energy']))
    return pet['name'], pet2['name'], pet['energy']
    
def meet_together(pet, pet2, pet3):
    print("%s, %s, and %s meet together and go to a picnic." %(pet['name'], pet2['name'], pet3['name']))
    return pet['name'], pet2['name'], pet3['name']


#unit test
pet = dog
pet2 = pig
pet3 = duck
assert feed(pet) == 7, "pet feed function failed"
assert walk(pet) == 6, "pet walk function failed"
assert sleep(pet) == ('Aji', 20), "pet sleep function failed"
assert wake_up(pet) == ('Aji','baffs'), "pet wake_up function failed"
assert show_photo(pet) == ('Aji','O o O'), "pet show_photo function failed"
assert play(pet, pet2) == ('Aji', 'Cheese', 17), "pet play function failed"
assert meet_together(pet, pet2, pet3) == ('Aji', 'Cheese', 'Doo'), "pet meet function failed"






