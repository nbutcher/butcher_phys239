import numpy as np
import h5py 
from functions import *
from parameters import Tdust, Tgas

f = h5py.File('SpecData.hdf5','r')

wave = np.array(f['Wavelength'])
lum = np.array(f['Luminosity'])
#BasicSpecPlot(wave,lum)

#stars = h5py.File('temp_star') #'Z020_Single.hdf5')
#starwave = np.array(stars['Wavelength'])
#starlum = np.array(stars['Luminosity'])
#slumlist = Stellar_Spectrum(wave,starwave,starlum)
#BasicSpecPlot(wave,slumlist)

'''
dustfile = 'graphite.hdf5'
#for i in range(0,81):
index = 0
dwave, size, qlist = Dust_File(dustfile,index)
V = 1
dlist = Dust_Spectrum(V,Distance,Tdust,size,dwave,qlist)
maxd = max(dlist)
darray = np.array(dlist)
contrib = np.where( darray > 0.0001*maxd )
dwave1 = []
dlist1 = []
for j in contrib[0]:
    dwave1.append(dwave[j])
    dlist1.append(darray[j])
BasicSpecPlot(dwave1,dlist1)
'''

sconst = 2e8 #This reproduces 3e3 to long end of plot
p = 2 #should always be > 0
slist = Synchrotron_Spectrum(sconst,p,wave)
#BasicSpecPlot(wave,slist)

factor = 1.0/3.0
flist = FreeFree_Spectrum(wave, factor, Tgas)
#print flist[0], flist[-1]
BasicSpecPlot(wave,flist)
