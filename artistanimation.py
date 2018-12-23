# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 14:59:58 2018

@author: marcy
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig, ax = plt.subplots(1, 1, figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

theta = -90
delta = np.radians(theta)
X = np.zeros(3)
Y = np.zeros(3)

fig.suptitle("δ = "+ str(theta) + "°", fontsize=18)

unit = 5
ims = []
for t in range(0, 360, unit):
    rad = np.radians(t)
    U = np.array((np.cos(rad), 0., np.cos(rad)))
    V = np.array((0., np.cos(rad + delta), np.cos(rad + delta)))
    im = ax.quiver(X, Y, U, V, color=('r','g','b'), angles='xy',scale_units='xy',scale=1)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=20, blit=True)
#plt.show()
ani.save("artistanime.gif", writer='imagemagick')


