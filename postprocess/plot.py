import matplotlib.pyplot as plt

def plot(t,u,x,y):
    plt.plot(t,u,'g:',label='u(t)')
    plt.plot(t,x,'b-',label='x(t)')
    plt.plot(t,y,'r--',label='y(t)')
    plt.ylabel('values')
    plt.xlabel('time')
    plt.legend(loc='best')
    plt.show()