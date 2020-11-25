def raising_function():
    # You can pass useful message to the exceptions you raise
    raise RuntimeError('this is a useful debug message') 

try:
    raising_function()
except RuntimeError as e:
    # The message can be retrieved by printing the exception
    print(e)
