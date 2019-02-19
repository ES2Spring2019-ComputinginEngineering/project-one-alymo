#project1: microbit pendulum by Mo and Alyssa

print("Part I: Simulation")

import numpy

def update_pendulum(ang_pos, ang_vel, ang_acc, atime1,time2):
    dt = time2-time1
    ang_vel_new = ang_vel+ang_acc*dt
    ang_pos_new = ang_pos+ang_vel*dt
    ang_acc_new = 9.8*(pi/2-ang_pos_new)
    return ang_pos_new, ang_vel_new, ang_acc_new

def print_pendulum(time,pos,vel):
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel, "\n")

pos = [0]
vel = [0]
ang_acc = 9.8*(pi/2-ang_pos)
time = numpy.linspace(0,20,201)
print_pendulum(time[0],pos[0],vel[0])

i = 1
while i < len(time):
    posNext, velNext = update_pendulum(acc[i],pos[i-1],vel[i-1],time[i-1],time[i])
    pos.append(posNext)
    vel.append(velNext)
    print_pendulum(time[i],pos[i],vel[i])
    i += 1