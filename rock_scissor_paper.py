#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:21:58 2022

@author: seulkeekang
"""

import random

print ("This is a Rock, Scissors, Paper game. Type 'Rock', 'Scissors', or 'Paper' to play the game, and 'end' to finish the it!")

possible_actions = ["rock", "scissors", "paper"]
computer_action = random.choice(possible_actions)

user_action = input("Enter a choice (rock, scissors, paper): ")
      
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")