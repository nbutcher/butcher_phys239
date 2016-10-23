# A file containing all functions that the driver file will call

import numpy as np
import numpy.linalg as lin
import matplotlib.pyplot as plt
from parameters import Bohr,me,charge

def MaxTimeStep(v,MaxDistance):
    """Calculates a maximum timestep based on a pre-defined maximum
    allowed distance per timestep and the velocity"""
    v_bohr = v / Bohr #v in bohr radii per second
    t = MaxDistance / v_bohr
    return t

def Initialize(bi,vi,IC,Xstart):
    """Sets an array with starting position and velocity of the 
    particle as read from IC"""
    b = IC[0][bi] * Bohr
    start_cgs = Xstart * Bohr
    vx = IC[1][vi]
    particle = np.array([[start_cgs,b],[vx,0]])
    return particle

def Calculate_Force(q1,q2,r):
    """Calculates the force on the moving charge in ergs"""
    #r_cgs = r
    F = q1 * q2 * pow(r,-2)
    return F 


def UpdateParticle(particle,dt): #MaxDistance,vdiff):
#    v = lin.norm(particle[1])
    r = lin.norm(particle[0])
#    tmax = MaxTimeStep(v,MaxDistance)
    force = Calculate_Force(charge,-charge,r)
    accel = force / me
    #dv = accel * dt
    xpos = particle[0][0]
    ypos = particle[0][1]
    xaccel = accel * xpos/r
    yaccel = accel * ypos/r
    dvx = xaccel * dt
    dvy = yaccel * dt
    dx = dt * particle[1][0]
    dy = dt * particle[1][1]
    #if (abs(xpos < 0.5)):
    #    print 'accel: ', accel
    particle += np.array([[dx,dy],[dvx,dvy]])
    return particle,xaccel,yaccel

def FinalTime(vinit,distance):
    #distance = (end - start) * Bohr
    total_t = distance / vinit
    return total_t

def MakePlot(time,x,y,val,name):
    plt.plot(time,x,label='x ' + val)
    plt.plot(time,y,label='y ' + val)
    plt.legend()
    plt.savefig(name+'.png')

#def MainLoop():

    
