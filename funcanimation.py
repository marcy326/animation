# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 18:25:39 2018

@author: marcy
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


fig, ax = plt.subplots(1, 1, figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

theta = 180
delta = np.radians(theta)
X = np.zeros(3)
Y = np.zeros(3)
U = np.array((np.cos(0), 0, np.cos(0)))
V = np.array((0, np.cos(delta), np.cos(delta)))


fig.suptitle("δ = "+ str(theta) + "°", fontsize=18)


Q = ax.quiver(X, Y, U, V, color=('r','g','b'), angles='xy', scale_units='xy', scale=1)
unit = 5
def update_quiver(t, Q, X, Y):
    rad = np.radians(t*unit)
    U = np.array((np.cos(rad), 0, np.cos(rad)))
    V = np.array((0, np.cos(rad + delta), np.cos(rad + delta)))

    Q.set_UVC(U,V)

    return Q,

ani = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y), interval=20, frames=360//unit, blit=True)
#plt.show()
ani.save("funcanime-" + str(theta) + ".gif", writer='imagemagick')
