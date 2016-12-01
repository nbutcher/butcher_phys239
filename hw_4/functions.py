import numpy as plt
import matplotlib.pyplot as plt

def BasicSpecPlot(wl,lum):
    plt.plot(wl,lum)
    plt.xlabel('Wavelength (microns)')
    plt.ylabel('Luminosity (L_sun / Hz)')
    plt.show()

