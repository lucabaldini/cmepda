import numpy
from matplotlib import pyplot as plt


class VoltageData:
   """Class for handling a set of measurements of the voltage at different
   times."""
   
   pass
   
   

if __name__ == '__main__':
    """ Here we test the functionalities of our class. These are not proper
    UnitTest - which you will se in a future lesson."""
    # Load some data
    t, v = numpy.loadtxt('sandbox/sample_data_file.txt', unpack=True)
    # Thest the constructor
    v_data = VoltageData(t, v)
    # Test len()
    assert len(v_data) == len(t)
    # Test the timestamps attribute
    assert numpy.all(v_data.voltages == v)
    # Test the voltages attribute
    assert numpy.all(v_data.timestamps == t)
    # Test square parenthesis
    assert v_data[3, 1] == v[3]
    assert v_data[-1, 0] == t[-1]
    # Test slicing
    assert numpy.all(v_data[1:5, 1] == v[1:5])
    # Test iteration
    for i, entry in enumerate(v_data):
        assert entry[0] == t[i]
        assert entry[1] == v[i]
    # Test printing
    print(v_data)
    # Test plotting
    plt.figure('voltage vs time')
    v_data.plot(plt.gca(), fmt='r+')
    plt.show()
    
    
