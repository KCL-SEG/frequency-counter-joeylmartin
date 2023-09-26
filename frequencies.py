"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for temp in items:
        word = str(temp)
        if word in frequencies.keys():
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    
    # Your code goes here
    return frequencies


