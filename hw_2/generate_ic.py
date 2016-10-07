import h5py
import numpy as np

Distance = 100 #in parsec
NumSteps = 1000000 #number of steps to take through the simulation
FreqBins = 1000 #number of divisions in the frequency range

S_init = 1
I_high = 2
I_low = 0.5

f = h5py.File('InitialConditions.hdf5',w)

I_list = f.create_group('I0')

sigma = np.ones([6,FreqBins])
sigma_list = f.create_dataset('sig')

source = np.ones(FreqBins) * S_init
S_list = f.create_dataset('S', source)


