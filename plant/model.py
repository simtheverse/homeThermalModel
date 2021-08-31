# function that returns dz/dt
def model(z,t,y_BC,i,Parameters):
    #x = z[0]
    #y = z[1]
    #dxdt = (-x + y_BC['temp'][i])/2.0
    #dydt = (-y + x)/5.0

    Tair = z[0]
    Tinf = z[1]
    Tamb = y_BC['Tamb_degR'][i]

    dTairdt = -Parameters['contents']['h']*Parameters['contents']['As']/Parameters['contents']['rho']/Parameters['contents']['V']/Parameters['contents']['c']*(Tair-Tinf)
    dTinfdt = (-Parameters['air']['h']*Parameters['air']['As']*((Tinf-Tair)+(Tinf-Tamb))+.1)/Parameters['air']['rho']/Parameters['air']['V']/Parameters['air']['c']

    dzdt = [dTairdt, dTinfdt]
    return dzdt