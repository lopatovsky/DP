import numpy as np
import matplotlib.pyplot as plt

def plot_tables():
    
    datai = np.loadtxt("2/table1", delimiter=',')
    dataf = np.loadtxt("2/table2", delimiter=',')
    X = [ 2**x for x in range(1,56)]
    X2 = [ 2**x for x in range(1,56)]
    


    #legend
    fig = plt.figure()
    ax = fig.add_subplot(111)
 
    ax.set_xlabel('number of hidden states')
    ax.set_ylabel('time [s]')

    ax.set_xscale("log", nonposx='clip')

    #plot
    plt.plot(X, datai[0] , label="whole" )  #whole time -al:int
    plt.plot(X, datai[1] )  #expm -al:int
    plt.plot(X, datai[2] )  #sq-mult -al:int

    

    plt.plot(X2, dataf[0] )  #whole time -al:float
    plt.plot(X2, dataf[1] )  #expm -al:float

    plt.legend()

    plt.show()


plot_tables()
