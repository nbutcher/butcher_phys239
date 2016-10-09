#This will control the execution of everything once the IC's have been made.
from gas_properties import Calculate_Sigma, Column_Density, Gaussian_Sigma
from parameters import *
from plotting_routines import Sigma_Plot
import numpy as np


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

