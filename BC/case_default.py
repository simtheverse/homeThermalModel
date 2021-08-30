from BC.Timeseries import Timeseries

def case_default():
    BC=dict()
    BC['defaultA'] = Timeseries([0, 1], [0, 0])
    BC['defaultB'] = Timeseries([0, 1], [0, 0])
    BC['defaultC'] = Timeseries([0, 1], [0, 0])
    BC['temp']     = Timeseries([0, 1], [0, 0])

    IC=dict()
    # Constants
    IC['tf'] = 100
    IC['ts'] = .1

    # Plant properties
    IC['contents_h'] = .2
    IC['contents_As']= 1
    IC['contents_rho']=100
    IC['contents_V'] = 1
    IC['contents_c'] = 1

    IC['air_h'] = .1
    IC['air_As']= 1
    IC['air_rho']=1
    IC['air_V'] = 100
    IC['air_c'] = 1

    IC['Tamb'] = 0+459.67



    # Initial Conditions
    IC['T0'] = 0
    IC['Tinf0'] = 0

    return [BC, IC]
