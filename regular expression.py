from ast import pattern
import re

string = 'hello what are you doing...My name is Dhruv...what you studing... I am learnig python..Ohhh nice its grate...'

# print('what' in string)
pattern = re.compile('what')
a = re.search('what', string)
print(a.span())
print(a.start())
print(a.end())
# Group is usefull when we are trying with multiple searches.
# group only return what ever we search in string.
print(a.group())
b = pattern.findall(string)
print(b)
print('===========================================================================================')
pattern = re.compile(
    'hello what are you doing...My name is Dhruv...what you studing... I am learnig python..Ohhh nice its grate...')
# In full match we need two string and we need to search same string.
# if its different string then its not match string.
c = pattern.fullmatch(string)
print(c)

# in match it doesn't care if we add something in our main string.
# it match the contain which we give to match.
d = pattern.match(string)
print(d)
