# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 19:32:40 2023

@author: dadou
"""

import matplotlib.pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i ** 2)
    myCubic.append(i ** 3)
    myExponential.append(1.5 ** i)


plt.figure('lin')
plt.clf()
plt.title('Linear')
plt.ylim(0, 1000)
plt.plot(mySamples, myLinear, 'b-', label='linear')
plt.legend(loc='upper left')

plt.figure('quad')
plt.clf()
plt.title('Quadratic')
plt.ylim(0, 1000)
plt.plot(mySamples, myQuadratic, 'ro', label='quadratic')
plt.legend(loc='upper left')

plt.figure('cub')
plt.clf()
plt.title('Cubic')
plt.ylim(0, 1000)
plt.plot(mySamples, myCubic, 'g^', label='cubic')
plt.legend(loc='upper left')

plt.figure('exp')
plt.clf()
plt.title('Exponential')
plt.ylim(0, 1000)
plt.plot(mySamples, myExponential, label='exponential')
plt.legend(loc='upper left')

plt.figure('les4')
plt.clf()
plt.title('les 4 figures')
plt.ylim(0, 10000)
plt.plot(mySamples, myLinear, 'b-', label='linear')
plt.plot(mySamples, myQuadratic, 'ro', label='quadratic')
plt.plot(mySamples, myCubic, 'g^', label='cubic')
plt.plot(mySamples, myExponential, 'r--', label='exponential')
plt.legend(loc='upper left')

plt.figure('les4a')
plt.clf()
plt.title('les 4 figures')
plt.subplot(211)
plt.ylim(0, 10000)
plt.plot(mySamples, myLinear, 'b-', label='linear')
plt.plot(mySamples, myQuadratic, 'ro', label='quadratic')
plt.plot(mySamples, myCubic, 'g^', label='cubic')
plt.plot(mySamples, myExponential, 'r--', label='exponential')
plt.legend(loc='upper left')

plt.figure('les4b')
plt.clf()
plt.title('les 4 figures')
plt.subplot(212)
plt.ylim(0, 10000)
plt.plot(mySamples, myLinear, 'b-', label='linear')
plt.plot(mySamples, myQuadratic, 'ro', label='quadratic')
plt.plot(mySamples, myCubic, 'g^', label='cubic')
plt.plot(mySamples, myExponential, 'r--', label='exponential')
plt.legend(loc='upper left')

plt.figure('les4c')
plt.clf()
plt.title('les 4 figures')
plt.subplot(121)
plt.ylim(0, 10000)
plt.plot(mySamples, myLinear, 'b-', label='linear')
plt.plot(mySamples, myQuadratic, 'ro', label='quadratic')
plt.plot(mySamples, myCubic, 'g^', label='cubic')
plt.plot(mySamples, myExponential, 'r--', label='exponential')
plt.legend(loc='upper left')

plt.figure('les4d')
plt.clf()
plt.title('les 4 figures')
plt.subplot(122)
plt.ylim(0, 10000)
plt.plot(mySamples, myLinear, 'b-', label='linear')
plt.plot(mySamples, myQuadratic, 'ro', label='quadratic')
plt.plot(mySamples, myCubic, 'g^', label='cubic')
plt.plot(mySamples, myExponential, 'r--', label='exponential')
plt.legend(loc='upper left')
