def parse_line(line):
    """ Parse a line of the file and return the values as float"""
    values = line.strip('\n').split(' ')
    # the following two lines may generate exceptions if they fails!
    time = float(values[0])
    tension = float(values[1])
    return time, tension

with open('snippets/data/fake_measurements.txt') as lab_data_file:
    for line_number, line in enumerate(lab_data_file): # get the line number
        if not line.startswith('#'): # skip comments
            try:
                time, tension = parse_line(line)
                print(time, tension)
            except ValueError as e:
                print('Line {} error: {}'.format(line_number, e))
