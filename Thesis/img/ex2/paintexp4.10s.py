import numpy as np
import matplotlib.pyplot as plt

def plot_tables():
    
    dataf = np.loadtxt("dataexp4.100s")
    X = [ 2**x for x in range(1,51)]
  
    #legend
    fig = plt.figure()
    ax = fig.add_subplot(111)
 
    ax.set_xlabel('number of hidden states')
    ax.set_ylabel('time [s]')

    ax.set_xscale("log", nonposx='clip')
    

    plt.plot(X, dataf )  #whole time -al:float

    plt.legend()

    plt.show()


plot_tables()
