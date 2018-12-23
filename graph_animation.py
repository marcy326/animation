# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 15:55:56 2018

@author: marcy
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig = plt.figure(figsize=(6, 6))
plt.xlim([-1, 1])
plt.ylim([-1, 1])

deg = -45
delta = np.radians(deg)

x = np.zeros(3)
y = np.zeros(3)


ims = []
for t in range(0, 360, 5):
    theta = np.radians(t)
    u = (np.cos(theta), 0, np.cos(theta))
    v = (0, np.cos(theta + delta), np.cos(theta + delta))
    im = plt.quiver(x, y, u, v, color=('r','g','b'), angles='xy',scale_units='xy',scale=1)
    ims.append([im])

plt.title("δ = " + str(deg) + "°", fontsize=18)
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True)
plt.show()
ani.save("artistanimation_" + str(deg) + ".gif", writer='imagemagick')
