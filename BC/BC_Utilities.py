import numpy

def resample_dict(BC, t):
    y_BC = dict()
    for key in BC:
        y_BC[key] = numpy.array(BC[key].resample(t))
    return y_BC