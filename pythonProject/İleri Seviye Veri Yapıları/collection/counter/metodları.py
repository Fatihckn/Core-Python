from collections import Counter

c = Counter('abcdeabcdabcaba')

print(c.most_common(3))

c.update('aaabbb')
print(c.most_common(3))

c.subtract('abc')
print(c.most_common(3))

list_of_elements = list(c.elements())
print(list_of_elements)

c.clear()
print(c)