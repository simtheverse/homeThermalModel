# function that returns dz/dt
def model(z,t,y_BC,i,Parameters):
    Tcontents_degR = z[0]
    Tair_degR = z[1]
    Tamb_degR = y_BC['Tamb_degR'][i]

    Tair_rho = y_BC['Pamb_Pa'][i]/Parameters['air']['r_specific_J_per_kgR']/Tair_degR

    dTcontentsdt = -Parameters['contents']['h']*Parameters['contents']['As']/Tair_rho/Parameters['contents']['V']/Parameters['contents']['c']*(Tcontents_degR-Tair_degR)
    dTairdt = (-Parameters['air']['h']*Parameters['air']['As']*((Tair_degR-Tcontents_degR)+(Tair_degR-Tamb_degR))+.1)/Tair_rho/Parameters['air']['V']/Parameters['air']['c']

    dzdt = [dTcontentsdt, dTairdt]
    return dzdt