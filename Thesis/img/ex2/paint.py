import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def plot_tables():
    
    ## SMALL dataset

    datai = np.loadtxt("table1", delimiter=',')
    dataf = np.loadtxt("table2", delimiter=',')
    X = range(2,41,2)
    X2 = range(2,29,2)
 
    ## BIG dataset

    #datai = np.loadtxt("table3", delimiter=',')
    #dataf = np.loadtxt("table4", delimiter=',')
    #X = range(2,37,2)
    #X2 = range(2,29,2)

    #legend
    fig = plt.figure()
    ax = fig.add_subplot(111)
 
    ax.set_xlabel('number of states')
    ax.set_ylabel('time [s]')

    

    #plot
    p1, = plt.plot(X, datai[0] , label="whole" )  #whole time -al:int
    p2, = plt.plot(X, datai[1] , label="expm" )  #expm -al:int
    p3, = plt.plot(X, datai[2] , label="sq-mult" )  #sq-mult -al:int

    p4, = plt.plot(X2, dataf[0] , label="whole")  #whole time -al:float
    p5, = plt.plot(X2, dataf[1] , label="expm ")  #expm -al:float

    title_proxy = Rectangle((0,0), 0, 0, color='w')

    plt.legend([title_proxy, p1, p2, p3, title_proxy, p4, p5 ], [r'integer-interval:', "whole","expm","sq-mult",r'float-interval:', "whole","expm"])
    

    #plt.legend()

    plt.show()


plot_tables()
