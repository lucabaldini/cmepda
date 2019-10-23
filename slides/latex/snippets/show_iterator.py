my_list = [1., 2., 3.]

# For-loop syntax
for element in my_list:
    print(element)

# This is equivalent (but much less readible and compact)
list_iterator = iter(my_list)
while True:
    try:
        print(next(list_iterator))
    except StopIteration:
        break
