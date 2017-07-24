import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import numpy as np
from matplotlib import pylab
from statistics import mean, variance, stdev

# read in data from text file
x, y = np.loadtxt('H_D_Spectrum.txt', unpack=True)
x2, y2 = np.loadtxt('BackGroundH_D.txt', unpack=True)
x3, y3 = np.loadtxt('He_Spectrum.txt', unpack=True)
x4, y4 = np.loadtxt('BackGround_He.txt', unpack=True)

plt.plot(x, y)
#plt.axvline(656.27,color='k')
#plt.axvline(656.08, color='k')
plt.xlabel('Wavelength (nm)')
plt.show()

#plt.plot(x3,y3)
#plt.plot(x4,y4)
#plt.show()


