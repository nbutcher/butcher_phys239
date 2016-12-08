#Functions used to generate the plots from the given datasets and
#equations describing luminosity

import h5py
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.special import gamma
from parameters import *

def BasicSpecPlot(wl,lum):
    '''Generates a plot of luminosity density vs. wavelength'''
    plt.loglog(wl,lum)
    plt.xlabel('Wavelength (microns)')
    plt.ylabel('Luminosity (L_sun / Hz)')
    plt.show()

def OverlaySpecPlot(w1,l1,label1,w2,l2,label2,w3,l3,label3,w4,l4,label4,givenwl,givenlum):
    '''Plots all four components against the given spectrum'''
    plt.loglog(w1,l1,label=label1)
    plt.loglog(w2,l2,label=label2)
    plt.loglog(w3,l3,label=label3)
    plt.loglog(w4,l4,label=label4)
    plt.loglog(givenwl,givenlum,label='Given')
    plt.legend()
    plt.show()


def microns_to_hz(wl):
    '''Converts a wavelength to microns to frequency in hertz'''
    wl_in_cm = wl * 1e-4 #convert from microns to cm
    return c / wl_in_cm

def SynchrotronMain(const,p,wl):
    '''Calculates synchrotron emission for a single wavelength'''
    f1 = (np.sqrt(3.) * qe**3 * const) / (2. * np.pi * me * c**2 * (p + 1.))
    g1 = gamma(p/4. + 19./12.)
    g2 = gamma(p/4. - 1./12.)
    freq = microns_to_hz(wl)
    f2 = ((me * c * 2 * np.pi * freq) / (3 * qe * const))**(-(p-1)/2)
    return f1 * g1 * g2 * f2

def Synchrotron_Spectrum(const,p,wlist):
    '''Calculates synchrotron emission for a list of wavelengths'''
    slist = []
    for wl in wlist:
        val = SynchrotronMain(const,p,wl)
        slist.append(val)

    return slist

def FreeFree(wl, factor, T): #(T,wl,ne,ni,Z,gff):
    ''' Returns free-free emission per volume per time per hertz'''
    freq = microns_to_hz(wl)
    val = factor * T**(-0.5) * math.exp(-h * freq / (kB * T))
    return val

def FreeFree_Spectrum(wlist, factor, T): #(T,ne,ni,Z,gff,wlist):
    '''Calculates free-free emission for a list of wavelengths'''
    flist = []
    for wl in wlist:
        val = FreeFree(wl, factor, T) #(T,wl,ne,ni,Z,gff)
        flist.append(val)
    return flist

def Planck_Law(wl, T):
    '''Calculates Planck's law for frequency'''
    f = microns_to_hz(wl)
    f1 = 2.*h*f**3 / c**2 
    #The exponent below can overflow within the asked for spectral 
    #range. When this happens the luminosity is negligible.
    try:
        f2 = 1. / math.expm1(h*f / (kB * T))
    except OverflowError: 
        f2 = 0
    return f1 * f2

def Read_Table(wl, wlist, qlist, order):
    '''order == 1 has wavelength descending, order == 0 has wavelength
    ascending in the list. Currently not used but left in case it is 
    needed again'''
    if (order == 1):
        for i in range(0,wlist.shape[0]):
            if (wlist[i] < wl):
                diff = wlist[i-1] - wlist[i]
                split = wl - wlist[i]
                frac = split / diff
                Qdiff = qlist[i-1] - qlist[i]
                Qval = qlist[i] + frac * Qdiff
                return Qval
    else:
        for i in range(0,wlist.shape[0]):
            if (wlist[i] > wl):
                diff = wlist[i] - wlist[i-1]
                split = wl - wlist[i-1]
                frac = split / diff
                Qdiff = qlist[i] - qlist[i-1]
                Qval = qlist[i-1] + frac * Qdiff
                return Qval


def Dust_File(infile,index):
    '''Opens a file containing dust data from provided Draine site'''
    f = h5py.File(infile,'r')
    if (index < 10):
        indexstr = 'Grain0' + str(index)
    else:
        indexstr = 'Grain' + str(index)
    grain = f[indexstr]
    wlist = np.array(grain['Wavelength'])
    size = np.array(grain['Size'])
    qlist = np.array(grain['Q'])
    return wlist, size[0], qlist

def Get_Kappa(a, wl, wlist, qlist):
    '''Calculates absorption opacity from table, not used'''
    Q = Read_Table(wl, wlist, qlist, 1)
    return 3. * Q / (4. * a)

def Dust_Emission(V,D,kappa,T,wl):
    '''Dust emission at the input wavelength'''
    B = Planck_Law(wl, T)
    return V * kappa * B / D**2


def Dust_Spectrum(V,D,T,a,wlist,qlist):
    '''Calculates dust emission for all values from the Draine
    dataset'''
    dustlist = []
    for i in range(0,wlist.shape[0]):
        Q = qlist[i]
        kappa = 3. * Q / (4. * a)
        wl = wlist[i]
        val = Dust_Emission(V,D,kappa,T,wl)
        #B = Planck_Law(wl,T)
        dustlist.append(val)
    return dustlist


def Stellar_Luminosity(wl, wltable, lumlist):
    '''Not used, reads stellar luminosity from table'''
    lum = Read_Table(wl, wltable, lumlist, 0)
    return lum

def Stellar_Spectrum(wllist, wltable, lumlist):
    '''Writes the stellar spectra from the Starburst99 dataset'''
    vallist = []
    for wl in wllist:
        lum = Stellar_Luminosity(wl,wltable,lumlist)
        vallist.append(lum)
    return vallist
