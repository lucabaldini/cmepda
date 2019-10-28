import numpy

class VoltageData:
    """Class for handling a set of measurements of the voltage at different
    times."""
   
    def __init__(self,  times, voltages, voltage_errs=None):
        """ Constructor from three iterables (times, voltages and voltage erros), 
        the third one being optional."""
        t = numpy.array(times, dtype=numpy.float64)
        v = numpy.array(voltages, dtype=numpy.float64)
        # Put together the arrays in a single matrix with column_stack 
        self._data = numpy.column_stack((t,v))
        # Optionally add also voltage errs
        if voltage_errs is not None:
            v_err = numpy.array(voltage_errs, dtype=numpy.float64)
            self._data = numpy.column_stack((self._data, v_err))
           
    @classmethod
    def from_file(cls, file_path):
        """Alternate constructor from a data file, exploiting load_txt()"""
        columns = numpy.loadtxt(file_path, unpack=True)
        return cls(*columns) # Unpack the tuple!
        
    @property
    def timestamps(self):
        """Return the column of timestamps as a numpy array."""
        # Use the slice syntax to select the first column
        return self._data[:, 0]
   
    @property
    def voltages(self):
        """Return the column of voltages as a numpy array."""
        # Use the slice syntax to select the second column
        return self._data[:, 1]    
    
    @property
    def voltage_errs(self):
        """ Return the voltage errors as a numpy array."""
        # If there is no errror column, numpy will raise a IndexError exception.
        # This is not very explicative for the user: instead we want to raise
        # an AttributeError, which is what you usually get when you call obj.x 
        # and x doesn't exist. So we catch the exception and raise another one.
        try:
            return self._data[:, 2]
        except IndexError:
            err_msg = 'The optional column \'voltage_errs\' is not present.'
            raise AttributeError(err_msg)
        
    def num_rows(self):
        """ Number of rows."""
        return self._data.shape[0]

    def num_columns(self):
        """ Number of columns (can be 2 or 3)."""
        return self._data.shape[1]
            
    def __len__(self):
        """ Number of data points (or rows in the file, which is the same)."""
        return self.num_rows()
           
    def __getitem__(self, index):
        # We use composition and simply call __getitem__ from _data
        return self._data[index]
   
    def __iter__(self):
        """Return the values row by row."""
        # We use a generator expression here. The syntax is very readible!
        for i in range(len(self)):
            yield self._data[i, :]
           
    def __repr__(self):
        """ Print the full content row by row."""
        # Define the row format. We loop on self.num_columns(), so the number
        # of {} always match the number of fields to print.
        row_fmt = ' '.join('{}' for _ in range(self.num_columns()))
        # Join the rows with the newline as separator. Note how we pass the
        # elements of the row to format with the unpacking syntax (*), which is
        # the same used in passing arguments
        return '\n'.join(row_fmt.format(*row) for row in self)
   
    def __str__(self):
        """ Print the full content row-by-row with a nice formatting."""
        # Define the row format
        row_fmt = 'Row {} -> {:.1f} s, {:.2f}'
        # Add the third field only when appropriate
        if self.num_columns() == 3:
            row_fmt += ' {:.2f}'
        # Generator expression for substituing the {} in the format string with
        # the actual values (lazy evaluation - no loop on the next line).
        row_fmt_gen = (row_fmt.format(i, *row) for i, row in enumerate(self))
        # Eventually join the string with a newline. Note that this is the only
        # place where the generators are actually evaluated
        return '\n'.join(row_fmt_gen)
       
    def plot(self, ax=None, fmt='bo'):
        """ Draw the data points."""
        from matplotlib import pyplot as plt
        # The user can provide an existing figure to which we add the plot;
        # otherwise, we create a new one.
        if ax is not None:
            plt.sca(ax) # sca (set current axes) selects the given figure
        else:
            ax = plt.figure('voltage_vs_time')
        # It's easier to ask forgivness than permission!
        try:
            plt.errorbar(self.timestamps, self.voltages, self.voltage_errs, 
                         fmt=fmt)
        except AttributeError:
            plt.plot(self.timestamps, self.voltages, fmt)
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [mV]')
        plt.grid(True)
        return ax # We return the axes, just in case

