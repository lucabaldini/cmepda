import numpy

class VoltageData:
   """Class for handling a set of measurements of the voltage at different
   times."""
   
   def __init__(self,  times, voltages):
       """ Constructor from two iterables (times and voltages)"""
       t = numpy.array(times, dtype=numpy.float)
       v = numpy.array(voltages, dtype=numpy.float)
       # Put together the arrays in a single matrix with column_stack 
       self._data = numpy.column_stack((t,v))
   
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
