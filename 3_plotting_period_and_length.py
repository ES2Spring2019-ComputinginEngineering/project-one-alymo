#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:29:19 2019

@author: alyssa
"""

import matplotlib.pyplot as plt

#Note: These Numbers plot simulation data; need to be modified to graph other
Length_of_Pendulum= [0.12065, 0.2159, 0.3429, 0.4699, 0.5969] 
Period_of_Pendulum= [0.6448, 0.6708,0.6210, 0.5008, 0.7255]


plt.plot(Length_of_Pendulum, Period_of_Pendulum)
plt.xlabel('Log(Pendulum Length)')
plt.ylabel('Log(Pendulum Period)')
plt.yscale('log')
plt.xscale('log')
plt.title('Pendulum Length and Period for Simulation')
plt.grid(True)
