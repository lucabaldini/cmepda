import numpy
from matplotlib import pyplot as plt
from voltage_data import VoltageData

def run_tests():
    """ Here we test the functionalities of our class. These are not proper
    UnitTests."""
    # Load some data
    t, v = numpy.loadtxt('sample_data_file.txt', unpack=True)
    # Test the constructor
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

    # Test constructor from data file
    v_data_2 = VoltageData.from_file('sample_data_file.txt') 
    # Check that the first row is the same
    assert (v_data_2[0] == v_data[0]).all()    

    # Test iteration
    for i, entry in enumerate(v_data):
        assert entry[0] == t[i]
        assert entry[1] == v[i]
    
    # Test representation and printing
    print(v_data)
    print(repr(v_data))   
    
    # Test interpolation
    v5 = v_data(v_data.timestamps[5])
    assert abs(v5 - v_data.voltages[5] < 1.e-5)    
   
    # Test plotting
    v_data.plot(fmt='ko', markersize=6, label='normal voltage')
    x_grid = numpy.linspace(min(t), max(t), 200)
    plt.plot(x_grid, v_data(x_grid), 'r-', label='spline')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    run_tests()
