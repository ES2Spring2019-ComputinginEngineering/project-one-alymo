import numpy as np
import math
import matplotlib.pyplot as plt

def update_pendulum(ang_pos, ang_vel, ang_acc, time1, time2):
    dt = time2-time1
    ang_vel_new = ang_vel+ang_acc*dt
    ang_pos_new = ang_pos+ang_vel*dt
    ang_acc_new = 9.8*(math.pi/2-ang_pos_new)
    return ang_pos_new, ang_vel_new, ang_acc_new

def print_pendulum(time, ang_pos, ang_vel, ang_acc):
    print("TIME:     ", time)
    print("ANGULAR POSITION: ", ang_pos)
    print("ANGULAR VELOCITY: ", ang_vel)
    print("ANGULAR ACCELERATION: ", ang_acc, "\n")

ang_pos = [0]
ang_vel = [0]
ang_acc = [9.8*(math.pi/2-ang_pos[0])]
time = np.linspace(0,20,40000)
print_pendulum(time[0], ang_pos[0], ang_vel[0], ang_acc)

i = 1
while i < len(time):
    ang_pos_new, ang_vel_new, ang_acc_new = update_pendulum(ang_pos[i-1], ang_vel[i-1], ang_acc[i-1], time[i-1], time[i])
    ang_pos.append(ang_pos_new)
    ang_vel.append(ang_vel_new)
    ang_acc.append(ang_acc_new)
    i += 1


plt.figure(figsize = (4, 6))


plt.subplot(3,1,1)
plt.plot(time, ang_pos, 'y-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.xlim((0, 20)) 
plt.grid()


plt.subplot(3,1,2)
plt.plot(time, ang_vel, 'b-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')
plt.xlim((0, 20)) 
plt.grid()


plt.subplot(3,1,3)
plt.plot(time, ang_acc, 'g-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs Time')
plt.xlim((0, 20)) 
plt.grid()