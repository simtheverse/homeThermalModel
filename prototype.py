import numpy as np
from scipy.integrate import odeint as solver
from BC.BC_Utilities import *

from BC.case_test import case_test as case
from plant.model import model as model
from postprocess.plot import plot as postprocess

[BC, Parameters] = case()

# Number of data points
n = int(Parameters['tf']/Parameters['ts'])

# time points
t = np.linspace(0,Parameters['tf'],n)
# resample BCs
y_BC = resample_dict(BC,t)
# store solution
Tair_degR = np.empty_like(t)
Tinf_degR = np.empty_like(t)

# initial conditions
z0 = [Parameters['IC']['T0_degR'], Parameters['IC']['Tinf0_degR']]
# record initial conditions
Tair_degR[0] = z0[0]
Tinf_degR[0] = z0[1]


# solve ODE
for i in range(1,n):
    # span for next time step
    tspan = [t[i-1],t[i]]
    # solve for next step
    z = solver(model,z0,tspan,args=(y_BC,i,Parameters,))
    # store solution for plotting
    Tair_degR[i] = z[1][0]
    Tinf_degR[i] = z[1][1]
    # next initial condition
    z0 = z[1]

# plot results
postprocess(t, y_BC, Tair_degR, Tinf_degR)