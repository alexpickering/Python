#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: taka0
"""
high = 100
low = 1
x = ''

while x != 'c':
    guess = (high + low) // 2
    print("Is your secret number " + str(guess) + "?", end ='')
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. \n")
    print(end ="")
    if(x == 'h'):
        high = guess
    elif(x == 'l'):
        low = guess
    elif(x == 'c'):
        break
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: " + str(guess))