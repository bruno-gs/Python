import re

# this is the song in the example
lyrics = '''
12 Drummers Drumming
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree
'''

# \s -- for spacebar | tab
# \w -- texts -- letters
# '+' for one or more appears
xmasRegex = re.compile(r'\d+\s\w+')
# return the list of the strings with the pattern (all of them)
print(xmasRegex.findall(lyrics))

# create your own needs
vowelRegex = re.compile(r'[aeiouAEIOU]') # same as r'[a|e|i|o|u ...]' 
print(vowelRegex.findall('Robocop eats baby food'))

doublevowelRegex = re.compile(r'[aeiouAEIOU]{2}') # when 2 vowels appear in sequence
print(doublevowelRegex.findall('Robocop eats baby food'))

# the '^' is the negative, then all will be find, less the pattern
consonantRegex = re.compile(r'[^aeiouAEIOU]') # same as r'[a|e|i|o|u ...]' 
print(consonantRegex.findall('Robocop eats baby food'))