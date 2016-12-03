import h5py
import numpy as np

outfile = h5py.File('silicate.hdf5','w')
f = open('Sil_81')

for i in range(0,5):
    line = f.readline()
    print line

offset = 0
while (offset < 81):
    print offset
    wavelist = []
    Qlist = []
    junk = f.readline()
    sizeline = f.readline()
    sizestr = ''
    for i in range(0,9):
        sizestr += sizeline[i]
    size = float(sizestr)
    junk = f.readline()
    for j in range(9,250):
        line = f.readline()
        wavestr = ''
        for i in range(0,9):
            wavestr += line[i]
        wave = float(wavestr)
        Qstr = ''
        for i in range(10,19):
            Qstr += line[i]
        Q = float(Qstr)
        wavelist.append(wave)
        Qlist.append(Q)
    sizearr = np.array([size])
    wavearr = np.array(wavelist)
    Qarr = np.array(Qlist)
    if (offset < 10):
        offstr = '0' + str(offset)
    else:
        offstr = str(offset)
    this_size = outfile.create_group('Grain'+offstr)
    grain_size = this_size.create_dataset('Size',data=sizearr)
    wavelength = this_size.create_dataset('Wavelength',data=wavearr)
    Q_abs = this_size.create_dataset('Q',data=Qarr)
    offset += 1
    print size

f.close()
outfile.close()
