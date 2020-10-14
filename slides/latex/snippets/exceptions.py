def throwing_function():
    raise
    print("This line is never executed!")

try:
  throwing_function()
  print("This line is never executed as well!")
except:
  print("This line is executed only if an exception is raised in the try block")
else: # optional!
  print("This line is executed only if no exception is raised in the try block")
finally: # optional!
  print("This line is always executed")
