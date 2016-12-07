import numpy as np
import h5py 
from functions import *

f = h5py.File('SpecData.hdf5','r')

wave = np.array(f['Wavelength'])
lum = np.array(f['Luminosity'])
T = 1e6

#stars = h5py.File('temp_star') #'Z020_Single.hdf5')
#starwave = np.array(stars['Wavelength'])
#starlum = np.array(stars['Luminosity'])
#slumlist = Stellar_Spectrum(wave,starwave,starlum)
#BasicSpecPlot(wave,slumlist)

dustfile = 'silicate.hdf5'
for i in range(0,81):
    dwave, size, qlist = Dust_File(dustfile,i)
    V = 1
    dlist = Dust_Spectrum(V,Distance,T,size,wave,dwave,qlist)
    BasicSpecPlot(wave,dlist)

sconst = 2e8 #This reproduces 3e3 to long end of plot
p = 2 #should always be > 0
slist = Synchrotron_Spectrum(sconst,p,wave)
#BasicSpecPlot(wave,slist)
factor = 1

flist = FreeFree_Spectrum(wave, factor, T)
#print flist[0], flist[-1]
#BasicSpecPlot(wave,flist)
