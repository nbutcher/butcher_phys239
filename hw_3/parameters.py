# Contains the user adjusted parameters for the test. Defines ICs

import numpy as np

# With the atomic number Z of the ion unspecified the distances
# will be scaled by a factor of sqrt(Z)

blist = []
for i in range(1,6):
    blist.append(i*2) 

vlist = []
for i in range(1,6):
    vlist.append(i * 0.5 * 1e7) #1e7 cm/s

IC = np.array([blist,vlist])

xStart = -200 #starting x position
MaxDistance = 1 #maximum distance charge can move in one timestep


