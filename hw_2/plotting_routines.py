import matplotlib.pyplot as plt

def Sigma_Plot(nu, sigma, filename):
    plt.plot(nu,sigma)
    plt.xlabel("Frequency (arbitrary units)")
    plt.ylabel("Cross Section (arbitrary units)")
    plt.savefig(filename + ".png")
    plt.clf()
