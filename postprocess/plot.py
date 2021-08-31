import matplotlib.pyplot as plt

def plot(t,y_BC,x,y):
    for key in y_BC:
        if "degR" in key:
            plt.plot(t,y_BC[key]-459.67,':',label=key)

    plt.plot(t,x-459.67,'b-',label='Tcontents(t)')
    plt.plot(t,y-459.67,'r--',label='T_air(t)')
    plt.ylabel('values')
    plt.xlabel('time')
    plt.legend(loc='best')
    plt.show()