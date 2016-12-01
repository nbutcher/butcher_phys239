import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.special import gamma
from parameters import *

def BasicSpecPlot(wl,lum):
    plt.loglog(wl,lum)
    plt.xlabel('Wavelength (microns)')
    plt.ylabel('Luminosity (L_sun / Hz)')
    plt.show()

def microns_to_hz(wl):
    wl_in_cm = wl * 1e-4 #convert from microns to cm
    return c / wl

def SynchrotronMain(const,p,wl):
    f1 = (np.sqrt(3.) * qe**3 * const) / (2. * np.pi * me * c**2 * (p + 1.))
    g1 = gamma(p/4. + 19./12.)
    g2 = gamma(p/4. - 1./12.)
    freq = microns_to_hz(wl)
    f2 = ((me * c * 2 * np.pi * freq) / (3 * qe * const))**(-(p-1)/2)
    return f1 * g1 * g2 * f2

def SynchrotronSpectrum(const,p,wlist):
    
    slist = []
    for wl in wlist:
        val = SynchrotronMain(const,p,wl)
        slist.append(val)

    return slist

def FreeFree(T,wl,ne,ni,Z,gff):
    freq = microns_to_hz(wl)
    val = 6.8e-38 * Z**2 * ne * ni * T**(-0.5) * math.exp(-h * freq / (kB * T))

