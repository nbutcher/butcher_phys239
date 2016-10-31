# Contains the user adjusted parameters for the test. Defines ICs

import numpy as np

# With the atomic number Z of the ion unspecified the distances
# will be scaled by a factor of sqrt(Z)

Bohr = 5.3e-9 #Bohr radius in cm
me = 9.11e-28 #mass of electron in g
charge = 4.803e-10 #charge of electron cgs
c = 29979245800 #speed of light in cm/s
blist = []
for i in range(1,6):
    blist.append(i*5e3) #impact parameter in units of Bohr radius

vlist = []
for i in range(1,6):
    vlist.append(i * 1e7) #1e7 cm/s

IC = np.array([blist,vlist])

xStart = -5e5 #starting x position in Bohr radius / z
TotalDistance = 1e6 * Bohr #distance to travel in cm
dt = 1e3 * Bohr / 1e7 #defines the timestep
