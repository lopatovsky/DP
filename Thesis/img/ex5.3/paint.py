import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def plot_mixed_tables():


    d1 = np.loadtxt("d10", delimiter=',')
    d2 = np.loadtxt("d20", delimiter=',')

    fig = plt.figure()

    ax = fig.add_subplot(111)
    ax.set_xlabel('iterations')
    ax.set_ylabel('performance ratio')

    plt.plot( d1[1], label = "10 sparse"  )
    plt.plot( d1[3], label = "10 dense"  )
    plt.plot( d2[1], label = "20 sparse"  )
    plt.plot( d2[3], label = "20 dense"  )
    plt.legend()
    fig.show()
    input()


def plot_tables():


    d1 = np.loadtxt("d20", delimiter=',')

    fig = plt.figure()

    ax = fig.add_subplot(111)
    ax.set_xlabel('iterations')
    ax.set_ylabel('performance ratio')

    plt.plot( d1[0], label = "train sparse"  )
    plt.plot( d1[1], label = "test sparse"  )
    plt.plot( d1[2], label = "train dense"  )
    plt.plot( d1[3], label = "test dense"  )
    plt.legend()
    fig.show()
    input()

plot_mixed_tables()
