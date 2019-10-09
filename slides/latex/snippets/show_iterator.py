my_list = [1., 2., 3.]

# For-loop syntax
for element in my_list:
    print(element)

# This is equivalent (but much less readible and compact)
list_iterator = iter(my_list)
while True:
    # We will study try-except statements in the advanced module
    # For now you just need to know that the code in the try block is
    # executed at each iteration until the list is over: at taht point the
    # code in the except block is executed instead. In this case we use the 
    # except block to just exit from the while loop
    try:
        print(next(list_iterator))
    except StopIteration:
        break
