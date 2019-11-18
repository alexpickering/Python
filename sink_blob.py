"""
sink_blob.py
Author: Alex Pickering
Date: 20191030

Python 3
Adapts Scheme code to Python
 - shows differences in list manipulation between languages
 - simulates gradually sinking solids in list of solids and bubbles

@author: taka0
"""

# Global variables
LIST_SIZE = 6
B = "bubble"
S = "solid"


def main():
    lob = request_list()
    print_lob(lob)
    b_count = find_b_count(lob)
    sink(b_count, lob)
    print_lob(lob)
    
    
# request user input for list of blobs
def request_list():
    lob = [""] * LIST_SIZE
    print("Enter blank value when complete")
    i = 0
    # (LIST_SIZE - 1) because list should always end with an empty value
    while i < (LIST_SIZE - 1):
        lob[i] = input("Enter list item %d: " % (i + 1))
        if lob[i] == 'B' or lob[i] == 'b':
            lob[i] = B
        elif lob[i] == 'S' or lob[i] == 's':
            lob[i] = S
        elif lob[i] == '' or lob[i] == 'E' or lob[i] == 'e':
            break
        i += 1
    return lob

# find bubble count in list
def find_b_count(lob):
    b_count = 0
    for blob in lob:
        if blob == B:
            b_count += 1
    return b_count
    

# find bubbles after solids, and swap
def sink(b_count, lob):
    i = 0
    temp = ""
    while i < LIST_SIZE and b_count > 0 and lob[i] != '':
        if lob[i] == S:
            # j is the end of the consecutive solids
            j = i + 1
            while lob[j] != B:
                j += 1
            # swap values, "bubbling" the bubble value to the top
            temp = lob[i]
            lob[i] = lob[j]
            lob[j] = temp
            i = j
        b_count -= 1
        i += 1
    return lob


# prints list in abbreviated format
def print_lob(lob):
    if len(lob) < 1:
        return 0
    for blob in lob:
        if blob == B:
            print("B", end = ' ')
        elif blob == S:
            print("S", end = ' ')
        else:
            print("")
            #print("E")
            break