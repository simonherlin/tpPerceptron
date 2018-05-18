import numpy as np
import sys
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

def function (array):
    if ((array[0] + array[1] - 1) > 0):
    #if ((array[0] + array[1] - 1) > 0 and array[1] > 0.5):
        array = np.concatenate([array,[1]])
    else:
        array = np.concatenate([array,[-1]])
    return array

table = np.random.rand(1000,2)

table = np.apply_along_axis(function, 1, table)
np.savetxt('result.txt', table, delimiter=' ')
plt.show()
