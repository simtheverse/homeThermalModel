from BC.Timeseries import Timeseries
from BC.case_default import case_default
from BC.getAmbientBC import getAmbientBC
from plant.AC import getAC_BC

def case_test():
    [BC, Parameters] = case_default()

    # Constants
    Parameters['ts'] = 1
    [BC['Tamb_degR'], BC['Pamb_Pa'], BC['UVIndex']] = getAmbientBC(Parameters)

    BC['AC_W'] = getAC_BC(Parameters['plant_AC']['coolingW'], 60*5, 60*10, Parameters['tf'])


    Parameters['IC']['Tcontents0_degR']    = 75+459.67 #BC['Tamb_degR'].values[0]
    Parameters['IC']['Tair0_degR'] = 72+459.67 #BC['Tamb_degR'].values[0]


    return [BC, Parameters]

if __name__ == "__main__":
    case_test()