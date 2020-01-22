from collections import Counter

l = [1, 2, 3, 4, 45, 6, 9, 6, 5, 5]

c = Counter(l)
print(c)

words = 'How many time each word showed up in this sequence word times each word'
a = words.split()
print(a)

b = Counter(words)
c = b.most_common(2)
print(b)
print(c)
