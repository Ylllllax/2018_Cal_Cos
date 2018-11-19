
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.integrate as sci
from scipy.stats import chisquare

theta_mean=[]
theta_median=[]
theta_sigma2=[]
theta_sigma=[]
z_mean=[]
z_median=[]

plt.figure(figsize=(10,8))

data_z_1 = [0.158, 0.227, 0.237, 0.242, 0.303, 0.46, 0.513, 0.518, 0.538, 0.542, 0.571, 0.587]
data_theta_1 = [26.1, 9.1, 32.8, 5.3, 8.4, 6.6, 1.6, 24, 3.2, 32.6, 1.4, 5.5]
theta_mean.append(np.mean(data_theta_1))
theta_median.append(np.median(data_theta_1))
a=0
for i in range(12):
    a=a+((data_theta_1[i]-theta_median[-1])**2)
theta_sigma2.append(np.var(data_theta_1))
theta_sigma.append((a**0.5)/12)
z_mean.append(np.mean(data_z_1))
z_median.append(np.median(data_z_1))



data_z_2 = [0.594, 0.595, 0.605, 0.611, 0.623, 0.63, 0.63, 0.635, 0.652, 0.657, 0.66, 0.664]
data_theta_2 = [5.6, 5.6, 4.5, 25.1, 17.4, 2.1, 1.8, 15.7, 13.5, 2.6, 1.5, 1.4]
theta_mean.append(np.mean(data_theta_2))
theta_median.append(np.median(data_theta_2))
a=0
for i in range(12):
    a=a+((data_theta_2[i]-theta_median[-1])**2)
theta_sigma2.append(np.var(data_theta_2))
theta_sigma.append((a**0.5)/12)
z_mean.append(np.mean(data_z_2))
z_median.append(np.median(data_z_2))


data_z_3 =  [0.664, 0.672, 0.674, 0.677, 0.719, 0.729, 0.751, 0.764, 0.782, 0.789, 0.815, 0.835]
data_theta_3 = [6.1, 5.4, 10.7, 1.5, 12.3, 3.6, 4.1, 10.3, 3.6, 3.1, 16, 2.1]
theta_mean.append(np.mean(data_theta_3))
theta_median.append(np.median(data_theta_3))
a=0
for i in range(12):
    a=a+((data_theta_3[i]-theta_median[-1])**2)
theta_sigma2.append(np.var(data_theta_3))
theta_sigma.append((a**0.5)/12)
z_mean.append(np.mean(data_z_3))
z_median.append(np.median(data_z_3))

data_z_4 =   [0.852, 0.857, 0.859, 0.867, 0.876, 0.895, 0.899, 0.902, 0.933, 0.94, 0.94, 0.976, 0.997]
data_theta_4 = [1.3, 36.8, 7.8, 20.9, 1.7, 3.3, 2.2, 4.5, 1, 2.1, 3.9, 0.9, 3.8]
theta_mean.append(np.mean(data_theta_4))
theta_median.append(np.median(data_theta_4))
a=0
for i in range(13):
    a=a+((data_theta_4[i]-theta_median[-1])**2)
theta_sigma2.append(np.var(data_theta_4))
theta_sigma.append((a**0.5)/13)
z_mean.append(np.mean(data_z_4))
z_median.append(np.median(data_z_4))


data_z_5 = [ 1.003, 1.019, 1.025, 1.049, 1.076, 1.096, 1.104, 1.11, 1.187, 1.201, 1.207, 1.216]
data_theta_5 =  [1.7, 3.6, 10.6, 4.5, 5.8, 2.1, 2.3, 2, 16.1, 8.8, 3.5, 4.3]
theta_mean.append(np.mean(data_theta_5))
theta_median.append(np.median(data_theta_5))
a=0
for i in range(12):
    a=a+((data_theta_5[i]-theta_median[-1])**2)
theta_sigma2.append(np.var(data_theta_5))
theta_sigma.append((a**0.5)/12)
z_mean.append(np.mean(data_z_5))
z_median.append(np.median(data_z_5))


