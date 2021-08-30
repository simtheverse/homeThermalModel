import matplotlib.pyplot as plt

def plot(t,y_BC,x,y):
    for key in y_BC:
        plt.plot(t,y_BC[key],':',label=key)

    plt.plot(t,x-459.67,'b-',label='T(t)')
    plt.plot(t,y-459.67,'r--',label='T_air(t)')
    plt.ylabel('values')
    plt.xlabel('time')
    plt.legend(loc='best')
    plt.show()