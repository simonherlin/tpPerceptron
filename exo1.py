import numpy as np


def generaterandomfile (filename):

    def function (array):

        if ((array[0] + array[1] - 1) > 0 ): #and array[1] > 0.5
            array = np.concatenate([array,[1]])
        else:
            array = np.concatenate([array,[-1]])
        return array

    table = np.random.rand(1000,2)
    table = np.apply_along_axis(function, 1, table)

    np.savetxt(filename, table , delimiter=' ')


generaterandomfile('app.csv')
generaterandomfile('gen.csv')
