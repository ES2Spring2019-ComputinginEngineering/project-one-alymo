#project1: microbit pendulum by Mo and Alyssa

print("Part I: Simulation")

import numpy

def update_pendulum(acc,pos,vel,time1,time2):
    dt = time2-time1
    posNext = pos+vel*dt+1/2*acc*dt
    velNext = vel+acc*dt
    return posNext,velNext

def print_pendulum(time,pos,vel):
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel, "\n")

pos = [0]
vel = [0]
acc = [0,1,2,3,4,4,2,2,1,0,0,0,0,-1,-1,-2,-2,-2,-3,-4,-4]
time = numpy.linspace(0,20,21)
print_pendulum(time[0],pos[0],vel[0])

i = 1
while i < len(time):
    posNext, velNext = update_system(acc[i],pos[i-1],vel[i-1],time[i-1],time[i])
    pos.append(posNext)
    vel.append(velNext)
    print_system(time[i],pos[i],vel[i])
    i += 1