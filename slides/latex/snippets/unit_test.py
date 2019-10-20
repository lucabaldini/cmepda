import unittest

def square(x):
    """Function returning the suare of x.

    In real life this would be in a differnt module!
    """
    return x**2.


class TestSquare(unittest.TestCase):

    def test(self):
        """Dumb unit test---make sure that the square of 2. is 4.
        """
        self.assertAlmostEqual(square(2.), 4.)


if __name__ == '__main__':
    unittest.main()
