# function that returns dz/dt
def model(z,t,y_BC,i,IC):
    #x = z[0]
    #y = z[1]
    #dxdt = (-x + y_BC['temp'][i])/2.0
    #dydt = (-y + x)/5.0

    T    = z[0]
    Tinf = z[1]
    Tamb = z[2]

    dTdt = -IC['contents_h']*IC['contents_As']/IC['contents_rho']/IC['contents_V']/IC['contents_c']*(T-Tinf)
    dTinfdt = (-IC['air_h']*IC['air_As']*((Tinf-T)+(Tinf-Tamb))+.1)/IC['air_rho']/IC['air_V']/IC['air_c']
    dTambdt = 0
    dzdt = [dTdt, dTinfdt, dTambdt]
    return dzdt