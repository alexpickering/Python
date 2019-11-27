#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: taka0
"""

balance = 1200
annualInterestRate = 0.05
high = (balance * (1 + (annualInterestRate/12.0))**12)/12.0
low = balance / 12
minPay = (high + low) / 2

def calcMonthR(b, minPay, air, n, i):
    return (b if (i <= 0) else calcMonthR(b - minPay + ((air/12.0) * (b - minPay)), minPay, air, n, i-1))

minPay = calcMonthR(balance, minPay, annualInterestRate, 12, 12)
while (minPay > 0.01 or minPay < -0.01):
    minPay = calcMonthR(balance, minPay, annualInterestRate, 12, 12)
    if minPay > 0.01: 
        low = minPay 
    elif minPay < -0.01: 
        high = minPay
    minPay = (high + low) / 2
print("Lowest Payment: " + str(round(minPay, 2)))