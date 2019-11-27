#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: taka0
"""
#balance and annualInterestRate are pre-defined

balance = 5000
annualInterestRate = .18
high = balance
low = 0
minPay = balance // 2



def calcMonth(b, minPay, air, n):
    for month in range (0,n):
        b = (b - minPay + ((air/12.0) * (b - minPay)))
    return b

while True:
    minPay = (high + low) // 2
    yearResult = round(calcMonth(balance, minPay, annualInterestRate, 12),-1)
    if yearResult > 0:
        low = minPay
    elif yearResult < 0:
        high = minPay
    elif yearResult == 0:
        break
    print(str(calcMonth(balance, minPay, annualInterestRate, 12)))
    yearResult = round(calcMonth(balance, minPay, annualInterestRate, 12),-1)


print("Lowest Payment: " + str(round(minPay, -1)))