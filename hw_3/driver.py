from parameters import *
from functions import *

for i in range(0,len(IC[0])):
    for j in range(0,len(IC[1])):
        cPart = Initialize(i,j,IC,xStart)
        print 'Begin'
        print cPart[0], cPart[1]
        xlist = []
        ylist = []
        vxlist = []
        vylist = []
        axlist = []
        aylist = []
        timelist = []
        t = 0
        final_t = FinalTime(cPart[1][0],TotalDistance)
        while (t < final_t):
            cPart,xaccel,yaccel = UpdateParticle(cPart,dt) #MaxDistance,vdiff)
            #cPart = UpdatePos(cPart,dt)
            xlist.append(cPart[0][0])
            ylist.append(cPart[0][1])
            vxlist.append(cPart[1][0])
            vylist.append(cPart[1][1])
            axlist.append(xaccel)
            aylist.append(yaccel)
            timelist.append(t)
            t += dt
        print 'Final'
        print cPart[0], cPart[1]
        MakePlot(timelist,xlist,ylist,'Position','Position'+str(i)+str(j))
        MakePlot(timelist,vxlist,vylist,'Velocity','Velocity'+str(i)+str(j))
        MakePlot(timelist,axlist,aylist,'Acceleration','Acceleration'+str(i)+str(j))
        break
    break

