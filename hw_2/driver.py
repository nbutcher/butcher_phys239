#This will control the execution of everything once the IC's have been made.
from gas_properties import Calculate_Sigma, Column_Density, Gaussian_Sigma, New_I, Calculate_Tau
from parameters import *
from plotting_routines import Sigma_Plot, Intensity_Plot
import numpy as np
import h5py

col_den = Column_Density(n,Distance)
print "Column density in cm^-2 is: ", col_den

nu_list = np.ones(FreqBins)
for i in range(0,FreqBins):
    nu_list[i] *= (i+1)
sig_list = np.zeros(FreqBins)
for i in tau_check:
    sig = Calculate_Sigma(n,Distance,i)
    print "Cross Section for tau = ", i, " is ", sig, " cm^-2."
    for j in range(0,FreqBins):
        bin_sig = Gaussian_Sigma(j,Central_Freq,Std_Dev,sig)
        sig_list[j] = bin_sig
    Sigma_Plot(nu_list, sig_list, 'Part3_'+str(sig)+'.png')

g = h5py.File('InitialConditions.hdf5','r')
I_initial = np.array(g['I_0'])
I_transport = np.array(I_initial)
sigma_store = np.array(g['sig'])
S_store = np.array(g['S'])
tau_store = Calculate_Tau(n,Distance,sigma_store)
S_current = 0
ds = float(Distance) / (NumSteps)
while (S_current < Distance):
    I_transport = New_I(I_transport, S_store, tau_store, Distance, ds)
    #print I_transport[2][10], I_initial[2][10],S_store[10]
    S_current += ds

Intensity_Plot(nu_list,I_transport,I_initial,S_store,filenames)
