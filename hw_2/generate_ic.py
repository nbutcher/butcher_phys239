import h5py
import numpy as np
import parameters


f = h5py.File('InitialConditions.hdf5',w)

I_list = f.create_group('I0')

sigma = np.ones([6,FreqBins])
sigma_list = f.create_dataset('sig')

source = np.ones(FreqBins) * S_nu
S_list = f.create_dataset('S', source)

I_vals = np.ones([NumCases,FreqBins])
for i in range(0,NumCases):
    I_vals[i] *= Cases[i][0]

I_list = f.create_dataset('I_0', I_vals)

