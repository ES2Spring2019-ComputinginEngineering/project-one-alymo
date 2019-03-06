#Step 4: Plotting Pendulum Length and Period
#Mo Liu and Alyssa Attonito
#This section generates log-log graphs to showcase the difference between the simulation and real-world data.


import matplotlib.pyplot as plt

#Note: Input numbers here to graph in the plot
Length_of_Pendulum= [0.12065, 0.2159, 0.3429, 0.4699, 0.5969] 
Period_of_Pendulum= [0.6448, 0.6708,0.6210, 0.5008, 0.7255]


plt.plot(Length_of_Pendulum, Period_of_Pendulum)
plt.xlabel('Log(Pendulum Length)')
plt.ylabel('Log(Pendulum Period)')
plt.yscale('log')
plt.xscale('log')
plt.title('Pendulum Length and Period for Simulation') #Note: change title as needed
plt.grid(True)
