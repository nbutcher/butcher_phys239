import numpy as np
import h5py 
from functions import *

f = h5py.File('SpecData.hdf5','r')

wave = f['Wavelength']
lum = f['Luminosity']

BasicSpecPlot(wave,lum)
