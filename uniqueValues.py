#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: taka0
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns list of
    keys that
    map to unique values
    ascending order
    '''
    returnList = []
    if (len(aDict) == 0):
        return []
    valueList = list(aDict.values())
    keyList = list(aDict.keys())
    for key, value in aDict.items():
        if valueList.count(value) == 1:
            returnList.append(key)
    returnList.sort()
    return returnList