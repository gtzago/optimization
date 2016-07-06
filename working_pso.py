from PSO import ParticleSwarmOptimization
import numpy as np


def cost1(x):
    'global minimum at (0,0)'
    c = -(1 + np.cos(12 * np.sqrt(np.power(x[0], 2) + np.power(x[1], 2)))) / (
        0.5 * (np.power(x[0], 2) + np.power(x[1], 2)) + 2)
    return c


def eggholder(x):
    'global minimum at (512,404), f = -959.6407 evaluated at [-512,512]'
    c = -(x[1] + 47) * np.sin(np.sqrt(np.abs(x[1] + (x[0] / 2) + 47))) - \
        x[0] * np.sin(np.sqrt(np.abs(x[0] - (x[1] + 47))))
    return c

pso = ParticleSwarmOptimization(
    cost=eggholder, d=2, min=-512, max=512, n=5000, c1=0.1, c2=0.7, w=0.7)
 
pso.run(max_iter=100)
