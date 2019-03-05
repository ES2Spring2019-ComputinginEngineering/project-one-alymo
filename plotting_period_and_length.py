#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:29:19 2019

@author: alyssa
"""

import matplotlib.pyplot as plt

Length_of_Pendulum= [0.12065, 0.2159, 0.3429, 0.4699, 0.5969] 
Period_of_Pendulum= [1.000, 1.207,1.461, 1.683, 1.882] #last data point made up


plt.plot(Length_of_Pendulum, Period_of_Pendulum)
plt.xlabel('Pendulum Length')
plt.ylabel('Pendulum Period')
plt.yscale('log')
plt.xscale('log')
plt.title('Pendulum Length and Period for Simulation')
plt.grid(True)

#Real World Data
#Length_of_Pendulum= [0.12065, 0.2159, 0.3429, 0.4699, 0.5969] 
#Period_of_Pendulum= [0.6561, 0.8014,0.6091, 0.5376, 0.4753] #last data point made up