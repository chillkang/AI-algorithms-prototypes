#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:21:58 2022

@author: seulkeekang
"""
# I first imported random module for generating a random choice of computer. For user interface, the program prints out a game instruction.
# I defined possible_actions (“rock”, “scissors”, and “paper”) for playing a game and generated one choice out of these three actions for computer_action.
# I defined user_action (user’s possible input) as “rock”, “scissors”, and “paper” to compete against computer_action.

import random

print ("This is a 'Rock, Scissors, Paper' game. \nType 'rock', 'scissors', or 'paper' to play the game, and 'end' to finish it!")

possible_actions = ["rock", "scissors", "paper"]
computer_action = random.choice(possible_actions)
user_action = ["rock", "scissors", "paper"]

# I wrapped if statements with a while loop to finish the game when user’s input is “end”.
# After an input prompt, the if statements are evaluated based on user_action. There are 4 scenarios here. 
# 1) If user_action is same as computer_action, it ’s a tie. The program prints out user_action and tells the user it’s a tie.
# 2) If user_action is “rock”, the expression is evaluated based on what the computer_action is. The program prints out whether the user wins or loses the game.
# 3-4) The logic works the same when user_action is “scissor” or “paper”.
# For user interface, if user_action was either “rock”, “scissor”, or “paper, the program prints out what user_action and computer_action were. 
# When user’s input is “end”, the while loop stops iterating.

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

# For user interface, if user_action is “end”, the program prints out that the user ended the gam

if user_action == "end":
    print("\nYou ended the game!")
