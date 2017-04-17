import numpy as np
import matplotlib.pyplot as plt

def plot_tables():
    
    ## SMALL dataset

    #datai = np.loadtxt("table1", delimiter=',')
    #dataf = np.loadtxt("table2", delimiter=',')
    #X = range(2,41,2)
    #X2 = range(2,29,2)
    
    
    ## BIG dataset

    datai = np.loadtxt("table3", delimiter=',')
    dataf = np.loadtxt("table4", delimiter=',')
    X = range(2,37,2)
    X2 = range(2,29,2)

    #legend
    fig = plt.figure()
    ax = fig.add_subplot(111)
 
    ax.set_xlabel('number of hidden states')
    ax.set_ylabel('time [s]')

    #plot
    plt.plot(X, datai[0] , label="whole" )  #whole time -al:int
    plt.plot(X, datai[1] , label="expm" )  #expm -al:int
    plt.plot(X, datai[2] , label="sq-mult" )  #sq-mult -al:int

    

    plt.plot(X2, dataf[0] , label="whole")  #whole time -al:float
    plt.plot(X2, dataf[1] , label="expm ")  #expm -al:float

    plt.legend()

    plt.show()


plot_tables()
