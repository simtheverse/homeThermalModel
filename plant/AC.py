def AC():
    aircond=dict()

    # First Co 24HX0-240

    aircond['coolingW'] = 24000 / 3.4121416351331 # BTUH to W
    aircond['CFM']      = 800                     # Cubic feet per minute

    return aircond

def getAC_BC(W, t_On, t_Off, tf):
    from BC.Timeseries import Timeseries
    time = [0]
    Watts = [0]
    for i in range(int(tf/(t_On+t_Off))):
        time = time + [time[-1]+.01, time[-1]+t_On, time[-1]+t_On, time[-1]+t_On+t_Off]
        Watts = Watts + [W,W,0,0]

    TS = Timeseries(time,Watts)
    return TS
