#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: taka0
"""
#balance and annualInterestRate are pre-defined

balance = 5000
annualInterestRate = .18
lowPay = 0


def calcMonth(b, mpr, air, n):
    for month in range (0,n):
        b = (b - (mpr * b)) + ((air/12.0) * (b - (mpr * b)))
    return b

def calcRecur(b, mpr, air):
    if b >= : balance
        return b
    else:
        return 
    
lowPay = calcRecur(balance, lowPay, annualInterestRate)

print("Lowest Payment: " + str(round(lowPay, -1)))