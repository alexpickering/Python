#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: taka0
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    #print('called')
    length = len(L)
    if not length > 1: #handles lists of lengths fewer than two
        if length == 1:
            return L[0]
        else:
            return 0
    topRun, topSum, current, currentSum = 0, 0, 0, 0
    #print('values assigned')
    for i in range(0,length): 
        
        #print('i loop entered ' + str(i))
        
        if topRun >= (length-i): #checks to see if larger run is possible in leftover list
            return topSum
        
        #print('check passed')
        
        j = i  #monotonically increasing test
        current = 1
        currentSum = L[j]
        while j+1 < length and (L[j] <= L[j+1]):
            current += 1
            currentSum += L[j+1]
            j += 1
        if current > topRun:
            topRun = current
            topSum = currentSum
            
        #print('mono inc passed ' + str(topSum))
        
        
        j = i  #monotonically decreasing test
        current = 1
        currentSum = L[j]
        while j+1 < length and (L[j] >= L[j+1]):
            current += 1
            currentSum += L[j+1]
            j += 1
        if current > topRun:
            topRun = current
            topSum = currentSum
            
        #print('mono dec passed ' + str(topSum))
    return topSum
        
    
    
    
    