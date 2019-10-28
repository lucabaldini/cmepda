def running_average():
    total_count = 0
    num_elements = 0
    def accumulator(value):
        # We declare the relevant variables as nonlocal
        nonlocal total_count, num_elements
        # Now we can assign to them - the variables in the closure will be
        # modified, as we want!
        total_count += value
        num_elements += 1
        return total_count/num_elements
    return accumulator
    
run_avg = running_average()
print(run_avg(1.))
print(run_avg(5.))
print(run_avg(2.5))
