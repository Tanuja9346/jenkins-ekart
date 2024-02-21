# sample_tuple = ('a', 'b', 'c', 'd')  
# print(sample_tuple[0])--through index fetch value
# print(sample_tuple[-1])

# a, b = (1, 2)---assign value
# print(a, b)

# sample_tuple = ('a',)--consider a value

# sample_tuple = ('a', 'b', 'c', 'd')
# sample_tuple[0] = 'abc'-->replace/alter value not support
# print(sample_tuple)

sample_tuple = ('a', 'a', 'b', 'c', 'd')
print(sample_tuple.index('a'))
print(sample_tuple.count('a'))