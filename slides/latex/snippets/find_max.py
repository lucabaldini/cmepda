def find_maximum(list_):
    """Find the biggest element in a list.
    """
    maximum = list_[0]
    for value in list_[1:]:
        if value > maximum:
            maximum = value
    return maximum

l = [1, 2, 5, 98, 3, 1672, 6, 34, 651]
print(find_maximum(l))
