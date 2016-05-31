
from os.path import os

import numpy as np


def vns(x, fun, kmax, tmax):
    t = 0
    while t < tmax:
        k = 1
        while k < kmax:
            x1 = shake(x, k)
            x2 = find_min_neig(x1, k, fun)

            if fun(x2) < fun(x):

                x = x2
                k = 1
            else:
                k = k + 1

        print 'x=', x
        print 'value=', fun(x)
        print 't=', t
        fun(x, prt=True)
        print '\n \n \n'


def find_min_neig(x, k, fun):
    xmin = x - k
    xmax = x + k
    xx = np.meshgrid(np.arange(xmin[0], xmax[0], 0.5), np.arange(xmin[1], xmax[1], 0.5), np.arange(
        xmin[2], xmax[2], 0.5), np.arange(xmin[3], xmax[3], 0.5), sparse=True)
    fx2 = fun(x)
    x2 = x
    for i1 in xx[0][0, :, 0, 0]:
        for i2 in xx[1][:, 0, 0, 0]:
            for i3 in xx[2][0, 0, :, 0]:
                for i4 in xx[3][0, 0, 0, :]:
                    xtest = np.array([i1, i2, i3, i4])
                    if fun(xtest) < fx2:
                        x2 = xtest
                        fx2 = fun(x2)
    return np.reshape(x2, (4, 1))


def vnd(x, k, fun):
    xmin = x - k
    xmax = x + k

    while (x > xmin).any() and (x < xmax).any():
        pass


def shake(x, k):
    return x +  0.5*np.random.randint(-k, k, size=(x.size, 1))
