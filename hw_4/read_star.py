import h5py
import numpy as np
from parameters import c, L_sun

wavelist = []
llist = []

offset = 511
end_off = offset + 10
f = open('fig7b.txt')
count = 0
for line in f:
    if (count <= 2):
        count += 1
        continue
    wavestr = ''
    for i in range(0,9):
        wavestr += line[i]
    wave = float(wavestr)
    wavelist.append(wave)
    lumstr = ''
    for i in range(offset,end_off):
#        print line[i]
        if (line[i] == '-'):
            lumstr += '-' 
        else:
            lumstr += line[i]
#    print lumstr
    lum = float(lumstr)
    llist.append(lum)
#    count += 1
#    if (count > 20):
#        break


f.close()
A_in_Hz = c / 1e-10
wavearr = np.array(wavelist)# * 1e-4
lumarr = np.array(llist)#* L_sun / A_in_Hz

outfile = h5py.File('temp_star','w') #'Z020_Single.hdf5','w')
wl = outfile.create_dataset('Wavelength',data=wavearr)
luminosity = outfile.create_dataset('Luminosity',data=lumarr)
outfile.close()
