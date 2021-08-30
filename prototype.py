import numpy as np
from scipy.integrate import odeint as solver

from BC.case_test import case_test as case
from plant.model import model as model
from postprocess.plot import plot as postprocess

[BC, IC] = case()

# initial conditions
z0 = [IC['x0'], IC['y0']]

# Number of data points
n = int(IC['tf']/IC['ts'])

# time points
t = np.linspace(0,IC['tf'],n)

# step input
u = np.zeros(n)
# change to 2.0 at time = 5.0

# store solution
x = np.empty_like(t)
y = np.empty_like(t)
# record initial conditions
x[0] = z0[0]
y[0] = z0[1]

# solve ODE
for i in range(1,n):
    # span for next time step
    tspan = [t[i-1],t[i]]
    # calc input
    u[i] = BC['temp'].lookup(t[i])
    # solve for next step
    z = solver(model,z0,tspan,args=(u[i],))
    # store solution for plotting
    x[i] = z[1][0]
    y[i] = z[1][1]
    # next initial condition
    z0 = z[1]

# plot results
postprocess(t, u, x, y)