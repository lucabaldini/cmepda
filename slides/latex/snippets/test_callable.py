import numpy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from callable import CallCounter

def line(x, m, q):
    return m * x + q

# Generate the datasets: a straight line + gaussian fluctuations
x = numpy.linspace(0., 1., 20)
y = line(x, 2., 10.) + numpy.random.normal(0, 0.1, len(x))

# Fit
counting_func = CallCounter(line)
popt, pcov = curve_fit(counting_func, x, y, p0=[-1., -100.]) # p0 is mandatory here
print('Fitted with {} function calls'.format(counting_func.num_calls))

# Show the results
m, q = popt
plt.figure('fit with custom callable')
plt.plot(x, y, 'bo')
plt.plot(x, line(x, m, q), 'r-')
plt.show()
