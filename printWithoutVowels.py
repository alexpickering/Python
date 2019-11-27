#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: taka0
"""
def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = 'aeiou'
    if s != None:
        sCopy = s[:]
        if any(vowels.find(letter.lower()) != -1 for letter in sCopy):
            for letter in sCopy:
                if vowels.find(letter.lower()) != -1:
                    sCopy = sCopy.replace(letter,"")
        print(sCopy)