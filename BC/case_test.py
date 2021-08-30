from BC.Timeseries import Timeseries
from BC.case_default import case_default

def case_test():
    [BC, IC] = case_default()

    BC['temp'] = Timeseries([0, 5, 5, 6, 10],[0, 0, 3, 3, 9])

    IC['y0'] = 4
    return [BC, IC]

if __name__ == "__main__":
    case_test()