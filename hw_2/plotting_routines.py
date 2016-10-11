# Contains plotting routines for cross section and intensity
import matplotlib.pyplot as plt
from parameters import *

def Sigma_Plot(nu, sigma, filename):
    plt.plot(nu,sigma)
    plt.xlabel("Frequency (arbitrary units)")
    plt.ylabel("Cross Section (arbitrary units)")
    plt.savefig(filename + ".png")
    plt.clf()

def Intensity_Plot(nu, I_full, I_0, S, filenames):
    for i in range(0,NumCases):
        plt.plot(nu,I_full[i],c='r',label='Final I')
        plt.plot(nu,I_0[i],c='black',label='Initial I')
        plt.plot(nu,S[i],c='blue',label='S')
        plt.xlabel('Frequency (arbitrary units)')
        plt.ylabel('Intensity (arbitrary units)')
        plt.ylim((0,I_large+1))
        plt.legend()
        plt.savefig(filenames[i] + '.png')
        plt.clf()
