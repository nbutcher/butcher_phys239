# This is the file to run to complete the assignment.

import math
from parameters import *
from functions import *

# Initial Sample Output

cPart = Initialize(0,0,IC,xStart)
xlist = []
ylist = []
vxlist = []
vylist = []
axlist = []
aylist = []
timelist = []
dipole_list = []
dipole_dot_list = []
dipole_ddot_list = []
dipole_ddot2_list = []
t = 0
final_t = FinalTime(cPart[1][0],TotalDistance)
while (t < final_t):
    cPart,xaccel,yaccel = UpdateParticle(cPart,dt) 
    xlist.append(cPart[0][0])
    ylist.append(cPart[0][1])
    vxlist.append(cPart[1][0])
    vylist.append(cPart[1][1])
    axlist.append(xaccel)
    aylist.append(yaccel)
    #Here we use the fact that the acceleration is radial
    dipole_ddot = -charge * math.sqrt(xaccel**2 + yaccel**2)
    dipole_ddot2 = charge**2 * (xaccel**2 + yaccel**2)
    dipole_ddot_list.append(dipole_ddot)
    dipole_ddot2_list.append(dipole_ddot2)
#    dipole_list.append(charge * math.sqrt(cPart[0][0]**2 + cPart[0][1]**2))
#    dipole_dot_list.append(-charge * math.sqrt(cPart[1][0]**2 + cPart[1][1]**2))
    timelist.append(t)
    t += dt
MakePlot(timelist,vxlist,vylist,'Velocity','Velocity'+str(0)+str(0))
MakePlot(timelist,axlist,aylist,'Acceleration','Acceleration'+str(0)+str(0))
TrajectoryPlot(xlist,ylist,'Position00')
DipolePlot(timelist,dipole_ddot_list,'Dipole_Change00')
wlist, dipole_w = FT_Dipole(dipole_ddot2_list,dt)
PowerSpectrum(wlist,dipole_w,'PowerSpectrum00')


for i in range(0,len(IC[0])):
    for j in range(0,len(IC[1])):
        cPart = Initialize(i,j,IC,xStart)
        dipole_list = []
        timelist = []
        t = 0
        final_t = FinalTime(cPart[1][0],TotalDistance)
        while (t < final_t):
            cPart,xaccel,yaccel = UpdateParticle(cPart,dt)
            #Here we use the fact that the acceleration is radial
            dipole_change2 = charge**2 * (xaccel**2 + yaccel**2)
            dipole_list.append(dipole_change2)
            timelist.append(t)
            t += dt
        wlist, dipole_w = FT_Dipole(dipole_list,dt)
        PowerSpectrum(wlist,dipole_w,'PowerSpectrum' + str(i) + str(j))
        #The above plots are indexed by i and j with what iteration
        #of the loops we are in.
        print "Done with ", i, ' ', j