data_z_6 =  [ 1.24, 1.25, 1.25, 1.252, 1.254, 1.259, 1.266, 1.275, 1.29, 1.292, 1.298, 1.322]
data_theta_6 = [1.6, 2.8, 1.6, 8.3, 3.4, 9.8, 3.6, 2.3, 4.4, 3.5, 4, 6]
theta_mean.append(np.mean(data_theta_6))
theta_median.append(np.median(data_theta_6))
a=0
for i in range(12):
    a=a+((data_theta_6[i]-theta_median[-1])**2)
theta_sigma2.append(np.var(data_theta_6))
theta_sigma.append((a**0.5)/12)
z_mean.append(np.mean(data_z_6))
z_median.append(np.median(data_z_6))


data_z_7 =  [ 1.325, 1.344, 1.379, 1.38, 1.404, 1.417, 1.435, 1.44, 1.446, 1.476, 1.499, 1.513]
data_theta_7 =  [2.3, 1.7, 0.7, 8.7, 4.9, 2.7, 1.2, 3.2, 5.1, 4.1, 4.9, 10.9]
theta_mean.append(np.mean(data_theta_7))
theta_median.append(np.median(data_theta_7))
a=0
for i in range(12):
    a=a+((data_theta_7[i]-theta_median[-1])**2)
theta_sigma2.append(np.var(data_theta_7))
theta_sigma.append((a/12)**0.5)
z_mean.append(np.mean(data_z_7))
z_median.append(np.median(data_z_7))


data_z_8 =[ 1.537, 1.545, 1.552, 1.555, 1.561, 1.564, 1.598, 1.733, 1.775, 1.832, 1.84, 1.85]
data_theta_8 =[1.4, 1.6, 10.5, 4.4, 1.5, 10.1, 2.7, 1, 8.8, 0.9, 1.3, 5.7]
theta_mean.append(np.mean(data_theta_8))
theta_median.append(np.median(data_theta_8))
a=0
for i in range(12):
    a=a+((data_theta_8[i]-theta_median[-1])**2)
theta_sigma2.append(np.var(data_theta_8))
theta_sigma.append((a**0.5)/12)
z_mean.append(np.mean(data_z_8))
z_median.append(np.median(data_z_8))



data_z_9 = [ 1.864, 1.875, 1.886, 1.897, 1.924, 1.946, 1.977, 2.028, 2.073, 2.101, 2.102, 2.107]
data_theta_9 =  [1.1, 8.5, 1.7, 3.3, 5.1, 9.8, 2.7, 2.2, 1, 1.2, 2.1, 10.6]
theta_mean.append(np.mean(data_theta_9))
theta_median.append(np.median(data_theta_9))
a=0
for i in range(12):
    a=a+((data_theta_9[i]-theta_median[-1])**2)
theta_sigma2.append(np.var(data_theta_9))
theta_sigma.append((a**0.5)/12)
z_mean.append(np.mean(data_z_9))
z_median.append(np.median(data_z_9))


data_z_10 = [ 2.109, 2.11, 2.12, 2.169, 2.179, 2.181, 2.187, 2.249, 2.286, 2.338, 2.36, 2.367]
data_theta_10 =[4.4, 10.8, 2.4, 7.1, 6.2, 4.4, 4.9, 1, 4.6, 10.6, 4, 13.1]
theta_mean.append(np.mean(data_theta_10))
theta_median.append(np.median(data_theta_10))
a=0
for i in range(12):
    a=a+((data_theta_10[i]-theta_median[-1])**2)
theta_sigma2.append(np.var(data_theta_10))
theta_sigma.append((a**0.5)/12)
z_mean.append(np.mean(data_z_10))
z_median.append(np.median(data_z_10))


data_z_11 = [ 2.427, 2.492, 2.501, 2.547, 2.55, 2.558, 2.582, 2.675, 2.69, 2.702, 2.991, 3.103]
data_theta_11 = [2.9, 1.9, 4, 2, 5.4, 7, 2.3, 1.2, 1, 4.9, 9.8, 3.8]
theta_mean.append(np.mean(data_theta_11))
theta_median.append(np.median(data_theta_11))
a=0
for i in range(12):
    a=a+((data_theta_11[i]-theta_median[-1])**2)
