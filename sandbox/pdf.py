
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit



class ProbabilityDensityFunction(InterpolatedUnivariateSpline):

    """Class describing a probability density function.
    """

    def __init__(self, x, y):
        """Constructor.
        """
        InterpolatedUnivariateSpline.__init__(self, x, y)
        ycdf = np.array([self.integral(x[0], xcdf) for xcdf in x])
        self.cdf = InterpolatedUnivariateSpline(x, ycdf)
        # Need to make sure that the vector I am passing to the ppf spline as
        # the x values has no duplicates---and need to filter the y
        # accordingly.
        xppf, ippf = np.unique(ycdf, return_index=True)
        yppf = x[ippf]
        self.ppf = InterpolatedUnivariateSpline(xppf, yppf)

    def prob(self, x1, x2):
        """Return the probability for the random variable to be included
        between x1 and x2.
        """
        return self.cdf(x2) - self.cdf(x1)

    def rnd(self, size=1000):
        """Return an array of random values from the pdf.
        """
        return self.ppf(np.random.uniform(size=size))



def test_triangular():
    """Unit test with a triangular distribution.
    """
    x = np.linspace(0., 1., 101)
    y = 2. * x
    pdf = ProbabilityDensityFunction(x, y)
    a = np.array([0.2, 0.6])
    print(pdf(a))

    plt.figure('pdf')
    plt.plot(x, pdf(x))
    plt.xlabel('x')
    plt.ylabel('pdf(x)')

    plt.figure('cdf')
    plt.plot(x, pdf.cdf(x))
    plt.xlabel('x')
    plt.ylabel('cdf(x)')

    plt.figure('ppf')
    q = np.linspace(0., 1., 250)
    plt.plot(q, pdf.ppf(q))
    plt.xlabel('q')
    plt.ylabel('ppf(q)')

    plt.figure('Sampling')
    rnd = pdf.rnd(1000000)
    plt.hist(rnd, bins=200)


def test_gauss(mu=0., sigma=1., support=10., num_points=500):
    """Unit test with a gaussian distribution.
    """
    from scipy.stats import norm
    x = np.linspace(-support * sigma + mu, support * sigma + mu, num_points)
    y = norm.pdf(x, mu, sigma)
    pdf = ProbabilityDensityFunction(x, y)

    plt.figure('pdf')
    plt.plot(x, pdf(x))
    plt.xlabel('x')
    plt.ylabel('pdf(x)')

    plt.figure('cdf')
    plt.plot(x, pdf.cdf(x))
    plt.xlabel('x')
    plt.ylabel('cdf(x)')

    plt.figure('ppf')
    q = np.linspace(0., 1., 1000)
    plt.plot(q, pdf.ppf(q))
    plt.xlabel('q')
    plt.ylabel('ppf(q)')

    plt.figure('Sampling')
    rnd = pdf.rnd(1000000)
    ydata, edges, _ = plt.hist(rnd, bins=200)
    xdata = 0.5 * (edges[1:] + edges[:-1])

    def f(x, C, mu, sigma):
        return C * norm.pdf(x, mu, sigma)
    
    popt, pcov = curve_fit(f, xdata, ydata)
    print(popt)
    print(np.sqrt(pcov.diagonal()))
    _x = np.linspace(-10, 10, 500)
    _y = f(_x, *popt)
    plt.plot(_x, _y)

    mask = ydata > 0
    chi2 = sum(((ydata[mask] - f(xdata[mask], *popt)) / np.sqrt(ydata[mask]))**2.)
    nu = mask.sum() - 3
    sigma = np.sqrt(2 * nu)
    print(chi2, nu, sigma)
    


if __name__ == '__main__':
    test_gauss()
    plt.show()
