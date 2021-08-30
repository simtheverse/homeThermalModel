from dataclasses import dataclass
from bisect import bisect_left


@dataclass(frozen=True)
class Timeseries:
    time: list
    values: list

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
        return [self.lookup(x) for x in t_vector]


if __name__ == "__main__":
    xs = [0, 5, 5, 6, 10]
    ys = [0, 0, 3, 3, 9]
    BC = dict()
    BC['Inlet_PAds_PSIA'] = Timeseries(xs, ys)

    stepsize = .01
    timeend = 15
    i_xs = [i * stepsize for i in range(int(timeend / stepsize))]
    import time
    import matplotlib.pyplot as plt

    start_time = time.time()
    ys = [BC['Inlet_PAds_PSIA'].lookup(x) for x in i_xs]
    plt.plot(i_xs, ys)
    print("%s secs" % (time.time() - start_time))
    plt.show()

    print(BC['Inlet_PAds_PSIA'].time)
