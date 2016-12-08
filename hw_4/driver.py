#This file is run after the stellar and dust model hdf5 input files have
#been created.

import numpy as np
import h5py 
from functions import *
from parameters import Tdust, Tgas

f = h5py.File('SpecData.hdf5','r')

wave = np.array(f['Wavelength'])
lum = np.array(f['Luminosity'])
#BasicSpecPlot(wave,lum)

stars = h5py.File('Z040_Single_Salpeter_Nebular.hdf5') 
starwave = np.array(stars['Wavelength'])
starlum = np.array(stars['Luminosity'])
massfrac = 2e-2
stararray = np.array(starlum) * massfrac
starwave1 = []
starlum1 = []
contrib = np.where( starwave>2e-1 )
for j in contrib[0]:
    starwave1.append(starwave[j])
    starlum1.append(stararray[j])

starwave1arr = np.array(starwave1)
starwave2 = []
starlum2 = []
contrib = np.where( starwave1arr<3e0 )
for j in contrib[0]:
    starwave2.append(starwave1[j])
    starlum2.append(starlum1[j])

#BasicSpecPlot(starwave2,starlum2)

dustfile = 'silicate.hdf5'
index = 0 
dwave, size, qlist = Dust_File(dustfile,index)
V = 5e60
dlist = Dust_Spectrum(V,Distance,Tdust,size,dwave,qlist)
maxd = max(dlist)
darray = np.array(dlist)
contrib = np.where( darray > 0.0001*maxd )
dwave1 = []
dlist1 = []
for j in contrib[0]:
    dwave1.append(dwave[j])
    dlist1.append(darray[j])
#BasicSpecPlot(dwave1,dlist1)

sconst = 5e12 
p = 2.0 #should always be > 0
slist = Synchrotron_Spectrum(sconst,p,wave)
sarray = np.array(slist)
contrib = np.where( sarray > 1e-7 )
swave1 = []
slist1 = []
for j in contrib[0]:
    swave1.append(wave[j])
    slist1.append(sarray[j])
#BasicSpecPlot(wave,slist)

factor = 1e-2
flist = FreeFree_Spectrum(wave, factor, Tgas)
farray = np.array(flist)
contrib = np.where( wave < 1e2 )
fwave1 = []
flist1 = []
for j in contrib[0]:
    fwave1.append(wave[j])
    flist1.append(farray[j])

#BasicSpecPlot(wave,flist)

OverlaySpecPlot(dwave1,dlist1,'Dust',swave1,slist1,'Synch',fwave1,flist1,'Free-free',starwave2,starlum2,'Starlight',wave,lum)
