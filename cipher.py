#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: taka0
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    decoded = ''
    key_code = {}
    for i in range(0,len(map_from)): #builds dictionary
        key_code[map_from[i]] = map_to[i]
        
    for char in code: #creates decoded string
        if char in key_code:
            decoded += key_code[char]
        else:
            decoded += char
    
    return (key_code, decoded) #returns tuple