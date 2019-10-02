def sloppy_sort(list_):
    """Poor man's implementation of a sorting algorithm.
    """
    sorted_list = []
    for item in list_:
        if len(sorted_list) == 0:
            sorted_list.append(item)
        else:
            if item < sorted_list[0]:
                sorted_list.insert(0, item)
            else:
                for i, sorted_item in enumerate(sorted_list):
                    if item <= sorted_item:
                        sorted_list.insert(i, item)
                        break
    return sorted_list

l = [10, 1, 5, 2, 7, 3, 9, 4]
print(l)
print(sloppy_sort(l))
