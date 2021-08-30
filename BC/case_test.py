from BC.Timeseries import Timeseries
from BC.case_default import case_default

def case_test():
    [BC, IC] = case_default()

    BC['temp'] = Timeseries([0, 5, 5, 6, 10],[0, 0, 3, 3, 9])

    # Constants
    IC['tf'] = 10000
    IC['ts'] = .1


    IC['T0']    = 60+459.67
    IC['Tinf0'] = 80+459.67
    IC['Tamb']  = 20+459.67
    return [BC, IC]

if __name__ == "__main__":
    case_test()