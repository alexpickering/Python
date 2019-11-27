#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: taka0
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) < 1 or (len(aStr) == 1 and char != aStr[0]): #checks for empty string or single char string that doesn't match
        return False
    elif char == aStr[len(aStr)//2]: #checks for match
        return True
    elif char < aStr[len(aStr)//2]:
        return isIn(char, aStr[:len(aStr)//2]) #re-establishes 'high' parameter
    else:
        return isIn(char, aStr[len(aStr)//2:]) #re-establishes 'low' parameter