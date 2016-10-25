import math
from parameters import *
from functions import *

# Initial Sample Output

cPart = Initialize(0,0,IC,xStart)
print 'Begin'
print cPart[0], cPart[1]
xlist = []
ylist = []
vxlist = []
vylist = []
axlist = []
aylist = []
timelist = []
dipole_list = []
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
    #Here we assume all acceleration is radial, should hold
    dipole_change = -charge * math.sqrt(xaccel**2 + yaccel**2)
    dipole_list.append(dipole_change)
    timelist.append(t)
    #if (cPart[0][1] < 0):
    #    break
    t += dt
print 'Final'
print cPart[0], cPart[1]
MakePlot(timelist,vxlist,vylist,'Velocity','Velocity'+str(0)+str(0))
MakePlot(timelist,axlist,aylist,'Acceleration','Acceleration'+str(0)+str(0))
TrajectoryPlot(xlist,ylist,'Position00')
DipolePlot(timelist,dipole_list,'Dipole_Change00')
wlist, dipole_w = FT_Dipole(dipole_list,dt)
PowerSpectrum(wlist,dipole_w,'PowerSpectrum00')
dnlkh

for i in range(0,len(IC[0])):
    for j in range(0,len(IC[1])):
        cPart = Initialize(i,j,IC,xStart)
        #xlist = []
        #ylist = []
        #vxlist = []
        #vylist = []
        #axlist = []
        #aylist = []
        dipole_list = []
        timelist = []
        t = 0
        final_t = FinalTime(cPart[1][0],TotalDistance)
        while (t < final_t):
            cPart,xaccel,yaccel = UpdateParticle(cPart,dt) #MaxDistance,vdiff)
            #xlist.append(cPart[0][0])
            #ylist.append(cPart[0][1])
            #vxlist.append(cPart[1][0])
            #vylist.append(cPart[1][1])
            #axlist.append(xaccel)
            #aylist.append(yaccel)
            dipole_change = math.sqrt(xaccel**2 + yaccel**2)
            dipole_list.append(dipole_change)
            timelist.append(t)
            t += dt
        #MakePlot(timelist,xlist,ylist,'Position','Position'+str(i)+str(j))
        #MakePlot(timelist,vxlist,vylist,'Velocity','Velocity'+str(i)+str(j))
        #MakePlot(timelist,axlist,aylist,'Acceleration','Acceleration'+str(i)+str(j))
        break
    break

