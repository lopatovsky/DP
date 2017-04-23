import numpy as np
import matplotlib.pyplot as plt

def plot_tables():
    
    dataf = np.loadtxt("tableexp4", delimiter=',')
    X = [ 2**x for x in range(1,57)]
  
    #legend
    fig = plt.figure()
    ax = fig.add_subplot(111)
 
    ax.set_xlabel('number of hidden states')
    ax.set_ylabel('time [s]')

    ax.set_xscale("log", nonposx='clip')
    

    plt.plot(X, dataf[0] )  #whole time -al:float
    plt.plot(X, dataf[1] )  #expm -al:float

    plt.legend()

    plt.show()


plot_tables()
