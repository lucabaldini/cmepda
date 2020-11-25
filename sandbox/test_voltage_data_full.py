import unittest
import numpy

from voltage_data_full import VoltageData


def absolute_data_folder_path():
    """Ugly hack for finding the path to the data folder. Works only if the
    current working directory is inside the cmepda package (any of the
    subfolder will do)"""
    import os
    cwd = os.getcwd()
    idx = cwd.rfind('cmepda')
    if idx == -1:
        raise IOError('Could not locate the data folder. The test must be run\
                      from inside the cmepda package.')
    else:
        cmepda_dir = cwd[:idx + len('cmepda')]
    return os.path.join(cmepda_dir, 'sandbox')


class TestVoltageData(unittest.TestCase):

    def setUp(self, sample_size=10):
        """Set up the test. """
        import os
        self.sample_size = sample_size
        self.t = numpy.linspace(0., 2., self.sample_size)
        self.v = numpy.random.uniform(0.5, 1.5, self.sample_size)
        self.v_err = numpy.repeat(0.05, self.sample_size)
        data_folder = absolute_data_folder_path()
        self.sample_file = os.path.join(data_folder, 'sample_data_file.txt')
        self.sample_file_with_errs = os.path.join(data_folder,
                                              'sample_data_file_with_errs.txt')

    def load_from_sample_arrays(self):
        """ Utility function: avoid to rewrite this in each test."""
        return VoltageData(self.t, self.v), \
               VoltageData(self.t, self.v, self.v_err)

    def test_constructor(self):
        """Test the constructor. Not that we access a private member, for
        testing purpose. This is generally not a good practice"""
        v_data, v_data_with_errs = self.load_from_sample_arrays()
        self.assertEqual(v_data._data.shape, (self.sample_size, 2))
        self.assertEqual(v_data_with_errs._data.shape, (self.sample_size, 3))

    def test_alternate_contructor(self):
        """Test constructor from file, both with and without the errors."""
        v_data = VoltageData.from_file(self.sample_file)
        v_data_with_errs = VoltageData.from_file(self.sample_file_with_errs)

    def test_num_rows(self):
        """Test that the number of rows gives the expected value."""
        for istance in self.load_from_sample_arrays():
            # Loop on the two instances: with and without errors
            # Check that len is equal to the number of rows
            self.assertEqual(istance.num_rows(), len(istance))
            # Check that the number of rows is the expected one
            self.assertEqual(istance.num_rows(), self.sample_size)

    def test_num_columns(self):
        """Test the number of columns."""
        v_data, v_data_with_errs = self.load_from_sample_arrays()
        # Two columns for the data without errors, three for data with errors
        self.assertEqual(v_data.num_columns(), 2)
        self.assertEqual(v_data_with_errs.num_columns(), 3)

    def _test_attributes(self, *attributes, expected_size=None):
        """Private wrokhorse function for testing the attribute in a loop,
        to be called by the actual test functions (notice the _ in front of the
        name)."""
        if expected_size is None:
            expected_size = self.sample_size
        for attr in attributes:
            # Test that the attribute is a numpy array
            self.assertTrue(isinstance(attr, numpy.ndarray))
            # Test the sape: they must be 1D with the right lenght
            self.assertEqual(attr.shape, (expected_size, ))

    def test_attributes(self):
        """Test that timestamps, voltages and voltages_err return the right
        thing. In case of data without error test that the correct exception
        is raised."""
        v_data, v_data_with_errs = self.load_from_sample_arrays()
        # Test that timestamps and voltages wrok
        self._test_attributes(v_data.timestamps,
                              v_data.voltages)
        # Test that accessing voltage_errs on a istance of the data without
        # errors trigger a AttributeError. We use a lambda function, since
        # assertRaises() requires a callable as second argument:
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
        self.assertRaises(AttributeError, lambda v : v.voltage_errs, v_data)
        # Test the three attributes on a istance with errors
        self._test_attributes(v_data_with_errs.timestamps,
                              v_data_with_errs.voltages,
                              v_data_with_errs.voltage_errs)

    def test_random_access(self):
        """Test __getitem__"""
        v_data, v_data_with_errs = self.load_from_sample_arrays()
        # Test the first value of the first column (timestamps)
        self.assertAlmostEqual(v_data[0,0], self.t[0])
        # Test the last value of the errors column
        self.assertAlmostEqual(
           v_data_with_errs[v_data_with_errs.num_rows() - 1, 2], self.v_err[-1])
        # Test slicing
        self.assertEqual(v_data[1:5, :].shape, (4, v_data.num_columns()))
        self.assertEqual(v_data_with_errs[: , 1:].shape,
                         (v_data_with_errs.num_rows(), 2))

    def test_iteration(self):
        """Test __iter__"""
        v_data, v_data_with_errs = self.load_from_sample_arrays()
        # A row must be a numpy array with size 2 or 3
        self._test_attributes(*(row for row in v_data),
                              expected_size=v_data.num_columns())
        self._test_attributes(*(row for row in v_data_with_errs),
                              expected_size=v_data_with_errs.num_columns())

    def test_formatting(self):
        """Test __str__ ad __repr__"""
        v_data, v_data_with_errs = self.load_from_sample_arrays()
        # This is not very clever - we are simply printing stuff.
        # A more refined approach would require us to capture the output string
        # and compare to the expect one, but its not very interesting.
        print(v_data, '\n')
        print(repr(v_data), '\n')
        print(v_data_with_errs, '\n')
        print(repr(v_data_with_errs), '\n')

    def test_plotting(self, draw=False):
        """ Test plotting."""
        from matplotlib import pyplot as plt
        # Note: you can ignore the Warning generated by the previous line
        v_data, v_data_with_errs = self.load_from_sample_arrays()
        # Draw the plots into our figure
        plt.figure('test_plot')
        ax = plt.gca()
        v_data.plot(ax)
        v_data_with_errs.plot(ax, fmt='r*')
        if draw:
            plt.show()


if __name__ == "__main__":
    unittest.main()
