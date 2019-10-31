"""Julia set generator, taken almost verbatim from the code repository of the 
book High Performance Python, of Micha Gorelick and Ian Ozsvald, except from the
drawing with matplotlib which is mine.
The original file can be found at:
https://github.com/mynameisfiber/high_performance_python/blob/master/01_profiling/cpu_profiling/julia1.py"""

import time


# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193


def show_greyscale(output_raw, width, height, max_iterations):
    """Convert list to array, show using PIL"""
    from matplotlib import pyplot as plt
    import numpy
    output = numpy.array(output_raw, dtype=numpy.float64).reshape(width, height)
    # Convert to grayscale
    output = ((255/max_iterations) * output).astype(dtype=numpy.int)
    plt.figure('Julia')
    plt.axis('off')
    plt.imshow(output, cmap='gray', vmin = 0, vmax = 255)
    plt.show()


def calculate_z_serial_purepython(maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output


def calc_pure_python(desired_width, max_iterations, draw_output=False):
    """Create a list of complex co-ordinates (zs) and complex parameters (cs), 
        build Julia set and display"""
    x_step = (float(x2 - x1) / float(desired_width))
    y_step = (float(y1 - y2) / float(desired_width))
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    
    # build a list of co-ordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed,
    # we use it to simulate a real-world scenario with several inputs to our
    # function
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))
    
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_purepython.__name__ + " took", secs, "seconds")

    # this sum is expected for 1000^2 grid with 300 iterations
    assert sum(output) == 33219980
    
    if draw_output:
        show_greyscale(output, len(x), len(y), max_iterations)


if __name__ == "__main__":
    # Calculate the Julia set using a pure Python solution with
    # reasonable defaults for a laptop
    # set draw_output to True to use matplotlib to draw an image
    calc_pure_python(desired_width=1000, max_iterations=300, draw_output=False)
