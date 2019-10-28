class VoltageData:

   """ Other methods here..."""
   
   def __len__(self):
       """ Number of data points (or rows in the file, which is the same) """
       return self._data.shape[0]
   
   def __getitem__(self, index):
       # We use composition and simply call __getitem__ from _data
       return self._data[index]
   
   def __iter__(self):
       """Return the values row by row"""
       # We use a generator expression here. The syntax is very readible!
       for i in range(len(self)):
           yield self._data[i, :] 
           
   def __repr__(self):
       """ Print the full content row by row """
       return '\n'.join('{} {}'.format(row[0], row[1]) for row in self)
   
   def __str__(self):
       """ Print the full content row-by-row with a nice formatting"""
       row_fmt = 'Row {} -> {:.1f} s, {:.2f} mV'
       row_str_gen = \
               (row_fmt.format(i, row[0], row[1]) for i, row in enumerate(self))
       return '\n'.join(row_str_gen)
