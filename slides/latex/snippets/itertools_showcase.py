from itertools import accumulate, product, chain, groupby, permutations, combinations
import operator

l1 = [1, 2, 3, 4]
print(list(accumulate(l1)))
print(list(accumulate(l1, func=operator.mul)))
print(list(combinations(l1, 3)))

l2 = [5, 6]
print(list(permutations(l2, 2)))
print(list(product(l1, l2)))

def is_even(n):
    return n % 2 == 0

l3 = list(chain(l1, l2))
# groupby expect the list to be sorted by the grouping function
l3.sort(key=is_even)
for k, g in groupby(l3, key=is_even):
    print(k, list(g))
