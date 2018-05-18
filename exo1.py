import numpy as np
import sys
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

def function (array):
    if ((array[0] + array[1] - 1) > 0 ):
        array = np.concatenate([array,[1]])
    else:
        array = np.concatenate([array,[-1]])
    return array

table = np.random.rand(100,2)

table = np.apply_along_axis(function, 1, table)
plt.scatter(table[:,0], table[:,1],s=100)
np.savetxt('result.txt', table, delimiter=' ')
plt.show()
