# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:17:32 2023

"""

import matplotlib.pyplot as plt
import numpy as np



def nanometer(sizes):
    y = (1 - 1.5 * (R / sizes) + (0.5) * (R/sizes)**3) * N #formular to get CN from particle DIAMETER
    return y

N = 12      # CN of FCC
R = 0.264   # bond distance from EXAFS fit in Angstrom 
CN = 9.4    # coordination number from EXAFS fit

x = np.arange(1, 10, 0.1)

y = nanometer(x)


particleSize = np.interp(CN, y, x) # obtain particle size for a given CN

plt.title("Particle Size Sample Name")     # add sample name
plt.xlabel("particle size [nm]")
plt.ylabel("coordination number")
plt.xlim(0, 10)
plt.ylim(nanometer(1), 12)
plt.xticks(np.arange(0, 11, 1))
plt.plot(x, y)

plt.text(3, 9, r'$CN_{particle}=(1-1.5 \frac{R}{d}+0.5 (\frac{R}{d})^3) CN_{bulk}$', fontsize=12)
x_coord = particleSize
y_coord = CN




x_highlighting = [0, x_coord, x_coord]
y_highlighting = [y_coord, y_coord, nanometer(1)]

plt.plot(x_highlighting, y_highlighting, color='grey', linestyle='dashed')

plt.plot(particleSize, CN, color='red', marker='o',
     markerfacecolor='red', markersize=3)

