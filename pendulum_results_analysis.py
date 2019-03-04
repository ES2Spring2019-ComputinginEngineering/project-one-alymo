#Step 4: Analysis of Results
#Mo Liu and Alyssa Attonito
#This section applies a filter to the raw data and plot acceleration and angular position against time. 

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

s = []
t = []
g = 9.81
 
#openning the data file and extracting the data:
with open ("pendulum_data.txt", "r") as file:
    for line in file:
        line = line.rstrip().split(",")
        y_acceleration = float(line[1])
        time = float(line[2])
        s.append(y_acceleration)
        t.append(time)
    
#applying filter to the raw data:
y_noisy_filt = sig.medfilt(s)
y_noisy_pks, _ = sig.find_peaks(s)
y_noisy_filt_pks, _ = sig.find_peaks(y_noisy_filt)

#calculating theta from y acceleration:
theta = np.arcsin(y_noisy_filt / g)

#plotting y acceleration against time:
plt.plot(time, y_noisy_filt,'r-')
plt.xlabel('Time (seconds)')
plt.ylabel('Y Acceleration (m/s^2)')
plt.title('Y Acceleration vs Time Filtered')
plt.xlim((0, 20))
plt.grid()

#plotting theta against time:
plt.plot(time, theta,'b-')
plt.title('Noisy Median Filtered')
plt.xlabel('Time (seconds)')
plt.ylabel('Theta(radians)')
plt.title('Theta vs Time Filtered')
plt.xlim((0, 20))
plt.grid()

#test plot:
plt.plot(t, y_noisy_filt)
plt.show()