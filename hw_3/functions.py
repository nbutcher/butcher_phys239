# A file containing all functions that the driver file will call

import numpy as np
import numpy.linalg as lin
import numpy.fft as ft
import matplotlib.pyplot as plt
import math
from parameters import Bohr,me,charge,c


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


def UpdateParticle(particle,dt):
    """Function that updates the particles position and velocity.
    Additionally returns the acceleration"""
    r = lin.norm(particle[0])
    force = Calculate_Force(charge,-charge,r)
    accel = force / me
    xpos = particle[0][0]
    ypos = particle[0][1]
    xaccel = accel * xpos/r
    yaccel = accel * ypos/r
    dvx = xaccel * dt
    dvy = yaccel * dt
    dx = dt * particle[1][0]
    dy = dt * particle[1][1]
    particle += np.array([[dx,dy],[dvx,dvy]])
    return particle,xaccel,yaccel

def FinalTime(vinit,distance):
    """Calculates final time based on distance to travel and initial
    velocity"""
    total_t = distance / vinit
    return total_t

def MakePlot(time,x,y,val,name):
    """Plot the x and y components of the input property as a 
    function of time"""
    plt.plot(time,x,label='x ' + val)
    plt.plot(time,y,label='y ' + val)
    plt.xlabel('Time (s)')
    plt.ylabel(val + ' (cgs units)')
    plt.legend()
    plt.savefig(name+'.png')
    plt.clf()

def DipolePlot(time,dipole,name):
    """Plot the second time derivative of the dipole moment as a 
    function of time"""
    plt.plot(time,dipole)
    plt.xlabel('Time (s)')
    plt.ylabel('Second derivative of dipole moment (statC cm s^-2)')
    plt.savefig(name+'.png')
    plt.clf()

def TrajectoryPlot(x,y,name):
    """Plot the trajectory of the particle"""
    xarray = np.array(x) 
    yarray = np.array(y)
    xarray /= Bohr
    yarray /= Bohr
    plt.plot(xarray,yarray)
    plt.xlabel('x position (Bohr radii)')
    plt.ylabel('y position (Bohr radii)')
    plt.savefig(name+'.png')
    plt.clf()

def DotProdAngle(a,b):
    val = a[0] * b[0] + a[1] * b[1]
    cos_theta = val / (lin.norm(a) * lin.norm(b))
    return cos_theta

def FT_Dipole(d_ddot,dt):
    """Perform a Fourier Transform to get the change in dipole 
    moment as a function of frequency"""

    dipole_ddot_list = np.array(d_ddot)
    n = dipole_ddot_list.size
    freq_array = ft.rfftfreq(n,dt)
    dipole_ddot_w = ft.rfft(dipole_ddot_list)
    dipole_ddot_w = np.sqrt(dipole_ddot_w * np.conj(dipole_ddot_w))
    return freq_array,dipole_ddot_w


def PowerSpectrum(wlist,dlist,name):
    """Plot the power spectrum as a function of frequency"""
    power = dlist * 2.0 / (3.0 * c**3)
    pos_wlist = []
    pos_power = []
    #for i in range(0,len(wlist)):
    #    if (wlist[i] > 0):
    #        pos_wlist.append(wlist[i])
    #        pos_power.append(power[i])
    #    else:
    #        pos_wlist.append(-wlist[i])
    #        pos_power.append(power[i])
    plt.scatter(np.log(wlist),np.log(power))
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Power (erg/s)')
    plt.savefig(name + '.png')
    plt.clf()
