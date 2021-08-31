from BC.Timeseries import Timeseries
from BC.case_default import case_default
from BC.getAmbientBC import getAmbientBC

def case_test():
    [BC, Parameters] = case_default()

    BC['temp'] = Timeseries([0, 5, 5, 6, 10],[0, 0, 3, 3, 9])

    # Constants
    Parameters['tf'] = 100000
    Parameters['ts'] = 1
    [BC['Tamb_degR'], BC['Pamb_Pa']] = getAmbientBC(Parameters)


    Parameters['IC']['T0_degR']    = BC['Tamb_degR'].values[0]
    Parameters['IC']['Tinf0_degR'] = BC['Tamb_degR'].values[0]


    return [BC, Parameters]

if __name__ == "__main__":
    case_test()