from BC.Timeseries import Timeseries

def case_default():
    BC=dict()
    BC['defaultA'] = Timeseries([0, 1], [0, 0])
    BC['defaultB'] = Timeseries([0, 1], [0, 0])
    BC['defaultC'] = Timeseries([0, 1], [0, 0])
    BC['temp']     = Timeseries([0, 1], [0, 0])

    IC=dict()
    IC['tf'] = 100
    IC['ts'] = .1
    IC['x0'] = 0
    IC['y0'] = 0

    return [BC, IC]
