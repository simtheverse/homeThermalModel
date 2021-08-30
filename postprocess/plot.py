import matplotlib.pyplot as plt

def plot(t,y_BC,x,y):
    for key in y_BC:
        plt.plot(t,y_BC[key],':',label=key)

    plt.plot(t,x,'b-',label='x(t)')
    plt.plot(t,y,'r--',label='y(t)')
    plt.ylabel('values')
    plt.xlabel('time')
    plt.legend(loc='best')
    plt.show()