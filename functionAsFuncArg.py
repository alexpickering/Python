#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: taka0
"""

def f(highest, second):
    return highest + second

def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    scoreList = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = word.lower()
    for x in range(0, len(word)):
        scoreList.append((alphabet.find(word[x]) +1) * x)
    scoreList.sort()        
    return f(scoreList[-1],scoreList[-2])