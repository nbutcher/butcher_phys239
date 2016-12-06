import numpy as np
import h5py 
from functions import *

f = h5py.File('SpecData.hdf5','r')

wave = np.array(f['Wavelength'])
lum = np.array(f['Luminosity'])


stars = h5py.File('Z020_Single.hdf5')
starwave = np.array(stars['Wavelength'])
starlum = np.array(stars['Luminosity'])
slumlist = Stellar_Spectrum(wave,starwave,starlum)
BasicSpecPlot(wave,slumlist)

sconst = 2e8 #This reproduces 3e3 to long end of plot
p = 2 #should always be > 0
slist = Synchrotron_Spectrum(sconst,p,wave)
#BasicSpecPlot(wave,slist)
#flist = FreeFree_Spectrum(T,ne,ni,Z,gff,wlist):
