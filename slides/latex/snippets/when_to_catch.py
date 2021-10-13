def parse_line(line):
    """ Parse a line of the file and return the values as float"""
    values = line.strip('\n').split(' ')
    # the following two lines may generate exceptions if they fail!
    time = float(values[0])
    tension = float(values[1])
    return time, tension

with open('snippets/data/fake_measurements.txt') as lab_data_file:
    for line in lab_data_file:
        if not line.startswith('#'): # skip comments
            time, tension = parse_line(line)
            print(time, tension)
