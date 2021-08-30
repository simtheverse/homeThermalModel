from Timeseries import Timeseries
from case_default import case_default

def case_test():
    BC = case_default()

    BC['temp'] = Timeseries([0, 5, 5, 6, 10],[0, 0, 3, 3, 9])


if __name__ == "__main__":
    case_test()