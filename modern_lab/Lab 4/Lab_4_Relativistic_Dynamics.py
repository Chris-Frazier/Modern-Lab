import matplotlib.pyplot as plt
plt.style.use('bmh')
import numpy as np
from matplotlib import pylab
import csv
from statistics import mean, stdev, variance




'''
# Example of polyfit
points = np.array([(1, 1), (2, 4), (3, 1), (9, 3)])

x = points[:, 0]
y = points[:, 1]

z = np.polyfit(x, y, 3)
f = np.poly1d(z)
print(f)

x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new)
plt.show()
'''

# read in the data from the text files
x, y = np.loadtxt('newCs137.txt', unpack=True)
x2, y2 = np.loadtxt('newCo60.txt', unpack=True)
x3, y3 = np.loadtxt('newBa133.txt', unpack=True)
x4, y4 = np.loadtxt('newNa22.txt', unpack=True)
x5, y5 = np.loadtxt('E_vs_p.txt', unpack=True)

# plot the gamma spectrum for each sample
'''
plt.scatter(x, y, color='r', edgecolors='k')
plt.axis([200, 600, 0, 5000])
plt.title('Cs 137')
plt.xlabel('channel number')
plt.ylabel('counts')
#plt.show()
'''

'''
plt.scatter(x2,y2, edgecolors='k')
plt.axis([500, 1000, -1000, 8000])
plt.title('Co 60')
plt.xlabel('channel number')
plt.ylabel('counts')
plt.show()
'''

'''
plt.scatter(x3,y3,color='g', edgecolors='k')
plt.axis([100, 400, -1000, 31000])
plt.title('Ba 133')
plt.xlabel('channel number')
plt.ylabel('counts')
plt.show()
'''

'''
plt.scatter(x4,y4, color='c', edgecolors='k')
plt.axis([100, 1200, -1000, 110000])
plt.title('Na 122')
plt.xlabel('channel number')
plt.ylabel('counts')
plt.show()
'''

# Fit a gaussian function to the photopeak for each graph
# Cs137
'''
xm = x[386:464]
ym = y[386:464]
ry = []
v = 77
while v > -1:
    ry.append(ym[v])
    v -= 1

#print(ry)

#plt.scatter(xm, ry)
#plt.axis([360, 520, -150, 5000])
#plt.show()


#plt.scatter(xm, ym)
#plt.axis([360, 520, -150, 5000])
#plt.show()


xn = x[218:386]
yn = y[218:386]

rn = []
v2 = 0
while v2 < 90:
    rn.append(yn[v2])
    v2 += 1

v3 = 0
while v2 < 168:
    rn.append(yn[v2] - ry[v3])
    v2 += 1
    v3 += 1
#print(rn)
#print(yn)
#print(xn[0])

#plt.scatter(xn, rn)
#plt.scatter(xn, yn)
#plt.scatter(xm, ry)
#plt.scatter(xm, ym)
#plt.axis([250, 550, -550, 5000])
#plt.show()


z = np.polyfit(xn[25:75], rn[25:75], 3)
f = np.poly1d(z)
print(f)

x_new = np.linspace(xn[0], xn[100], 50)
y_new = f(x_new)

#plt.plot(xn, rn, 'o', x_new, y_new)
plt.plot(x_new, y_new, color='b')
plt.axvline(324, color='black')
plt.axvline(443, color='black')
plt.show()
'''

'''
#Co60
xc = x2[500:700]
yc = y2[500:700]

plt.scatter(xc, yc)


z2 = np.polyfit(xc, yc, 3)
f2 = np.poly1d(z2)
print(f2)

xc_new = np.linspace(xc[0], xc[-1], 50)
yc_new = f2(xc_new)

plt.plot(xc_new, yc_new, color='k')
plt.axvline(596, color='k')
plt.show()
'''

'''
# Ba133
xb1 = x3[244:377]
yb1 = y3[244:377]

xb2 = x3[110:243]
yb2 = y3[110:243]

ryb1 = []
v4 = 132
while v4 > -1:
    ryb1.append(yb1[v4])
    v4 -= 1

v5 = 0
ryb2 = []
while v5 < 133:
    ryb2.append(yb2[v5] -ryb1[v5])
    v5 += 1

#plt.scatter(xb1, ryb1)
#plt.show()

plt.scatter(xb2, yb2)
#plt.show()

plt.scatter(xb2, ryb2)
#plt.show()


#plt.scatter(xb1, yb1)


z3 = np.polyfit(xb2[30:70], ryb2[30:70], 3)
f3 = np.poly1d(z3)
print(f3)

xb_new = np.linspace(xb2[0], xb2[-1], 50)
yb_new = f3(xb_new)

plt.plot(xb_new, yb_new, color='k')
plt.axvline(150, color='k')
plt.show()
'''

'''
#Na22
xn = x4[352:500]
yn = y4[352:500]

xn2 = x4[100:351]
yn2 = y4[100:351]

ryn = []
v6 = 147
while v6 > -1:
    ryn.append(yn[v6])
    v6 -= 1
myn = []
v7 = 0
while v7 < 103:
    myn.append(yn2[v7])
    v7 += 1
v8 = 0
while v7 < 251:
    myn.append(yn2[v7] - ryn[v8])
    v7 += 1
    v8 += 1


xn3 = x4[850:1050]
yn3 = y4[850:1050]

xn4 = x4[650:849]
yn4 = y4[650:849]



#plt.scatter(xn, ryn)
#plt.scatter(xn, yn)
#plt.show()

#plt.scatter(xn2, myn)
#plt.show()

#plt.scatter(xn3, yn3)
#plt.show()

plt.scatter(xn4, yn4)
#plt.show()


z4 = np.polyfit(xn4[0:100], yn4[0:100], 3)
f4 = np.poly1d(z4)
print(f4)

xn_new = np.linspace(xn4[0], xn4[100], 50)
yn_new = f4(xn_new)

plt.plot(xn_new, yn_new, color='k')
plt.axvline(701, color='k')
plt.show()
'''
# plot of energy vs momentum of electron
z5 = np.polyfit(x5, y5, 2)
f5 = np.poly1d(z5)
print(f5)

x5_new = np.linspace(260000, 770000, 50)
y5_new = f5(x5_new)

xerr = 0
yerr = 0.0002

plt.errorbar(x5, y5, yerr=yerr, xerr=xerr, fmt='o', capsize=5, ecolor='r')
plt.plot(x5_new, y5_new, color='g', label='Best fit line')
plt.xlabel('Energy (eV)')
plt.ylabel('Momentum (eV/c)')
plt.scatter(x5, y5)
plt.legend()
plt.show()
