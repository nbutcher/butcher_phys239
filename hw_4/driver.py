import numpy as np
import h5py 
from functions import *

f = h5py.File('SpecData.hdf5','r')

wave = f['Wavelength']
lum = f['Luminosity']

sconst = 2e8 #This reproduces 3e3 to long end of plot
p = 2 #should always be > 0
slist = SynchrotronSpectrum(sconst,p,wave)
#BasicSpecPlot(wave,slist)

#flist = FreeFreeSpectrum(T,ne,ni,Z,gff,wlist):
