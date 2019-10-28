import numpy

class LabData:
  
  def __init__(self, times, values):
     """ Our usual constructor"""
     self.times = numpy.array(times, dtype=numpy.float64)
     self.values = numpy.array(values, dtype=numpy.float64)

  @classmethod # The classmethod decorator
  def from_file(cls, file_path): # We get the class as first argument, not self 
      """ Constructor from a file"""
      print(cls)
      times, values = numpy.loadtxt(file_path, unpack=True)
      # We call the constructor of 'cls' which is our LabData
      # This is not a 'real' constructor, we need to return the object!
      return cls(times, values)

# We call the alternate constructor from the class itself, not from an instance!
lab_data = LabData.from_file('snippets/data/measurements.txt')
print(lab_data.values)
