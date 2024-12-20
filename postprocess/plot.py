import matplotlib.pyplot as plt

def plot(t,y_BC,x,y):
    for key in y_BC:
        if "degR" in key:
            plt.plot(t,y_BC[key]-459.67,':',label=key.split('_')[0])

    plt.plot(t,x-459.67,'b-',label='Tstructure(t) degF')
    plt.plot(t,y-459.67,'r--',label='Tair(t) degF')
    plt.plot(t,y_BC['AC_W']/y_BC['AC_W']*100, label='AC On')
    plt.ylabel('values')
    plt.xlabel('time')
    plt.legend(loc='best')
    plt.show()