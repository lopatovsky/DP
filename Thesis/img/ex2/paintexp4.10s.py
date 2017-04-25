import numpy as np
import matplotlib.pyplot as plt

def plot_tables():
    
    #d1 = np.loadtxt("dataexp4.1s") 
    d80 = np.loadtxt("dataexp4.80s")
    d100 = np.loadtxt("dataexp4.100s")
    d10 = np.loadtxt("dataexp4.10s")
    X = [ 2**x for x in range(1,51)]
    
    dataf = ( 8*d80 + 10*d100 + 1*d10 ) / 19

    #legend
    fig = plt.figure()
    ax = fig.add_subplot(111)
 
    ax.set_xlabel('approximate length of the time intervals')
    ax.set_ylabel('time [s]')

    ax.set_xscale("log", nonposx='clip')
    

    plt.plot(X, dataf )  #whole time -al:float

    plt.legend()

    plt.show()


plot_tables()
