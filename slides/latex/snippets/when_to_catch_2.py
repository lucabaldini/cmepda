def parse_line(line):
    """ Parse a line of the file and return the values as float"""
    values = line.strip('\n').split(' ')
    time = float(values[0])
    voltage = float(values[1])
    return time, voltage

with open('snippets/data/fake_measurements.txt') as lab_data_file:
    for line_number, line in enumerate(lab_data_file): # get the line number
        if not line.startswith('#'): # skip comments
            try:
                time, voltage = parse_line(line)
                print(time, voltage)
            except ValueError as e:
                print('Line {} error: {}'.format(line_number, e))
