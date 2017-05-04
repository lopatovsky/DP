import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def plot_tables():


    s = np.loadtxt("sparse", delimiter=',')
    d = np.loadtxt("dense", delimiter=',')
    Xs = range(5,140,5)
    Xd = range(5,80,5)

    fig = plt.figure()

    ax = fig.add_subplot(111)
    ax.set_xlabel('number of states')
    ax.set_ylabel('time [s]')

    plt.plot( Xs , s, label = "sparse matrix"  )
    plt.plot( Xd , d, label = "dense matrix"  )
    plt.legend()
    fig.show()
    input()

plot_tables()
