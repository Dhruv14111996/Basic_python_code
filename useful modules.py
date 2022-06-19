from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 5, 6, 4]
sentence = 'blah blah blah just thinking about python.'

print(Counter(li))
print(Counter(sentence))

# In default dict if we give some value which not in main dict the it throughs error.
# But if we use lambda dunction and we give value out of dict so it count lambda as a default.
Dict = defaultdict(lambda: 6, {'a': 1, 'b': 2, 'c': 3})
# As we can see here we call 'e' which not in main dict but it count lambda as a defaultdict.
print(Dict['e'])

# In order dict it check the order sf dict if its match ans true else false.
d = {'c': 100}
d['a'] = 1
d['b'] = 2

d2 = {'c': 100}
d2['b'] = 2
d2['a'] = 1

print(d2 == d)
