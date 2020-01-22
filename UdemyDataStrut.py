mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in mylist:
    if num % 2 == 0:
        print(f'Even Number {num}')
    else:
        print(f'Odd number {num}')

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_sum = 0

for item in mylist:
    list_sum = list_sum + item
    print(list_sum)
print(f'Total sum {list_sum}')

x = 0

while x < 5:
    print(f'Current value of X is {x}')
    x = x + 1

word = 'abcde'

for item, value in enumerate(word):
    print(item)
    print(value)

mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c', 'd', 'e']

for item in zip(mylist1, mylist2):
    print(item)
    print(list(item))

mylist = [x ** 2 for x in range(0, 11) if (x % 2) == 0]
print(mylist)

results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(results)

print(mylist1.pop())


def pig_latin(input):
    first_letter = input[0]

    if first_letter in 'aeiou':
        pig_word = input + 'ae'
    else:
        pig_word = input[0:] + 'ay'
    return pig_word


abc = pig_latin('apple')
print(abc)


def myfunc(x, y, z):
    if z == True:
        return x
    else:
        return y


def myfunc1(x, y, z):
    return x if z == True else y


abc = myfunc('Hello', 'Goodbye', False)
print(abc)

abc1 = myfunc1('Hello', 'Nupur', False)
print(abc1)


def is_greater(a, b):
    return True if a > b else False
