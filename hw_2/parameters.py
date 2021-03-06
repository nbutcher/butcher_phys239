# This file contains all the parameters that the user may want to change

n = 1.0 # Number density in cm^-3
Distance = 100 # Distance through medium in parsecs
NumSteps = 1000000 # Number of steps to take to travel Distance
FreqBins = 1001 # Number of bins for frequency
Central_Freq = FreqBins/2 # Center bin for odd FreqBins
Std_Dev = 100 # The standard deviation in number of bins

# These are the tau values to output the cross section for in part 1.
tau_check = [1e-3, 1.0, 1e3]
#tau_check1 = 1e-3
#tau_check2 = 1.0
#tau_check3 = 1e3

# Values for tau < 1, tau > 1, and tau >> 1
tau_XL = 1e3
tau_L = 5
tau_S = 0.5

# S (source function) and I_0 for I_0>S and I_0<S 
S_nu = 3.0
I_small = 1.0 #0.5 * S_nu
I_large = 5.0 #2.0 * S_nu

# Case list as a tuple with I0, tau0 (on line center), 
# and 0 for flat sigma or 1 for Gaussian
Cases = [(0, tau_XL, 0), (0, tau_S, 1), (I_small, tau_S, 1), 
        (I_large, tau_S, 1), (I_small, tau_L, 1), (I_large, tau_L, 1)]
NumCases = len(Cases)

filenames = ['Intensity_A','Intensity_B','Intensity_C','Intensity_D','Intensity_E','Intensity_F']
