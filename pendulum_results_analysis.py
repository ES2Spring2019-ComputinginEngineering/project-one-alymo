import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.signal as sig

s = []
t = []
g = 9.81
 
with open ("pendulum_data.txt", "r") as file:
    for line in file:
        line = line.rstrip().split(",")
        y_acceleration = float(line[1])
        time = float(line[2])
        s.append(y_acceleration)
        t.append(time)
    

y_noisy_filt = sig.medfilt(s)
y_noisy_pks, _ = sig.find_peaks(s)
y_noisy_filt_pks, _ = sig.find_peaks(y_noisy_filt)

theta = np.arcsin(y_noisy_filt / g)

plt.subplot(2,2,2)
plt.plot(time, s, 'r-', time[y_noisy_pks], s[y_noisy_pks], 'b.')
plt.title('Noisy')


plt.subplot(2,2,4)
plt.plot(time, y_noisy_filt,'r-', time[y_noisy_filt_pks], y_noisy_filt[y_noisy_filt_pks], 'b.')
plt.title('Noisy Median Filtered')

plt.tight_layout()

plt.subplot(3,1,1)
plt.plot(t, s, 'y-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Y Acceleration (m/s^2)')
plt.title('Y Acceleration vs Time')
plt.xlim((0, 20))
plt.grid()

plt.plot(t, s)
plt.show()
