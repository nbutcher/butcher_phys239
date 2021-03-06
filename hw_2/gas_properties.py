#This file contains functions to be called by generate_ic.py and driver.py
import math
from constants import pc

def Column_Density(n,D):
    # Calculates column density in cm^-2 from number density n in 
    # cm^-3 and distance D in parsecs
    D_cm = D * pc
    c_den = D_cm * n
    return c_den

def Calculate_Sigma(n,D,tau):
    # Assuming distance D in parsecs and number density n in cm^-3, 
    # returns required cross section in cm^-2 for the input optical 
    # depth tau
    col_den = Column_Density(n,D)
    sigma = 1.0 / (col_den / tau)
    return sigma


def Gaussian_Sigma(freqbin,center,width,sigma_max):
    # Accepts the frequency bin, central bin, standard deviation
    # (width), and sigma at the center. Returns the cross section
    # for that bin.
    sig = sigma_max * math.exp(-float(freqbin-center)**2 / float(2*width**2))
    return sig

def Calculate_Tau(n,D,sigma):
    col_den = Column_Density(n,D)
    tau = col_den * sigma
    return tau

def New_I(I,S,d_tau,D):#,ds):
    #d_tau = (ds / D) * tau
    I_new = I - d_tau * I + d_tau * S
    return I_new

