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