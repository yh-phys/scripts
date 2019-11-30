#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
#colors=['f0a3ff', '0075dc', '993f00', '4c005c', '426600', 'ff0010', '9dcc00', 'c20088', '003380', 'ffa405', 'ffff00', 'ff5005', '5ef1f2', '740aff', '990000', '00998f', '005c31', '2bce48', 'ffcc99', '94ffb5', '8f7c00', '6fa8bb', '808080']
colors=['3953a4', 'faa316', 'd93b2b', '0db14b', 'f0a3ff', '0075dc', '993f00', '4c005c', '426600', 'ff0010', '9dcc00', 'c20088', '003380', 'ffa405', 'ffff00', 'ff5005', '5ef1f2', '740aff', '990000', '00998f', '005c31', '2bce48', 'ffcc99', '94ffb5', '8f7c00', '6fa8bb', '808080']
x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x)+np.cos(x)*np.sin(x)+np.cos(2*x)**2
fig= plt.figure(figsize=(5.0,40))
for i in range(len(colors)):
    ax=fig.add_subplot(len(colors), 1, i+1)
    icolor='#'+colors[i]
    ax.plot(x,y,color=icolor,lw=1,alpha=0.9,label='#'+colors[i])
    ax.fill_between(x, 0, y,facecolor=icolor,alpha=0.25)
    plt.xlim(0, 2*np.pi)
    ax.legend()
plt.savefig('colors.pdf',dpi=600)

#plt.show()
