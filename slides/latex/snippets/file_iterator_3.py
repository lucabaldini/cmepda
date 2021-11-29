class LabFile:
    def __init__(self, file_obj):
        self._file = file_obj
       
    def __iter__(self):
        # This is more readible
        for i, line in enumerate(self._file):
            if line.startswith('#'):
                continue
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
