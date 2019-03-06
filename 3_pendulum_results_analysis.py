#Step 3: Analysis of Results
#Mo Liu and Alyssa Attonito
#This section applies a filter to the raw data and plot acceleration and angular position against time. 

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

s = []
t = []
g = 9.81
 
#openning the data file and extracting the data:
with open ("pendulum_data_4.75.txt", "r") as file:
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
theta_pks, _ = sig.find_peaks(theta)

#plotting y acceleration against time:
plt.figure()
plt.plot(t, y_noisy_filt,'g-', t[y_noisy_filt_pks], y_noisy_filt[y_noisy_filt_pks], 'b.')
plt.xlabel('Time (seconds)')
plt.ylabel('Y Acceleration (m/s^2)')
plt.title('Y Acceleration vs Time Filtered')
plt.grid()
plt.show()

#plotting theta against time:
plt.figure()
plt.plot(t, theta,'b-', t[y_noisy_filt_pks], theta[y_noisy_filt_pks], 'g.')
plt.title('Noisy Median Filtered')
plt.xlabel('Time (seconds)')
plt.ylabel('Theta(radians)')
plt.title('Theta vs Time Filtered')
plt.grid()
plt.show()

#Determining period by averaging time differences
peaks = t[theta_pks]
time_difference = np.diff(peaks)
period = str(np.sum(time_difference)/len(time_difference))
print("Period: " + period + "s")

#a sampel file for testing: pendulum_data_4.75.txt
"""0.008,1.056,0.0019989
-0.02,1.032,0.0719986
0.012,1.0,0.137999
-0.052,0.944,0.204
0.044,1.136,0.27
0.02,1.064,0.334999
0.02,0.76,0.402
0.092,0.336,0.466999
-0.212,0.012,0.532999
-0.588,0.088,0.598999
-1.824,0.2,0.664999
-1.736,-0.08,0.73
-2.04,-0.104,0.796
-2.04,-0.024,0.862
-2.04,0.068,0.927999
-1.676,-0.104,0.993
-0.972,0.108,1.059
-0.664,0.1,1.125
-0.408,0.068,1.101
-0.44,-0.012,1.166
-0.532,0.028,1.233
-0.86,-0.016,1.298
-1.256,-0.032,1.364
-1.388,-0.12,1.43
-2.04,-0.292,1.495
-2.04,-0.252,1.561
-2.04,-0.224,1.626
-1.724,-0.2,1.692
-1.22,-0.276,1.758
-0.716,-0.176,1.824
-0.496,-0.2,1.892
-0.276,-0.156,1.959
-0.328,-0.1,2.024
-0.652,-0.084,2.092
-1.156,-0.156,2.159
-1.504,-0.104,2.224
-1.996,-0.016,2.29
-2.04,-0.14,2.356
-2.04,0.088,2.421
-1.756,-0.168,2.485
-1.028,0.024,2.552
-0.94,0.096,2.618
-0.62,0.032,2.684
-0.428,0.036,2.75
-0.584,0.02,2.815
-0.76,-0.04,2.882
-1.392,-0.076,2.949
-1.764,-0.132,3.016
-2.04,-0.252,3.081
-2.04,-0.26,3.147
-2.016,-0.264,3.213
-1.472,-0.228,3.278
-0.976,-0.128,3.344
-0.592,-0.184,3.41
-0.496,-0.076,3.476
-0.46,-0.06,3.541
-0.464,-0.02,3.607
-0.736,-0.056,3.673
-1.22,-0.056,3.739
-1.788,-0.152,3.804
-2.04,-0.164,3.874
-2.04,0.04,3.941
-1.888,-0.152,4.006
-1.5,0.216,4.073
-1.14,0.06,4.139
-0.736,0.092,4.204
-0.52,0.088,4.27
-0.496,0.072,4.336
-0.732,0.02,4.402
-1.2,-0.04,4.466
-1.668,-0.136,4.532
-2.04,-0.212,4.599
-2.04,-0.22,4.665
-1.772,-0.22,4.73
-1.684,-0.12,4.796
-1.1,-0.12,4.862
-0.644,-0.076,4.927
-0.496,-0.116,4.993"""
