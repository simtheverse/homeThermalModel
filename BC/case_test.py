from BC.Timeseries import Timeseries
from BC.case_default import case_default
from BC.getAmbientBC import getAmbientBC

def case_test():
    [BC, Parameters] = case_default()

    BC['temp'] = Timeseries([0, 5, 5, 6, 10],[0, 0, 3, 3, 9])

    # Constants
    Parameters['tf'] = 10000
    Parameters['ts'] = .1


    Parameters['IC']['T0_degR']    = 60+459.67
    Parameters['IC']['Tinf0_degR'] = 80+459.67

    [BC['Tamb_degR'], BC['Pamb_Pa']] = getAmbientBC(Parameters)
    return [BC, Parameters]

if __name__ == "__main__":
    case_test()