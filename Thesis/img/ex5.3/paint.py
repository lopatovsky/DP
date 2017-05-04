import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def plot_tables():


    d5 = np.loadtxt("d10", delimiter=',')

    fig = plt.figure()

    ax = fig.add_subplot(111)
    ax.set_xlabel('iterations')
    ax.set_ylabel('performance ratio')

    plt.plot( d5[0], label = "train sparse"  )
    plt.plot( d5[1], label = "test sparse"  )
    plt.plot( d5[2], label = "train dense"  )
    plt.plot( d5[3], label = "test dense"  )
    plt.legend()
    fig.show()
    input()

plot_tables()
