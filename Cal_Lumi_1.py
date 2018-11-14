import numpy as np
import seaborn
import matplotlib.pyplot as plt
import scipy.integrate as sci
'''
theta=2.0
D_A = 1/theta
S   = 0.57
z   = 0.229
al  = -0.04
L=4*np.pi* (D_A**2) *S/((1+z)**(al-3))
print(L)

tehta= 5.1
D_A = 1/theta
S   = 0.12
z   = 3.2
al  = -0.23
L=4*np.pi* (D_A**2) *S/((1+z)**(al-3))
print(L)

theta= 9.8
D_A = 1/theta
S   = 0.55
z   = 3.387
al  = -0.16
L=4*np.pi* (D_A**2) *S/((1+z)**(al-3))
print(L)


S1  = 0.57
S2  = 0.41
S   = (S1+S2)/2
z   = 0.011
al  = 0.27
q   = 0.5
D_A = ((q*z)+(q-1)*(((1+2*q*z)**0.5)-1))/((q**2)*((1+z)**2))
L=4*np.pi* (D_A**2) *S/((1+z)**(al-3))*(10**26)
print(L)

S1  = 0.57
S2  = 0.60
S   = (S1+S2)/2
z   = 0.229
al  = -0.04
q   = 0.5
D_A = ((q*z)+(q-1)*(((1+2*q*z)**0.5)-1))/((q**2)*((1+z)**2))
L=4*np.pi* (D_A**2) *S/((1+z)**(al-3))*(10**26)
print(L)
'''

data=[   1.252,1.8,1.49,0.15,8.3   ]

z=data[0]
S1=data[1]
S2=data[2]
al=data[3]
theta=data[4]

S   = (S1+S2)/2
q   = 0.5
D_A = ((q*z)+(q-1)*(((1+2*q*z)**0.5)-1))/((q**2)*((1+z)**2))
L=4*np.pi* (D_A**2) *S/((1+z)**(al-3))*(10**26)
print(L)
if L>(10**26) :
    print (1)
else:
    print(0)
