import h5py
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

def ThreeSpecPlot(w1,l1,label1,w2,l2,label2,w3,l3,label3):
    plt.loglog(w1,l1,label=label1)
    plt.loglog(w2,l2,label=label2)
    plt.loglog(w3,l3,label=label3)
    plt.legend()
    plt.show()

def microns_to_hz(wl):
    wl_in_cm = wl * 1e-4 #convert from microns to cm
    return c / wl_in_cm

def SynchrotronMain(const,p,wl):
    f1 = (np.sqrt(3.) * qe**3 * const) / (2. * np.pi * me * c**2 * (p + 1.))
    g1 = gamma(p/4. + 19./12.)
    g2 = gamma(p/4. - 1./12.)
    freq = microns_to_hz(wl)
    f2 = ((me * c * 2 * np.pi * freq) / (3 * qe * const))**(-(p-1)/2)
    return f1 * g1 * g2 * f2

def Synchrotron_Spectrum(const,p,wlist):
    
    slist = []
    for wl in wlist:
        val = SynchrotronMain(const,p,wl)
        slist.append(val)

    return slist

def FreeFree(wl, factor, T): #(T,wl,ne,ni,Z,gff):
    ''' Returns free-free emission per volume per time per hertz'''
    freq = microns_to_hz(wl)
#    print freq, h * freq / (kB * T), math.exp(-h * freq / (kB * T))
    #val = 6.8e-38 * Z**2 * ne * ni * T**(-0.5) * math.exp(-h * freq / (kB * T))
    val = factor * T**(-0.5) * math.exp(-h * freq / (kB * T))
    return val

def FreeFree_Spectrum(wlist, factor, T): #(T,ne,ni,Z,gff,wlist):
    flist = []
    for wl in wlist:
        val = FreeFree(wl, factor, T) #(T,wl,ne,ni,Z,gff)
        flist.append(val)
    return flist

def Planck_Law(wl, T):
    f = microns_to_hz(wl)
    f1 = 2.*h*f**3 / c**2 
    try:
        f2 = 1. / math.expm1(h*f / (kB * T))
    except OverflowError:
        f2 = 0
    #print math.exp(h*f / (kB * T)), math.expm1(h*f / (kB * T)), f
    #print wl, h*f, kB * T
    #print wl, f, h * f, kB * T
    return f1 * f2

def Read_Table(wl, wlist, qlist, order):
    '''order == 1 has wavelength descending, order == 0 has wavelength
    ascending in the list'''
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
    Q = Read_Table(wl, wlist, qlist, 1)
    return 3. * Q / (4. * a)

def Dust_Emission(V,D,kappa,T,wl):
    B = Planck_Law(wl, T)
    #print B, kappa, wl
    return V * kappa * B / D**2

'''def Dust_Spectrum(V,D,T,a,wlist,wlist_q,qlist):
    dustlist = []
    for wl in wlist:
        k = Get_Kappa(a, wl, wlist_q, qlist)
        val = Dust_Emission(V,D,k,T,wl)
        dustlist.append(val)
    return dustlist'''

def Dust_Spectrum(V,D,T,a,wlist,qlist):
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
    lum = Read_Table(wl, wltable, lumlist, 0)
    return lum

def Stellar_Spectrum(wllist, wltable, lumlist):
    vallist = []
    for wl in wllist:
        lum = Stellar_Luminosity(wl,wltable,lumlist)
        vallist.append(lum)
    return vallist
