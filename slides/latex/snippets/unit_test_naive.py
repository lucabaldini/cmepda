def square(x):
    """Function returning the suare of x.
    """
    return x**2.

def test():
    """Dumb unit test---make sure that the square of 2. is 4.
    """
    assert square(2.) == 4.
    print('Passed---cool!')


if __name__ == '__main__':
    test()
