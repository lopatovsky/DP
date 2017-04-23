import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def plot_tables():
    
    datai = np.loadtxt("2/table1", delimiter=',')
    dataf = np.loadtxt("2/table2", delimiter=',')
    X = [ 2**x for x in range(1,57)]
    X2 = [ 2**x for x in range(1,56)]

    #X = [ x for x in range(1,57)]
    #X2 = [ x for x in range(1,56)]
    


    #legend
    fig = plt.figure()
    ax = fig.add_subplot(111)
 
    ax.set_xlabel('max time interval [s]')
    ax.set_ylabel('time [s]')


    ax.set_xscale("log", nonposx='clip')
  
    #plot
    p1, = plt.plot(X, datai[0] , label="whole" )  #whole time -al:int
    p2, = plt.plot(X, datai[1] , label="expm" )  #expm -al:int
    p3, = plt.plot(X, datai[2] , label="sq-mult" )  #sq-mult -al:int

    p4, = plt.plot(X2, dataf[0] , label="whole")  #whole time -al:float
    p5, = plt.plot(X2, dataf[1] , label="expm ")  #expm -al:float

    title_proxy = Rectangle((0,0), 0, 0, color='w')

    plt.legend([title_proxy, p1, p2, p3, title_proxy, p4, p5 ], [r'integer-interval:', "whole","expm","sq-mult",r'float-interval:', "whole","expm"])

    plt.show()


plot_tables()
