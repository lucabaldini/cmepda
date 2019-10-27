def parse_line(line):
    """ Parse a line of the file and return the values as float"""
    values = line.strip('\n').split(' ')
    try:
        time = float(values[0])
        tension = float(values[1])
    except ValueError as e:
        print(e) # This is not useful - which line of the file has the error?
        return None # We can't really return something meaningful
    return time, tension

with open('fake_measurements.txt') as lab_data_file:
    for line in lab_data_file:
        if not line.startswith('#'): # skip comments
            time, tension = parse_line(line)
            print(time, tension) # This line still crash badly!
