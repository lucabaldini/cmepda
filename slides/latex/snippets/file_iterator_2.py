from itertools import dropwhile

class LabFile:
    def __init__(self, file_obj):
        self._file = file_obj
       
    def __iter__(self):
        # Enumerate is now inside dropwhile, so all lines are counted
        # This is a bit convoluted, though
        for i, line in dropwhile(lambda x : x[1].startswith('#'),
                                 enumerate(self._file)):
            values = line.strip('\n').split(' ')
            try:
                time = float(values[0])
                tension = float(values[1])
            except ValueError as e:
                print('Line {} error: {}'.format(i, e))
                continue
            yield time, tension

with open('snippets/data/fake_measurements.txt') as lab_data_file:
    for time, tension in LabFile(lab_data_file):
        print(time, tension)
