#Step 1 and 2: Simulation
#Mo Liu and Alyssa Attonito
#This section creates a simulation that allows the user to visualize and analyze the simulated data. 

import numpy as np
import math
import matplotlib.pyplot as plt

#change l according to length of pendulum
g = 9.81
l = 0.50

#updates values with time:
def update_pendulum(ang_pos, ang_vel, ang_acc, time1, time2):
    dt = time2-time1
    ang_vel_new = ang_vel+ang_acc*dt
    ang_pos_new = ang_pos+ang_vel*dt
    ang_acc_new = g/l*math.sin(ang_pos)
    return ang_pos_new, ang_vel_new, ang_acc_new

#prints values:
def print_pendulum(time, ang_pos, ang_vel, ang_acc):
    print("TIME:     ", time)
    print("ANGULAR POSITION: ", ang_pos)
    print("ANGULAR VELOCITY: ", ang_vel)
    print("ANGULAR ACCELERATION: ", ang_acc, "\n")

#initial values in lists:
ang_pos = [math.pi/2]
ang_vel = [0]
ang_acc = [0]
time = np.linspace(0,20,40000)
print_pendulum(time[0], ang_pos[0], ang_vel[0], ang_acc)

#iterating the update:
i = 1
while i < len(time):
    ang_pos_new, ang_vel_new, ang_acc_new = update_pendulum(ang_pos[i-1], ang_vel[i-1], ang_acc[i-1], time[i-1], time[i])
    ang_pos.append(ang_pos_new)
    ang_vel.append(ang_vel_new)
    ang_acc.append(ang_acc_new)
    i += 1

#reassigning variables to np:
time = np.asarray(time)
ang_pos = np.asarray(ang_pos)
ang_vel = np.asarray(ang_vel)
ang_acc = np.asarray(ang_acc)

ang_pos_peaks, _ = sig.find_peaks(ang_pos)
ang_vel_peaks, _ = sig.find_peaks(ang_vel)
ang_acc_peaks, _ = sig.find_peaks(ang_acc)

#plotting simulation data:
plt.figure(figsize = (4, 6))


plt.subplot(3,1,1)
plt.plot(time, ang_pos, 'g-', time[ang_pos_peaks], ang_pos[ang_pos_peaks], 'b.') 
plt.xlabel('Time (seconds)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.xlim((0, 20)) 
plt.grid()


plt.subplot(3,1,2)
plt.plot(time, ang_vel, 'g-', time[ang_vel_peaks], ang_vel[ang_vel_peaks], 'b.')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')
plt.xlim((0, 20)) 
plt.grid()


plt.subplot(3,1,3)
plt.plot(time, ang_acc, 'g-', time[ang_acc_peaks], ang_acc[ang_acc_peaks], 'b.')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs Time')
plt.xlim((0, 20)) 
plt.grid()

plt.tight_layout()
plt.show()

#determining the period:
peaks = time[ang_acc_peaks]
time_difference = np.diff(peaks)
period = str(np.sum(time_difference)/len(time_difference))
print("Period: " + period + "s")

