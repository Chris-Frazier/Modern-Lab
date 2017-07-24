import matplotlib.pyplot as plt
import numpy as np
from statistics import mean



# read in the data for each measurement
x, y = np.loadtxt('254nm.txt', unpack=True)
x2, y2 = np.loadtxt('365nm.txt', unpack=True)
x3, y3 = np.loadtxt('408nm.txt', unpack=True)
x4, y4 = np.loadtxt('435_8nm.txt', unpack=True)
x5, y5 = np.loadtxt('545-555nm.txt', unpack=True)
x6, y6 = np.loadtxt('583nm.txt', unpack=True)
x7, y7 = np.loadtxt('688_696nm.txt', unpack=True)

x8, y8 = np.loadtxt('435_8_1OD.txt', unpack=True)
x9, y9 = np.loadtxt('435_8_03OD.txt', unpack=True)
x10, y10 = np.loadtxt('435_8_05OD.txt', unpack=True)
x11, y11 = np.loadtxt('435_8_07OD.txt', unpack=True)

x12, y12 = np.loadtxt('Vs_inv_wave.txt', unpack=True)

# make the plots for each individual data set
'''
plt.scatter(x, y)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (nA)')
plt.title('Current vs Voltage 254nm')
#plt.axhline(y=-5.08, color='black')
plt.show()
'''
'''
plt.scatter(x2, y2)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (nA)')
plt.title('Current vs Voltage 365nm')
#plt.axhline(y= -0.4,color= 'black')
plt.show()
'''
'''
plt.scatter(x3, y3)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (nA)')
plt.title('Current vs Voltage 408nm')
#plt.axhline(y=-0.02, color='black')
plt.show()
'''

plt.scatter(x4, y4)
#plt.xlabel('Voltage (V)')
#plt.ylabel('Current (nA)')
#plt.title('Current vs Voltage 435.8nm')
#plt.axhline(y=-1.15, color='black')
#plt.show()

'''
plt.scatter(x5, y5)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (nA)')
plt.title('Current vs Voltage 546nm')
#plt.axhline(y=-0.08,color= 'black')
plt.show()
'''
'''
plt.scatter(x6, y6)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (nA)')
plt.title('Current vs Voltage 578nm')
#plt.axhline(y=-0.015,color='black')
plt.show()
'''
'''
plt.scatter(x7, y7)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (nA)')
plt.axis([-2, 2, -2, 20])
plt.title('Current vs Voltage 691nm')
#plt.axhline(y=0, color='black')
plt.show()
'''

plt.scatter(x8, y8, label='0.1OD')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (nA)')
plt.title('Current vs Voltage 435.8 1OD')
#plt.show()


plt.scatter(x9, y9, label='0.3OD')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (nA)')
plt.title('Current vs Voltage 435.8 3OD')
#plt.show()

plt.scatter(x10, y10, label='0.5OD')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (nA)')
plt.title('Current vs Voltage 435.8 5OD')
#plt.show()

plt.scatter(x11, y11, label='0.7OD')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (nA)')
plt.title('Current vs Voltage 435.8 OD')
#plt.axhline(y=0, color='black')
plt.legend()
plt.show()


# Generate best fit line for data
def best_fit_slope_and_intercept(x, y):
    m = (((mean(x) * mean(y)) - mean(x*y)) /
         ((mean(x)**2) - mean(x**2)))
    b = mean(y) - m*mean(x)
    return m, b
m, b = best_fit_slope_and_intercept(x12, y12)

reg_line = [(m*x) + b for x in x12]

'''
# Plot of Stopping voltage vs Inverse Wavelength
plt.scatter(x12, y12)
plt.plot(x12, reg_line, color='g')
plt.xlabel('Inverse Wavelength (1/m)')
plt.ylabel('Stopping Voltage (V)')
plt.title('Stopping Voltage vs Inverse Wavelength')
plt.show()
'''
h = m/299792458
print(m, b, h)

