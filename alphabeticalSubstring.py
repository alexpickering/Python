#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

@author: taka0
"""

#s = 'abcabcdabcdeaxaza'
#s = 'azcbobobegghakl'
#s = 'abcbcd'
lindex = 0 #index of longest substring's first char
lmax = 0 #length of longest substring

for index1 in range(0,len(s)):
    tempmax = 0
    #print(str(index1) + " " + str(index2) + " --line 28")
    for index2 in range(0,len(s) - index1):
        #print(str(index1) + " " + str(index2) + " --line 30")
        if (index1 + index2 + 1 < len(s) and (s[index1 + index2] <= s[index1 + index2 + 1])):
            #print(s[index1 + index2] + " " + s[index1 + index2 + 1])
            #print(str(index1) + " " + str(index2) + " --line 33")
            tempmax += 1
            #print("tempmax is " + str(tempmax))
        else:
            break
    if(tempmax > lmax):
        lindex = index1
        lmax = tempmax
   # print("Exiting inner loop")
#print(lindex)
#print(lmax)
print("Longest substring in alphabetical order is: " + s[lindex : lindex + lmax + 1])
    