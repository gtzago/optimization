import csv

from VNS import VNS_TSP
import numpy as np
import matplotlib.pyplot as plt


with open('./database/att48_d.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    d = np.array([])
    count = 0
    for row in reader:
        aux = [int(i) for i in row]
        d = np.append(d, aux)
        count += 1

    d = np.reshape(d, (count, count))

with open('./database/att48_xy.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    pos = np.array([])
    count = 0
    for row in reader:
        aux = [int(i) for i in row]
        pos = np.append(pos, aux)
        count += 1

    pos = np.reshape(pos, (-1, 2))


with open('./database/att48_s.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    s = np.array([])
    count = 0
    for row in reader:
        aux = [int(i) for i in row]
        s = np.append(s, aux)
        count += 1

    s = np.reshape(s, (-1, 1))
    s = s[:-1, :].astype(int)
    s = np.ravel(s)
    s = s - 1


# d = d[0:15, 0:15]
# pos = pos[0:15, :]

vns = VNS_TSP(d=d, pos=pos)
vns.run()
plt.figure()
plt.plot(pos[:, 0], pos[:, 1], 'go')
plt.hold(True)
plt.plot(pos[vns.s, 0], pos[vns.s, 1])


# plt.figure()
# plt.plot(pos[:, 0], pos[:, 1],'go')
# plt.hold(True)
# plt.plot(pos[s, 0], pos[s, 1])
plt.show()
