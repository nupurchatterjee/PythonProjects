import re

patterns = ['term1', 'term2']

text = "This is a string with term1, not for term or term2"

match = re.search(patterns[0], text)
print(match.start())
print(match.end())

x = [1, 2, 3, [4, 5]]

print(x)

y = [1, 2, 3]

y.extend([4, 5])
print(y)
print(x.index(2))
print(x.index(11))
x.insert()

x.reverse()
y.sort()


