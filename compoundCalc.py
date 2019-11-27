#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: taka0
"""
#balance, annualInterestRate, and monthlyPaymentRate are pre-defined

balance = 5000
monthlyPaymentRate = .02
annualInterestRate = .18

def calcMonth(b, mpr, air):
    return (b - (mpr * b)) + ((air/12.0) * (b - (mpr * b)))

for month in range (0,12):
    balance = calcMonth(balance, monthlyPaymentRate, annualInterestRate)

print("Remaining balance: " + str(round(balance, 2)))