#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:21:58 2022

@author: seulkeekang
"""

import random

print ("This is a 'Rock, Scissors, Paper' game. \nType 'rock', 'scissors', or 'paper' to play the game, and 'end' to finish it!")

possible_actions = ["rock", "scissors", "paper"]
computer_action = random.choice(possible_actions)
user_action = ["rock, scissors", "paper"]

while user_action != "end":
    
    user_action = input("Enter a choice (rock, scissors, paper, or end):")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    if user_action != "end":
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")    

if user_action == "end":
    print("\n You ended the game!")
