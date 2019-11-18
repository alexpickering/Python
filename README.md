# Python
Experiments in Python



## sink_blob.py

### Summary
This program is a translation of the Scheme file, sink_blob.rkt, primarily as a way to discover the differences in list management
between Scheme and Python.

### Description
Start program with main(), after which
- request_list() prompts the user for up to LIST_SIZE values, and returns values as a list
- print_lob() prints this list in abbreviated form
- find_b_count() returns the number of bubbles in the list
- sink() moves all solids 1 position lower on the list if they are before bubbles.
- print_lob() prints the final list order in abbreviated form
