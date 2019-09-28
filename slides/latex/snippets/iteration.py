list1 = ['a', 'b', 'c']
list2 = [10, 11, 12]

# Horrible (and very un-Pythonic, too)!
for i in range(len(list1)):
    print(i, list1[i])

# Nice-looking.
for i, item in enumerate(list1):
    print(i, item)

# Zipping iterables
for item1, item2 in zip(list1, list2):
    print(item1, item2)

# List comprehension
print([x**2 for x in list2])
