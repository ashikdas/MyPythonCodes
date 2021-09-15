# This program will counts the frequency of characters on a string.

import pprint as pp
text = 'This a simple text to TEST the code.'

letters = {}

for i in text:
    letters.setdefault(i, 0)
    letters[i] = letters[i]+1

pp.pprint(letters)