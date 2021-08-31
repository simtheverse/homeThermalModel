## Based off of github:clampr/meteostat-py-example-v1.py

# Import Meteostat library and dependencies
from datetime import datetime
import pytz
import matplotlib.pyplot as plt
from meteostat import Stations, Hourly
import numpy as np
from dateutil import parser
from datetime import timedelta

from BC.Timeseries import Timeseries

def getAmbientBC(Parameters):

    [lat,lon] = Parameters['geolocation']

    start_naive = parser.parse(Parameters['datetime_str'])
    end_naive   = start_naive + timedelta(seconds=Parameters['tf'])

    timezone = pytz.timezone("America/Phoenix")
    start_tz = timezone.localize(start_naive)
    end_tz = timezone.localize(end_naive)
    start = start_tz.astimezone(pytz.utc).replace(tzinfo=None)
    end = end_tz.astimezone(pytz.utc).replace(tzinfo=None)

    # Get closest weather station to Vancouver, BC
    stations = Stations()
    stations = stations.nearby(lat, lon)
    stations = stations.inventory('hourly', (start, end))
    station = stations.fetch(1)

    # Get daily data for 2018 at the selected weather station
    data = Hourly(station, start, end)
    data = data.fetch()

    data['time']      = data.index.astype(np.int64)/1e+9
    data['time']      = data['time'] - data['time'][0]
    data['Tamb_degR'] = data['temp'] * 9 / 5 + 32 +459.67   # C to R
    data['Pamb_Pa']   = data['pres'] * 100                  # mb to Pa

    Tamb_degR  = Timeseries(data['time'].to_list(),data['Tamb_degR'].to_list())
    Pamb_Pa    = Timeseries(data['time'].to_list(),data['Pamb_Pa'].to_list())

    return [Tamb_degR, Pamb_Pa]

if __name__ == "__main__":
    from BC.case_default import case_default
    [BC, Parameters] = case_default()

    [Tamb_degR, Pamb_Pa] = getAmbientBC(Parameters)
    print('hi')