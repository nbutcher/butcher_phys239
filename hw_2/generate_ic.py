# This file generates an HDF5 file with the cross section, initial 
# intensity, and source function for each test case
import h5py
import numpy as np
from parameters import *
from gas_properties import Gaussian_Sigma,Calculate_Sigma

f = h5py.File('InitialConditions.hdf5','w')



source = np.ones([NumCases,FreqBins]) * S_nu
S_list = f.create_dataset('S', data=source)

sigma = np.ones([NumCases,FreqBins])
I_vals = np.ones([NumCases,FreqBins])
sigma_max = np.ones(NumCases)
for i in range(0,NumCases):
    sigma_max[i] *= Calculate_Sigma(n,Distance,Cases[i][1])
for i in range(0,NumCases):
    I_vals[i] *= Cases[i][0]
    if (Cases[i][2]):
        for j in range(0,FreqBins):
            sigma[i][j] = Gaussian_Sigma(j,Central_Freq,Std_Dev,sigma_max[i])
    else:
        sigma[i] *= sigma_max[i]

I_list = f.create_dataset('I_0', data=I_vals)
sigma_list = f.create_dataset('sig',data=sigma)

f.close()

