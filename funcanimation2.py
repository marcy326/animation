# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 23:57:40 2018

@author: marcy
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


fig = plt.figure(figsize=(6, 6))
plt.xlim([-1, 1])
plt.ylim([-1, 1])

#パラメータを代入
deg = 180
delta = np.radians(deg)

#初期ベクトルを設定
X = np.zeros(3)
Y = np.zeros(3)
U = np.array((np.cos(0), 0, np.cos(0)))
V = np.array((0, np.cos(delta), np.cos(delta)))
Q = plt.quiver(X, Y, U, V, color=('r','g','b'), angles='xy', scale_units='xy', scale=1)

#ベクトルを更新
unit = 5
def update_quiver(t, Q, X, Y):
    theta = np.radians(t*unit)
    U = np.array((np.cos(theta), 0, np.cos(theta)))
    V = np.array((0, np.cos(theta + delta), np.cos(theta + delta)))

    Q.set_UVC(U,V)

    return Q,


plt.title("δ = " + str(deg) + "°", fontsize=18)
ani = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y), interval=50, frames=360//unit, blit=True)
plt.show()
ani.save("funcanimation_" + str(deg) + ".gif", writer='imagemagick')
