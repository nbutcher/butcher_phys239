# A file containing all functions that the driver file will call

import numpy as np
import numpy.linalg as lin
from parameters import Bohr

def MaxTimeStep(v,MaxDistance):
    """Calculates a maximum timestep based on a pre-defined maximum
    allowed distance per timestep and the velocity"""
    v_bohr = v / Bohr #v in bohr radii per second
    t = MaxDistance / v_bohr
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
    dvx = dv * xpos/r
    dvy = dv * ypos/r
    particle += np.array([[0,0],[dvx,dvy]])
    return dt

def UpdatePos(particle,dt):
    vx_bohr = particle[1][0] / Bohr
    vy_bohr = particle[1][1] / Bohr
    drx = vx_bohr * dt
    dry = vy_bohr * dt
    particle += np.array([drx,dry],[0,0])
