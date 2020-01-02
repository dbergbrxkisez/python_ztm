from collections import Counter, defaultdict, OrderedDict

# Counter creates a counter object that keeps track of how many times an item occured in an iterable.
# li = [1, 2, 3, 4, 5, 6, 7]
# sentence = 'blah blah blah thinking about python'
#
#
# print(Counter(li))
# print(Counter(sentence))


# # Default dictionary gives a default value if it doesn't exist.
# dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
# print(dictionary['a'])
# # print(dictionary['c'])
# # print(int())
# print(dictionary['c'])


#OrderedDict =  Retains the order that you insert into a dictionary
# A dictionary has no sense of order
# in case of OrderedDict() we get the same order. If not in same order, it gives false.
d = OrderedDict()
# d = {'c': 100}
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
# d2 = {'c': 100}
d2['b'] =2
d2['a'] = 1

print(d2 == d)




