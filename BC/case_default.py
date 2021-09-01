from BC.Timeseries import Timeseries
from BC.getAmbientBC import getAmbientBC

from plant.AC import AC as AC
from plant.roomAir import roomAir as roomAir
from plant.people import person as person

def case_default():
    Parameters = dict()
    Parameters['tf'] = 60*60  # 1 hour in seconds
    Parameters['ts'] = .1     # time step = seconds

    # Time Series Boundary Conditions
    BC=dict()
    BC['temp']     = Timeseries([0, 1], [0, 0])
    BC['numberOfPeople'] = Timeseries([0,1], [1,1])
    BC['appliance_heatload_W'] = Timeseries([0,1], [50,50])


    # Get Ambient conditions
    Parameters['geolocation'] = [33.456506143111966, -111.68313649552813]
    Parameters['datetime_str'] = "Aug 29th 2021 8:00am"

    [BC['Tamb_degR'], BC['Pamb_Pa']] = getAmbientBC(Parameters)


    IC=dict()
    # Constants
    IC['tf'] = 100
    IC['ts'] = .1

    # Plant properties
    #Contents defintion
    Contents = dict()
    Contents['h'] = .2
    Contents['As']= .9*.9  #m^2
    Contents['rho']=100
    Contents['V'] = 3.35*3.35*0.1524 # m^3 = 11*11*.5ft^2
    Contents['c'] = 1
    Parameters['plant_contents'] = Contents

    # Air definition
    Parameters['plant_roomAir'] = roomAir()

    # People Definition
    Parameters['plant_Person'] = person()

    # AC parameters
    Parameters['plant_AC'] = AC()







    # Initial Conditions
    IC = dict()
    IC['T0_degR'] = 0
    IC['Tinf0_degR'] = 0
    Parameters['IC'] = IC

    # Other Parameters
    Parameters['geolocation'] = [33.456506143111966, -111.68313649552813]

    return [BC, Parameters]

if __name__ == "__main__":
    case_default()