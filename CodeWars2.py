"""
CodeWars lvl 7kyu

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

def get_count(sentence):
    a = 0
    nums = 0
    while a < len(sentence):
        if(sentence[a] == "a" or sentence[a] == "e" or sentence[a] == "i" or sentence[a] == "o" or sentence[a] == "u"):
            nums += 1
        a += 1
    return nums
