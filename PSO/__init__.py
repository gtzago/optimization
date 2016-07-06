import time

import matplotlib.pyplot as plt
import numpy as np


class ParticleSwarmOptimization(object):

    def __init__(self, cost, d, min=-10, max=10, n=100, c1=0.1, c2=0.1, w=0.5):

        self.n = n  # number of particles.
        self.d = d  # number of dimensions.
        self.w = w  # inertia.
        self.c1 = c1  # acceleration constant towards best particle position.
        self.c2 = c2  # acceleration constant towards best global position.
        # particle positions.
        self.x = 1.0 * np.random.randint(min, max, (self.n, self.d))
        # particle best visited positions.
        self.p = np.copy(self.x)
        # particle velocities.
        self.v = 0.01 * np.random.randint(min, max, (self.n, self.d))
        self.cost = cost  # cost function supplied by the user.
        self.min = min
        self.max = max

        costs = []
        for i in range(self.n):
            costs.append(self.cost(self.x[i]))
        self.g = self.x[np.argmin(costs), :]

    def run(self, max_iter=1000):
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        line1, = ax.plot(self.x[:, 0], self.x[:, 1], 'go')
        plt.grid(True)

        for iter in range(max_iter):
            print 'Iteration {:d}'.format(iter)
            print 'Minimum cost {:3.1f}'.format(self.cost(self.g))
            
            for i in range(self.n):
                self.v[i, :] = self.w * self.v[i, :] + self.c1 * np.random.rand() * (
                    self.p[i, :] - self.x[i, :]) + self.c2 * np.random.rand() * (self.g - self.x[i, :])
                self.x[i, :] = self.x[i, :] + self.v[i, :]
                if self.x[i, 0] > self.max:
                    self.x[i, 0] = self.max
                if self.x[i, 0] < self.min:
                    self.x[i, 0] = self.min
                if self.x[i, 1] > self.max:
                    self.x[i, 1] = self.max
                if self.x[i, 1] < self.min:
                    self.x[i, 1] = self.min

                if self.cost(self.x[i, :]) < self.cost(self.p[i, :]):
                    self.p[i, :] = self.x[i, :]
                    if self.cost(self.x[i, :]) < self.cost(self.g):
                        self.g = self.x[i, :]
            line1.set_xdata(self.x[:, 0])
            line1.set_ydata(self.x[:, 1])
            fig.canvas.draw()
#             time.sleep(0.1)
