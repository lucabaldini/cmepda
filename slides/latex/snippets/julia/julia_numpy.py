"""Julia set generator, reimplemented using numpy by me.
The orginal implementation in pure python comes from the code repository of the 
book High Performance Python, of Micha Gorelick and Ian Ozsvald, except from the
drawing with matplotlib which is also mine.
The original file can be found at:
https://github.com/mynameisfiber/high_performance_python/blob/master/01_profiling/cpu_profiling/julia1.py"""

import time
import numpy


# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -0.42193


def show_greyscale(output_raw, width, height, max_iterations):
    """Convert list to array, show using PIL"""
    from matplotlib import pyplot as plt
    output = numpy.array(output_raw, dtype=numpy.float64).reshape(width, height)
    # Convert to grayscale
    output = ((255/max_iterations) * output).astype(dtype=numpy.int)
    plt.figure('Julia')
    plt.axis('off')
    plt.imshow(output, cmap='gray', vmin = 0, vmax = 255)
    plt.show()


def calculate_z_serial_numpy(maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
    # Initialize the output with zeroes
    output = numpy.zeros(len(zs))
    # Create an array of indices for the output array. We will use these indices
    # to know whic values to increment in the loop
    idx = numpy.arange(len(output))
    for _ in range(maxiter):
        # Mask the pixels, removing those for which the loop condition is false
        # Note: masking create new arrays, so it is a bit expensive!
        mask = numpy.abs(zs) < 2
        zs = zs[mask]
        cs = cs[mask]
        # We mask the index array as well, to stay in sync with zs and cs
        idx = idx[mask]
        # Add one to the output for the elements which are still in game
        output[idx] = output[idx] + 1
        # Update zs. Note: only the pixel not masked!
        zs = numpy.square(zs) + cs
    return output


def calc_pure_python(desired_width, max_iterations, draw_output=False):
    """Create a list of complex co-ordinates (zs) and complex parameters (cs), 
        build Julia set and display"""
    x = numpy.linspace(x1, x2, desired_width, endpoint=False)
    y = numpy.linspace(y2, y1, desired_width, endpoint=False)
    # build a list of co-ordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed,
    # we use it to simulate a real-world scenario with several inputs to our
    # function
    gridx, gridy = numpy.meshgrid(x, y)
    zs = (gridx + 1j * gridy).flatten()
    cs = numpy.repeat(complex(c_real, c_imag), len(x)*len(y))
    
    start_time = time.time()
    output = calculate_z_serial_numpy(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_numpy.__name__ + " took", secs, "seconds")

    # this sum is expected for 1000^2 grid with 300 iterations
    assert sum(output) == 33219980
    
    if draw_output:
        #show_false_greyscale(output, width, height, max_iterations)
        show_greyscale(output, len(x), len(y), max_iterations)


if __name__ == "__main__":
    # Calculate the Julia set using a numpy solution with
    # reasonable defaults for a laptop
    # set draw_output to True to use matplotlib to draw an image
    calc_pure_python(desired_width=1000, max_iterations=300, draw_output=False)
