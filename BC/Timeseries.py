from dataclasses import dataclass
from bisect import bisect_left


@dataclass
class Timeseries:
    time: list
    values: list

    def __post_init__(self):
        self.original_time = self.time
        self.original_values = self.values

    def lookup(self, t):

        if t <= self.time[0]:  return self.values[0]
        if t >= self.time[-1]: return self.values[-1]

        i = bisect_left(self.time, t)
        k = (t - self.time[i - 1]) / (self.time[i] - self.time[i - 1])
        y = k * (self.values[i] - self.values[i - 1]) + self.values[i - 1]

        return y

    def plot(self):
        import matplotlib.pyplot as selfPlot
        selfPlot.plot(self.time, self.values)
        selfPlot.show()

    def resample(self, t_vector):
        self.time = t_vector
        self.values = [self.lookup(x) for x in t_vector]

        return self.values

    def reset(self):
        self.time = self.original_time
        self.values = self.original_values
        return


if __name__ == "__main__":
    xs = [0, 5, 5, 6, 10]
    ys = [0, 0, 3, 3, 9]
    BC = dict()
    BC['Inlet_PAds_PSIA'] = Timeseries(xs, ys)

    stepsize = .01
    timeend = 10
    i_xs = [i * stepsize for i in range(int(timeend / stepsize))]
    import time
    import matplotlib.pyplot as plt

    start_time = time.time()
    ys = [BC['Inlet_PAds_PSIA'].lookup(x) for x in i_xs]
    plt.plot(i_xs, ys)
    print("%s secs" % (time.time() - start_time))
    plt.show()

    print(BC['Inlet_PAds_PSIA'].time)
