import numpy as np
import h5py 
from functions import *

f = h5py.File('SpecData.hdf5','r')

wave = f['Wavelength']
lum = f['Luminosity']

sconst = 1
p = 2 #should always be > 0
slist = SynchrotronSpectrum(sconst,p,wave)
BasicSpecPlot(wave,slist)
