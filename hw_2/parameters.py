# This file contains all the parameters that the user may want to change

n = 1.0 # Number density in cm^-3
Distance = 100 # Distance through medium in parsecs
NumSteps = 1000000 # Number of steps to take to travel Distance
FreqBins = 1000 # Number of bins for frequency
FWHM = 400 # Number of bins the full-width half-max

# These are the tau values to output the cross section for in part 1.
tau_check1 = 1e-3
tau_check2 = 1.0
tau_check3 = 1e3

# Values for tau < 1, tau > 1, and tau >> 1
tau_XL = 1e3
tau_L = 5
tau_S = 0.5

# S (source function) and I_0 for I_0>S and I_0<S 
S = 1.0
I_small = 0.5 * S
I_large = 2.0 * S

# Case list as a tuple with I0, tau0 (on line center), 
# tau (off of line center)
Cases = [(0, tau_XL, tau_XL), (0, tau_S, tau_S), (I_small, tau_S, tau_S), 
        (I_large, tau_S, tau_S), (I_small, tau_L, tau_S), (I_large, tau_L, tau_S)]
