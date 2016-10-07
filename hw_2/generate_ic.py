import h5py
import numpy as np
from parameters import *
from gas_properties import Gaussian_Sigma

f = h5py.File('InitialConditions.hdf5',w)

I_list = f.create_group('I0')


source = np.ones(FreqBins) * S_nu
S_list = f.create_dataset('S', source)

sigma = np.ones([NumCases,FreqBins])
I_vals = np.ones([NumCases,FreqBins])
for i in range(0,NumCases):
    I_vals[i] *= Cases[i][0]
    if (Cases[i][2]):
        for j in range(0,Freq_Bins):
            sigma[i][j] = Gaussian_Sigma(j,Central_Freq,Std_Dev,Cases[i][1])
    else:
        sigma[i] *= Cases[i][1]

I_list = f.create_dataset('I_0', I_vals)
sigma_list = f.create_dataset('sig')


