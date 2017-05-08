import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

data = np.loadtxt("big_train", delimiter=' ')

fig = plt.figure()

ax = fig.add_subplot(111)
ax.set_xlabel('iterations')
ax.set_ylabel('performance ratio')

runs = 5

for states in range(2,9):

    plt.plot(  range(1,101), data[states][1:] / runs, label = str(states)  )
   

plt.legend()
    

plt.show()
input()
