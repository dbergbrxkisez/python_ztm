# https://www.w3schools.com/python/python_regex.asp
# https://regex101.com

import re

# compile is going to allow us to get a pattern like 'this'.
pattern = re.compile('this')
pattern2 = re.compile('search this inside of this text please!')
pattern3 = re.compile(r"([a-zA-Z]).([a])")  # r stands for raw string
string = 'search this inside of this text please!'
string2 = 'search this inside of this text please! Dbergbrxkisez'

print('search' in string)

# Returns the match object with all the detais.
# span returns where it occurs in the string. which start at index of 17 and ends at 21.
print(re.search('this', string))

# a = re.search('this', string)
# Instead of doing re.search() I can use pattern
# now I don't need to pass 'this' need to pass only the string.
a = pattern.search(string)

# a = re.search('thIs', string)  # If we do something that doesn't exist it gives AttributeError.

# span tells me where the string occurs as a tuple.
print(a.span())

# start tells me when the text starts.
print(a.start())

# group returns the part of the string where, there was the match.
# group is very useful when we are trying to do multiple searches.
print(a.group())                 # we are going to return a match object or none if it doesn't exist in the string.

print(a.end())                   # It tells me where it ends.

# Now I can use pattern everywhere and use methods on it.

# This does the same as line 11.
print('.search()')
a = pattern.search(string)
print(a)
a2 = pattern3.search(string2)
print(a2.group())                 # I am searching for a letter followed by anything followed by letter a.
print(a2.group(1))                # prints s
print(a2.group(2))                # prints a

# findall finds all the instances of the match.
print('.findall()')
b = pattern.findall(string)       # both instances of 'this' inside of a list.
print(b)

# in order to fullmatch to return a match it has to be the EXACT SAME STRING that we're searching.
print('.fullmatch()')
c = pattern.fullmatch(string)     # returns none if it not the match
c2 = pattern2.fullmatch(string)   # returns the match object
c3 = pattern2.fullmatch(string2)  # returns none because it's not the full match.
print(c2)
print(c3)

# Match just matches the string and it doesn't care what's afterwards.
print('.match()')
d = pattern2.match(string)
print(d)
d2 = pattern2.match(string2)
print(d2)
