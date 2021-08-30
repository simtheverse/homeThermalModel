# function that returns dz/dt
def model(z,t,y_BC,i):
    x = z[0]
    y = z[1]
    dxdt = (-x + y_BC['temp'][i])/2.0
    dydt = (-y + x)/5.0
    dzdt = [dxdt,dydt]
    return dzdt