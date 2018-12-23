# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 17:24:09 2018

@author: marcy
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig = plt.figure(figsize=(6, 6))
plt.xlim([-1, 1])
plt.ylim([-1, 1])

#角度を定義
deg = -90
delta = np.radians(deg)
theta = 45
theta = np.radians(theta)

#ベクトルを定義
x = np.zeros(3)
y = np.zeros(3)
u = (np.cos(theta), 0, np.cos(theta))
v = (0, np.cos(theta + delta), np.cos(theta + delta))

plt.quiver(x, y, u, v, color=('r','g','b'), angles='xy',scale_units='xy',scale=1)

plt.title("δ = " + str(deg) + "°", fontsize=18)
plt.show()
