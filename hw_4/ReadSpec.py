import numpy as np
import h5py

def dat_to_hdf5(infile, outfile):
    '''Reads the datafile and converts it into an hdf5 file for ease
    of working with'''

    hf = h5py.File(outfile,'w')
    f = open(infile,'r')
    
    skipfirst = 1
    wavelength = []
    lum = []
    dlum = []
    for line in f:
        if (skipfirst):
            skipfirst = 0
            continue
        temp = ''
        for i in range(6,15):
            temp += line[i]
        ftemp = float(temp)
        wavelength.append(ftemp)
        temp = ''
        for i in range(21,30):
            temp += line[i]
        ftemp = float(temp)
        lum.append(ftemp)
        temp = ''
        for i in range(36,45):
            temp += line[i]
        ftemp = float(temp)
        dlum.append(ftemp)

    wl = hf.create_dataset("Wavelength",data=wavelength)
    l = hf.create_dataset("Luminosity",data=lum)
    dl = hf.create_dataset("Sigma",data=lum)
    f.close()
    hf.close()

dat_to_hdf5('m82spec.dat','SpecData.hdf5')
