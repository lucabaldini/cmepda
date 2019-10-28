def running_average():
    total_count = 0
    num_elements = 0
    def accumulator(value):
        total_count += value # Doesn't work! total_count is reassigned!
        num_elements += 1 # Doesn't work! total_count is reassigned!
        return total_count/num_elements
    return accumulator
    
run_avg = running_average()
print(run_avg(1.))
print(run_avg(5.))
print(run_avg(2.5))
