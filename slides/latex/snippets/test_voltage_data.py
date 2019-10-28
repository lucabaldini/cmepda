from voltage_data import VoltageData
from matplotlib import pyplot as plt

def run_tests(): # This is not a proper unittest module!
    # Test constructor from data file
    data_file = VoltageData.from_file('snippets/data/sample_data_file.txt')
    # Column access by simple name
    t = data_file.timestamps
    v = data_file.voltages
    print(t[0], v[0])
    
    # Iterable by row
    for row in data_file:
        pass

    # Proper representation and printing
    print(repr(data_file))
    print(data_file)

    # Item access with slicing
    print(data_file[1:5, :])

    # Constructor from iterables (list, tuple, array)
    data_file_2 = VoltageData(list(t), tuple(v))
    # Check that the forst row is the same
    assert((data_file_2[0] == data_file[0]).all())
    # Plotting
    data_file_2.plot()
    plt.show()
