
from os.path import os

import numpy as np
import itertools as it
import math
import matplotlib.pyplot as plt


class VNS_TSP(object):

    def __init__(self, d, pos):
        self.d = d
        self.n = d.shape[0]
        self.s = range(self.n)
        np.random.shuffle(self.s)
        self.s = list(self.s)
        self.pos = pos

    def cost(self, s):
        c = 0
        for i in range(self.n):
            c = c + self.d[s[i], s[i - 1]]
        return c

    def vnd(self, s, l):

        c = self.cost(s)

        for i in range(self.n):
            s_new = np.copy(s)
            s_new[i] = s[i - l]
            s_new[i - l] = s[i]
            c_new = self.cost(s_new)
            if c_new < c:
                c = c_new
                s = np.copy(s_new)
        return s

    def shake(self, s, k):
        s_out = np.copy(s)

        for i in range(k):
            rand = np.random.randint(0, self.n, 2)
            s_out[rand[0]] = s[rand[1]]
            s_out[rand[1]] = s[rand[0]]
            s = np.copy(s_out)
        return s_out

    def run(self):

        for k in range(1, 40):
            sl = self.shake(self.s, k)
            for l in range(1, 10):
                sll = self.vnd(sl, l)
                if any(sll != sl):
                    sl = sll
                    l = 0
#                     plt.figure()
#                     plt.plot(self.pos[:, 0], self.pos[:, 1],'go')
#                     plt.hold(True)
#                     plt.plot(self.pos[sl, 0], self.pos[sl, 1])
#                     plt.show()
                    
            if self.cost(sl) < self.cost(self.s):
                self.s = sl
                k = 0


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
    return x + 0.5 * np.random.randint(-k, k, size=(x.size, 1))
