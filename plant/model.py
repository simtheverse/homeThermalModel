# function that returns dz/dt

def Qconvection(h,As, Text, Tint):
    W = h*As*(Text-Tint)

    return W  # watts entering system

def model(z,t,y_BC,i,Parameters):
    Tcontents_degR = z[0]
    Tair_degR = z[1]
    Tamb_degR = y_BC['Tamb_degR'][i]



    # Room contents calc
    Q_solar_load = 500 * y_BC['UVIndex']/9 #W
    Q_convection_contents_room = Qconvection(Parameters['plant_roomAir']['h'], Parameters['plant_contents']['As'], Tcontents_degR, Tair_degR)
    dTcontentsdt = (-Q_convection_contents_room + Q_solar_load)/Parameters['plant_contents']['rho']/Parameters['plant_contents']['V']/Parameters['plant_contents']['c']


    ## Room air calc
    Tair_rho = y_BC['Pamb_Pa'][i]/Parameters['plant_roomAir']['r_specific_J_per_kgR']/Tair_degR
    Q_convection_amb_room = Qconvection(Parameters['plant_roomAir']['h'], Parameters['plant_roomAir']['As'], Tamb_degR, Tair_degR)
    Q_heatload = Parameters['plant_Person']['heatload_W'] * y_BC['numberOfPeople'][i] + y_BC['appliance_heatload_W'][i]
    Q_AC = y_BC['AC_W'][i]


    Qnet = (Q_convection_amb_room+Q_heatload+Q_convection_contents_room-Q_AC)

    dTairdt = Qnet /Tair_rho/Parameters['plant_roomAir']['V']/Parameters['plant_roomAir']['c']

    dzdt = [dTcontentsdt, dTairdt]
    return dzdt