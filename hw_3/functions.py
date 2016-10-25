# A file containing all functions that the driver file will call

import numpy as np
import numpy.linalg as lin
import numpy.fft as ft
import matplotlib.pyplot as plt
import math
from parameters import Bohr,me,charge,c

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
    force = Calculate_Force(charge,-charge,r)
    #print force
    accel = force / me
    #dv = accel * dt
    xpos = particle[0][0]
    ypos = particle[0][1]
    xaccel = accel * xpos/r
    yaccel = accel * ypos/r
    #print accel, xaccel,yaccel, xpos, ypos
    dvx = xaccel * dt
    dvy = yaccel * dt
    dx = dt * particle[1][0]
    dy = dt * particle[1][1]
    particle += np.array([[dx,dy],[dvx,dvy]])
    return particle,xaccel,yaccel

def FinalTime(vinit,distance):
    #distance = (end - start) * Bohr
    total_t = distance / vinit
    return total_t

def MakePlot(time,x,y,val,name):
    plt.plot(time,x,label='x ' + val)
    plt.plot(time,y,label='y ' + val)
    plt.xlabel('Time (s)')
    plt.ylabel(val + ' (cgs units)')
    plt.legend()
    plt.savefig(name+'.png')
    plt.clf()

def DipolePlot(time,dipole,name):
    plt.plot(time,dipole)
    plt.xlabel('Time (s)')
    plt.ylabel('Second derivative of dipole moment (statC cm s^-2)')
    plt.savefig(name+'.png')
    plt.clf()

def TrajectoryPlot(x,y,name):
    xarray = np.array(x) 
    yarray = np.array(y)
    xarray /= Bohr
    yarray /= Bohr
    plt.plot(xarray,yarray)
    plt.xlabel('x position (Bohr radii)')
    plt.ylabel('y position (Bohr radii)')
    plt.savefig(name+'.png')
    plt.clf()


def FT_Dipole(d,dt):
    dipole_list = np.array(d)
    dipole_w = ft.fft(dipole_list)
    dipole_w = dipole_w.real
    #time_array = np.array(time)
    n = dipole_w.size
    freq_array = ft.fftfreq(n,dt)
    return freq_array,dipole_w

def PowerSpectrum(wlist,dlist,name):
    power = dlist * dlist * wlist * wlist * wlist * wlist * 2.0 / (3.0 * c**3)
    pos_wlist = []
    pos_power = []
    for i in range(0,len(wlist)):
        if (wlist[i] > 0):
            pos_wlist.append(wlist[i])
            pos_power.append(power[i])
    print min(pos_power)
    plt.plot(pos_wlist,pos_power)
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Power (erg/s)')
    plt.savefig(name + '.png')
    plt.clf()
