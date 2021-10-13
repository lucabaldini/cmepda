from itertools import dropwhile

class LabFileIterator:
    def __init__(self, file_obj):
        self._lines = dropwhile(lambda line: line.startswith('#'), file_obj)
        
    def __next__(self):
        line = next(self._lines)
        values = line.strip('\n').split(' ')
        time = float(values[0])
        tension = float(values[1])
        return time, tension
    
    def __iter__(self):
        return self

with open('snippets/data/fake_measurements.txt') as lab_data_file:
    try:
        for line_number, (time, tension) in enumerate(LabFileIterator(lab_data_file)):
            print(line_number, time, tension)
    except ValueError as e:
        # Here we get the wrong line number! Why?
        print('Line {} error: {}'.format(line_number, e))
