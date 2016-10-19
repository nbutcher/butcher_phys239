# Contains the user adjusted parameters for the test. Defines ICs

import numpy as np

blist = []
for i in range(1,6):
    blist.append(i*2) #units are in Bohr radius

vlist = []
for i in range(1,6):
    vlist.append(i * 0.5 * 1e7) #1e7 cm/s

IC = np.array([blist,vlist])

xStart = 200 #starting x in Bohr radii
MaxDistance = 1 #maximum distance charge can move in one timestep

