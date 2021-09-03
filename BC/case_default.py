from dateutil import parser

from BC.Timeseries import Timeseries
from BC.getAmbientBC import getAmbientBC

from plant.AC import AC as AC
from plant.AC import getAC_BC
from plant.roomAir import roomAir as roomAir
from plant.people import person as person

from datetime import datetime, timedelta

def case_default():
    Parameters = dict()
    hours = 9
    Parameters['tf'] = 60*60*hours  # 1 hour in seconds
    Parameters['ts'] = .1     # time step = seconds

    # Time Series Boundary Conditions
    BC=dict()
    BC['temp']     = Timeseries([0, 1], [0, 0])
    BC['numberOfPeople'] = Timeseries([0,1], [1,1])
    BC['appliance_heatload_W'] = Timeseries([0,1], [1000,1000])


    # Get Ambient conditions
    Parameters['geolocation'] = [33.4152, -111.8315]
    now = datetime.now() - timedelta(hours=24)
    now = parser.parse('September 2nd 2021 8:00am')
    Parameters['datetime_str'] = now.strftime("%m/%d/%Y %H:%M:%S")

    [BC['Tamb_degR'], BC['Pamb_Pa'], BC['UVIndex']] = getAmbientBC(Parameters)


    IC=dict()
    # Constants
    IC['tf'] = 100
    IC['ts'] = .1

    # Plant properties
    #Contents defintion
    Contents = dict()
    Contents['As']= 991/10.764  #ft^2 -> m^2
    Contents['rho']= 515 # kg/m^3  http://www.ibpsa.org/proceedings/BS2017/BS2017_012.pdf
    Contents['V'] = Contents['As']*0.1524 # m^2 *.5ft
    Contents['c'] = 1400/1.8  # 1400 J/kg/K -> J/kg/R
    Parameters['plant_contents'] = Contents

    # Air definition
    Parameters['plant_roomAir'] = roomAir()

    # People Definition
    Parameters['plant_Person'] = person()

    # AC parameters
    Parameters['plant_AC'] = AC()
    BC['AC_W'] = getAC_BC(Parameters['plant_AC']['coolingW'], 60*4, 60*20, Parameters['tf'])


    # Initial Conditions
    IC = dict()
    IC['Tcontents0_degR'] = 0
    IC['Tair0_degR'] = 0
    Parameters['IC'] = IC


    return [BC, Parameters]

if __name__ == "__main__":
    case_default()