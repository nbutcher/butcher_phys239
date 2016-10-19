# A file containing all functions that the driver file will call

import numpy as np
import numpy.linalg as lin
from constants import Bohr

def MaxTimeStep(v,MaxDistance):
    """Calculates a maximum timestep based on a pre-defined maximum
    allowed distance per timestep and the velocity"""
    t = MaxDistance / v
    return t

def Initialize(bi,vi,IC,Xstart):
    """Sets an array with starting position and velocity of the 
    particle as read from IC"""
    b = IC[0][bi]
    vx = IC[1][vi]
    particle = np.array([[Xstart,b],[vx,0]])
    return particle

def Calculate_Force(particle):
    """Calculates the force on the moving charge in ergs"""
    r = lin.norm(particle[0])
    r_cgs = r * Bohr
    F = pow(r_cgs,-2)
    return F

def Components(r):
    

def UpdateVel(particle,MaxDistance,vdiff):
    v = lin.norm(particle[1])
    r = lin.norm(particle[0])
    tmax = MaxTimeStep(v,MaxDistance)
    force = Calculate_Force(particle)
    #dv = force * dt
    dt = vdiff * v / force
    if (dt > tmax):
        dt = tmax
    dv = force * dt
    xpos = particle[0][0]
    ypos = particle[0][1]
    dvx = xpos/r
    dvy = ypos/r
    particle += np.array([[0,0],[dvx,dvy]])

    
