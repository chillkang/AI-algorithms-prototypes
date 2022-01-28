#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 17:05:23 2022

@author: seulkeekang
"""

from enum import Enum
 
class Direction(Enum):
    Left = 1
    Right = 2
    Neutral = 3
    
class Tape:
    def __init__(self, word, alphabet):
        self.alphabet = alphabet + "$#"       
        self.head_position = 0
        self.__init_tape(word)
 
    def __init_tape(self, word):
        tape = "$";
        for char in (c for c in word if c in self.alphabet):
            tape += char
        tape += "#";
        self._tape = list(tape)
        
    def write(self, character):
        if self.head_position < 1 or character not in self.alphabet:
            return
        self._tape[self.head_position] = character
 
        last_item_index = len(self._tape) - 1
        if self.head_position == last_item_index:
            self._tape += '#'
            
    def read(self):
        return self._tape[self.head_position]
    
    def get_tape(self):
        self._remove_trailing_sharps()
        return ''.join(self._tape)
    
    def _remove_trailing_sharps(self):
        for i in range(len(self._tape) - 1, 1, -1):
            if self._tape[i] == '#' and self._tape[i-1] == '#':
                del self._tape[-1:]
            else:
                break
            
    def move_head(self, direction):
        if direction == Direction.Right:
            self.head_position += 1
        elif direction == Direction.Left:
            self.head_position -= 1
 
        if self.head_position > len(self._tape) - 1:
            self._tape += '#'
        if self.head_position < 0:
            self.head_position = 0
            
    def get_length(self):
        return len(self._tape)

class StateType(Enum):
    Start = 1
    Final = 2
    Empty = 3
 
class State:
    def __init__(self, id, state_type):
        self.id = id
        self.type = state_type
        
class Transition:
    def __init__(self, current_state, current_char, new_state, new_char, direction):
        self.current_state = current_state
        self.current_char = current_char
        self.new_state = new_state
        self.new_char = new_char
        self.direction = direction
        
class TuringMachine:
    def __init__(self, states, transitions, tape):
        self.states = states
        self.start_state = self.get_start_state()
        self.transitions = transitions
        self.tape = tape
        
    def get_tape(self):
        return self.tape.get_tape()
 
    def get_start_state(self):
        return next(state for state in self.states if state.type == StateType.Start)
    
    def process(self, verbose=False):
        current_state = self.start_state
        step = 0
        self._log_process(step)
 
        while current_state.type != StateType.Final:
            current_char = self.tape.read()
            state_id = current_state.id
 
            transition = next(t for t in self.transitions
                              if t.current_state == state_id
                              and t.current_char == current_char)
 
            current_state = next(state for state in self.states if state.id == transition.new_state)
 
            self.tape.write(transition.new_char)
            self.tape.move_head(transition.direction)
            
            step += 1
            self._log_process(step)
 
    def _log_process(self, step):
        print('\nTape after step {0}: '.format(step))
        print('[', end='')
     
        for i in range(0, self.tape.get_length()):
            if self.tape.head_position == i:
                print("\033[4m" + self.tape._tape[i] + "\033[0m", end='')
            else:
                print(self.tape._tape[i], end='')
     
        print(']')
         
#tape = Tape('|||&||', '|&')
#states = [
            #State("s0", StateType.Start),
            #State("s1", StateType.Empty),
            #State("s2", StateType.Empty),
            #State("s3", StateType.Empty),
            #State("s4", StateType.Empty),
            #State("sf", StateType.Final)
         #]
 
#transitions = [
                 #Transition("s0", "$", "s1", "$", Direction.Right),
                 #Transition("s1", "#", "sf", "#", Direction.Neutral),
                # Transition("s1", "|", "s1", "|", Direction.Right),
                 #Transition("s1", "&", "s2", "|", Direction.Right),
                 #Transition("s2", "|", "s2", "|", Direction.Right),
                 #Transition("s2", "#", "s3", "#", Direction.Left),
                 #Transition("s3", "|", "s4", "#", Direction.Left),
                 #Transition("s4", "|", "s4", "|", Direction.Left),
                 #Transition("s4", "$", "sf", "$", Direction.Neutral),
              #]
 
#tm = TuringMachine(states, transitions, tape)
#tm.process(True)
 
tape = Tape('|||#||', '|&')
states = [
            State("s0", StateType.Start),
            State("s1", StateType.Empty),
            State("s2", StateType.Empty),
            State("s3", StateType.Empty),
            State("s4", StateType.Empty),
            State("s5", StateType.Empty),
            State("s6", StateType.Empty),
            State("s7", StateType.Empty),
            State("s8", StateType.Empty),
            State("sf", StateType.Final)
         ]
 
transitions = [
                 Transition("s0", "$", "s0", "$", Direction.Right),
                 Transition("s0", "#", "sf", "#", Direction.Neutral),
                 Transition("s0", "|", "s1", "|", Direction.Right),
                 Transition("s1", "|", "s1", "|", Direction.Right),
                 Transition("s1", "#", "s2", "#", Direction.Right),
                 Transition("s2", "#", "s2", "#", Direction.Right),
                 Transition("s2", "|", "s3", "|", Direction.Right),
                 Transition("s3", "|", "s4", "|", Direction.Left),
                 Transition("s3", "#", "s6", "#", Direction.Left),
                 Transition("s4", "|", "s5", "#", Direction.Left),
                 Transition("s5", "#", "s5", "#", Direction.Left),
                 Transition("s5", "|", "s2", "#", Direction.Right),
                 Transition("s5", "$", "s2", "$", Direction.Right),
                 Transition("s6", "|", "s7", "#", Direction.Left),
                 Transition("s7", "#", "s7", "#", Direction.Left),
                 Transition("s7", "$", "sf", "$", Direction.Neutral),
                 Transition("s7", "|", "s8", "#", Direction.Left),
                 Transition("s8", "|", "s8", "|", Direction.Left),
                 Transition("s8", "$", "sf", "$", Direction.Neutral)
              ]
 
tm = TuringMachine(states, transitions, tape)
tm.process(True)