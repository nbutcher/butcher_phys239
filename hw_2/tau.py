#This file will answer the questions in part a and give low, medium, and high cross sections to generate_ic.py
from constants import pc

def Column_Density(n,D):
    # Calculates column density in cm^-2 from number density n in 
    # cm^-3 and distance D in parsecs
    D_cm = D * pc
    c_den = D_cm * n
    return c_den

def Calculate_Sigma(D,n,tau):
    # Assuming distance D in parsecs and number density n in cm^-3, 
    # returns required cross section in cm^-2 for the input optical 
    # depth tau.
    D_cm = D * pc
    l_mfp = D / tau
    sigma = 1.0 / (n * l_mfp)
    return sigma

print Column_Density(1,100)