theta_sigma2.append(np.var(data_theta_11))
theta_sigma.append((a**0.5)/12)
z_mean.append(np.mean(data_z_11))
z_median.append(np.median(data_z_11))


data_z_12 = [3.198, 3.2, 3.2, 3.387, 3.469, 3.58, 3.59, 3.75, 3.818, 3.889, 3.891, 4.715]
data_theta_12 = [2.8, 5.1, 7.1, 4.9, 6.5, 4, 4.6, 14.2, 2, 2.7, 1.2, 1.2]
theta_mean.append(np.mean(data_theta_12))
theta_median.append(np.median(data_theta_12))
a=0
for i in range(12):
    a=a+((data_theta_12[i]-theta_median[-1])**2)
theta_sigma2.append(np.var(data_theta_12))
theta_sigma.append((a**0.5)/12)
z_mean.append(np.mean(data_z_12))
z_median.append(np.median(data_z_12))


'''
expect_theta=[]
for j in range(0,10):
    a=(1+z_median[j])**(-1)
    b=1
    xi_z= sci.quad(f,a,b)[0]
    expect_theta.append(D*(1+z_median[j])/xi_z)
observed=np.array(theta_median)  
expected=np.array(expect_theta)
print(chisquare(observed, expected))#普通ChiSquare检验
'''


lh=29.41
c=1470
D=100*lh/c
K=1000
omega_0=0
Omega_m_0=0

'''
ka2=0
Omega_m=0.2
omega=-1
def f(x):
    return (x*((x**(-1))*Omega_m+(x**(-1-3*omega))*(1-Omega_m))**0.5)**(-1)
for j in range(0,12):
    a=(1+z_mean[j])**(-1)
    b=1
    xi_z= sci.quad(f,a,b)[0]
    print(theta_median[j],D*(1+z_mean[j])/xi_z,theta_sigma2[j])
    ka2 = ka2 + (theta_median[j]-D*(1+z_median[j])/xi_z)**2/theta_sigma2[j]
print(ka2)
'''

for m in range(0,100):
    Omega_m = m/100
    for n in range(-100,0):
        omega = n/100
        ka2=0
        def f(x):
            return (x*((x**(-1))*Omega_m+(x**(-1-3*omega))*(1-Omega_m))**0.5)**(-1)
        for j in range(0,12):
            a=(1+z_median[j])**(-1)
            b=1
            xi_z= sci.quad(f,a,b)[0]
            ka2 = ka2 + (theta_median[j]-D*(1+z_median[j])/xi_z)**2/(theta_sigma[j]**2)
        if ka2 < K :
            K=ka2
            omega_0=omega
            Omega_m_0=Omega_m
        print(ka2)
        
for m in range(0,100):
    Omega_m = m/100
    for n in range(-100,0):
        omega = n/100
        ka2=0
        def f(x):
            return (x*((x**(-1))*Omega_m+(x**(-1-3*omega))*(1-Omega_m))**0.5)**(-1)
        for j in range(0,12):
            a=(1+z_median[j])**(-1)
            b=1
            xi_z= sci.quad(f,a,b)[0]
            ka2 = ka2 + (theta_median[j]-D*(1+z_median[j])/xi_z)**2/(theta_sigma[j]**2)
        if  ka2-K <= 2.3 :
            plt.plot(Omega_m,omega,'ro')
        elif  2.3 <=  ka2-K <=	5.99 :
            plt.plot(Omega_m,omega,'bo')

        

print("Omega_m_0=",Omega_m_0,"omega_0=",omega_0,"chi^2=",K)
plt.xlabel(r"$\Omega_m$")
plt.ylabel(r"$\omega$")
plt.xlim(0,1)
plt.ylim(-1,0)
plt.title("Confidence region")
plt.legend()
plt.show()
