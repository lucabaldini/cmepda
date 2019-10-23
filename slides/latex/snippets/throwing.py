def throwing_function():
    # You can pass useful message to the exceptions you throw
    raise RuntimeError('this is a useful debug text') 

try:
    throwing_function()
except RuntimeError as e:
    # The message can be retrieved by printing the exception
    print(e)
