import numpy as np
from scipy.integrate import odeint as solver
from BC.BC_Utilities import *

from BC.case_test import case_test as case
from plant.model import model as model
from postprocess.plot import plot as postprocess

[BC, IC] = case()

# Number of data points
n = int(IC['tf']/IC['ts'])

# time points
t = np.linspace(0,IC['tf'],n)
# resample BCs
y_BC = resample_dict(BC,t)
# store solution
T = np.empty_like(t)
Tinf = np.empty_like(t)

# initial conditions
z0 = [IC['T0'], IC['Tinf0'], IC['Tamb']]
# record initial conditions
T[0] = z0[0]
Tinf[0] = z0[1]


# solve ODE
for i in range(1,n):
    # span for next time step
    tspan = [t[i-1],t[i]]
    # solve for next step
    z = solver(model,z0,tspan,args=(y_BC,i,IC,))
    # store solution for plotting
    T[i]    = z[1][0]
    Tinf[i] = z[1][1]
    # next initial condition
    z0 = z[1]

# plot results
postprocess(t, y_BC, T, Tinf)