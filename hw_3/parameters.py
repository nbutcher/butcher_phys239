# Contains the user adjusted parameters for the test. Defines ICs

import numpy as np

# With the atomic number Z of the ion unspecified the distances
# will be scaled by a factor of sqrt(Z)

Bohr = 5.3e-9 #Bohr radius in cm
me = 9.11e-28 #mass of electron in g
charge = 4.803e-10 #charge of electron cgs
blist = []
for i in range(1,6):
    blist.append(i*2) 

vlist = []
for i in range(1,6):
    vlist.append(i * 0.5 * 1e7) #1e7 cm/s

IC = np.array([blist,vlist])

xStart = -200 #starting x position in Bohur radius / z
MaxDistance = 1 #maximum distance charge can move in one timestep
TotalDistance = 400 #distance to travel in units of Bohr radius / Z
vdiff = 0.05
dt = 0.01 * Bohr / 1e7 #
