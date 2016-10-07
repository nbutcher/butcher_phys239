#This will control the execution of everything once the IC's have been made.
from gas_properties import Calculate_Sigma, Column_Density
from parameters import *

col_den = Column_Density(n,Distance)
print "Column density in cm^-2 is: ", col_den

for i in tau_check:
    sig = Calculate_Sigma(n,Distance,i)
    print "Cross Section for tau = ", i, " is ", sig, " cm^-2."
