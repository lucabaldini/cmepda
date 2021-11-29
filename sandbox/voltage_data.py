import numpy
from matplotlib import pyplot as plt
from scipy import interpolate


class VoltageData:
    """Class for handling a set of measurements of the voltage at different
    times."""

    def __init__(self, times, voltages):
        """ Constructor from two iterables of the same length."""
        t = numpy.array(times, dtype=numpy.float64)
        v = numpy.array(voltages, dtype=numpy.float64)
        # Put together the arrays in a single matrix with column_stack
        self._data = numpy.column_stack([t, v])
        self.spline = interpolate.InterpolatedUnivariateSpline(self.timestamps,
                                                               self.voltages,
                                                               k=3)
    @classmethod
    def from_file(cls, file_path):
        """ Alternate constructor from a data file, exploiting load_txt()"""
        t, v = numpy.loadtxt(file_path, unpack=True)
        return cls(t, v) 


    @property
    def timestamps(self):
        # Use the slice syntax to select the first column
        return self._data[:, 0]

    @property
    def voltages(self):
        # Use the slice syntax to select the second column
        return self._data[:, 1]

    def __len__(self):
        """ Number of measurements (or rows in the file, which is the same) """
        return len(self._data)

    def __getitem__(self, index):
        """Random access. We use composition and simply call 
        __getitem__ from _data. """
        return self._data[index]

    def __iter__(self):
        """Return the values row by row.
        We use a generator expression here. The syntax is very readible!"""
        for i in range(len(self)):
            yield self._data[i, :]
        # Also works: return iter(data)

    def __repr__(self):
        """ Print the full content row by row """
        # Use a generator expression
        return '\n'.join('{} {}'.format(row[0], row[1]) for row in self)
    
    def __str__(self):
        """ Print the full content row-by-row with a nice formatting"""
        row_fmt = 'Row {} -> {:.1f} s, {:.2f} mV'
        return '\n'.join(row_fmt.format(i, entry[0], entry[1]) \
                         for i, entry in enumerate(self))

    def __call__(self, t):
        """ Return the voltage value interpolated at time t"""
        return self.spline(t)

    def plot(self, ax=None, fmt='bo', **plot_options):
       """ Draw the data points using matplotlib.pyplot."""
       from matplotlib import pyplot as plt
       # The user can provide an existing figure to add the plot, otherwise we
       # create a new one.
       if ax is not None:
           plt.sca(ax) # sca (Set Current Axes) selects the given figure
       else:
           ax = plt.figure('voltage_vs_time')
       plt.plot(self.timestamps, self.voltages, fmt, **plot_options)
       plt.xlabel('Time [s]')
       plt.ylabel('Voltage [mV]')
       plt.grid(True)
       return ax # We return the axes, just in case 
