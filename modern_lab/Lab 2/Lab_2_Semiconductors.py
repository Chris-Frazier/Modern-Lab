import matplotlib.pyplot as plt
import numpy as np
import csv

#
'''
x = []
y = []

with open('RTP.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
'''

x,y = np.loadtxt('RTP.csv',delimiter=',',unpack=True)

x2,y2 = np.loadtxt('HTP.csv', delimiter=',',unpack=True)

x3,y3 = np.loadtxt('LTP.csv', delimiter=',',unpack=True)

x4,y4 = np.loadtxt('RTN.csv',delimiter=',',unpack=True)

x5,y5 = np.loadtxt('HTN.csv', delimiter=',',unpack=True)

x6,y6 = np.loadtxt('LTN.csv', delimiter=',',unpack=True)

plt.scatter(x,y, label = 'T = 25 C', color = 'b')
plt.scatter(x2,y2, label= 'T = 46 C', color= 'r')
plt.scatter(x3,y3, label= 'T = -193 C', color= 'g')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (nA)')

plt.title('Current vs Voltage \n Positive')
plt.legend()
plt.show()

#plt.scatter(x2,y2)
plt.scatter(x4,y4, label='T = 25 C', color='b')
plt.scatter(x5,y5, label='T = 46 C', color='r')
plt.scatter(x6,y6, label='T = -193 C', color='g')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (pA)')
plt.title('Current vs Voltage \n Negative')
plt.legend()
plt.axis([-1.4,-0.3,-8,0])
plt.show()
#print(x)

