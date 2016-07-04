from VNS import vns
import numpy as np









def fun(x, prt=False):
    def i(x):
        i = np.zeros((7, 1))
        i[0, 0] = np.sign(-(np.dot(np.array([2, 2, 10, 20]), x) - 11))
        i[1, 0] = np.sign(-(np.dot(np.array([50, 20, 10, 30]), x) - 70))
        i[2, 0] = np.sign(-(np.dot(np.array([80, 70, 10, 80]), x) - 250))
        i[3, 0] = np.sign(-x[0])
        i[4, 0] = np.sign(-x[1])
        i[5, 0] = np.sign(-x[2])
        i[6, 0] = np.sign(-x[3])
        return i

    alfa = 100000 * np.ones((1, 7))

    f = np.dot(np.array([2, 4, 1.5, 1]), x)

    if prt:
        print 'i=', i(x)
        print 'f=', f

    return (1 * f + np.dot(alfa, i(x)))[0][0]


x0 = 10 * np.ones((4, 1))

vns(x0, fun, kmax=5, tmax=30)
