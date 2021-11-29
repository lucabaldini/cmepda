from decorator_samples import clocked, repeat, print_function_info

""" To chain the effect of more than one decorator just stack them above the 
function definition """

@print_function_info
@repeat(num_times=3)
@clocked
def greet(name):
    print(f'Hello {name}')
    
greet('Bob')
