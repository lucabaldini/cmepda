# The 'find()' method for strings in python uses an error flag
text = 'elephant'
print(text.find('p')) # upon success returns the position of the substring
print(text.find('d')) # returns -1 if the substring is not found

def safe_division(a, b):
    if b == 0:
        return 0 # Is that meaningful? What can we return?
    else:
        return a/b

# Why is this dangerous?
num_process = 0
num_cpu_available = 3
average_cpu_available = safe_division(num_cpu_available, num_process)
print(average_cpu_available) # Oops no cpu available... or not?
