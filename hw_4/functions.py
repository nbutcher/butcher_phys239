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
    ''' Returns free-free emission per volume per time per hertz'''
    freq = microns_to_hz(wl)
    val = 6.8e-38 * Z**2 * ne * ni * T**(-0.5) * math.exp(-h * freq / (kB * T))
    return val

def FreeFreeSpectrum(T,ne,ni,Z,gff,wlist):
    flist = []
    for wl in wlist:
        val = FreeFree(T,wl,ne,ni,Z,gff)
        flist.append(val)
    return flist

def Planck_Law(wl, T):
    f1 = 2.*h*c**2 / wl**5
    f2 = 1. / (math.exp(h*c / (wl * kB * T)) - 1)
    return f1 * f2

def Read_Dust_Table(wl, wlist, qlist):
    for i in range(0,wlist.shape[0]):
        if (wlist[i] < wl):
            diff = wlist[i-1] - wlist[i]
            split = wl - wlist[i]
            frac = split / diff
            Qdiff = qlist[i-1] - qlist[i]
            Qval = qlist[i] + frac * Qdiff
            return Qval

def Dust_File(infile,index):
    f = h5py.File(infile,'r')
    if (index < 10):
        indexstr = 'Grain0' + str(index)
    else:
        indexstr = 'Grain' + str(index)
    grain = f[indexstr]
    wlist = np.array(grain['Wavelength'])
    size = np.array(grain['Size'])
    qlist = np.array(grain['Q'])
    return wlist, size, qlist

def Get_Kappa(a, wl, wlist, qlist):
    Q = Read_Dust_Table(wl, wlist, qlist)
    return 3. * Q / (4. * a)

def Dust_Emission(V,D,kappa,T,wl):
    B = Planck_Law(wl, T)
    return V * kappa * B / D**2

def Dust_Spectrum(V,D,kappa,T,a,wlist,wlist_q,qlist):
    dustlist = []
    for wl in wlist:
        k = Get_Kappa(a, wl, wlist_q, qlist)
        val = Dust_Emission(V,D,k,T,wl)
        dustlist.append(val)
    return dustlist
