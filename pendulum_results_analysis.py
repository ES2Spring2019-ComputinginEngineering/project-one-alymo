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

#convert the list to np.array
t = np.asarray(t)
    
#applying filter to the raw data:
y_noisy_filt = sig.medfilt(s)
y_noisy_filt_pks, _ = sig.find_peaks(y_noisy_filt)

#calculating theta from y acceleration:
theta = np.arcsin(y_noisy_filt / g)

#plotting y acceleration against time:
plt.subplot(2, 1, 1)
plt.plot(t, y_noisy_filt,'g-', t[y_noisy_filt_pks], y_noisy_filt[y_noisy_filt_pks], 'b.')
plt.xlabel('Time (seconds)')
plt.ylabel('Y Acceleration (m/s^2)')
plt.title('Y Acceleration vs Time Filtered')
plt.grid()

#plotting theta against time:
plt.subplot(2, 1, 2)
plt.plot(t, theta,'b-', t[y_noisy_filt_pks], theta[y_noisy_filt_pks], 'g.')
plt.title('Noisy Median Filtered')
plt.xlabel('Time (seconds)')
plt.ylabel('Theta(radians)')
plt.title('Theta vs Time Filtered')
plt.grid()

plt.tight_layout()
plt.show()

#Determining period by averaging time differences
peaks = t[y_noisy_filt_pks]
time_difference = np.diff(peaks)
period = str(np.sum(time_difference)/len(time_difference))
print("Period: " + period + "s")