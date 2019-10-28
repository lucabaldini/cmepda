class VoltageData:

    """Other methods here..."""

    def plot(self, ax=None, fmt='bo'):
        """ Draw the data points."""
        from matplotlib import pyplot as plt
        # The user can provide an existing figure to add the plot, otherwise we
        # create a new one.
        if ax is not None:
            plt.sca(ax) # sca (Set Current Axes) selects the given figure
        else:
            ax = plt.figure('voltage_vs_time')
        plt.plot(self.timestamps, self.voltages, fmt)
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [mV]')
        plt.grid(True)
        return ax # We return the axes, just in case 
