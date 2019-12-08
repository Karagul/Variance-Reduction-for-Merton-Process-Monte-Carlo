# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 19:25:36 2017

@author: wuqianfan
"""

import numpy as np
import matplotlib.pyplot as plt

# parameters
T = 1; S0 = 100; xi = 110; V0 = 0.12; kappa = 2; theta = 0.15; sigma = 0.8; r = 0

def Euler_Heston(N):
    
    dt = T/N; ST = S0; VT = V0;
    for i in range(N):
        ST += r * ST * dt + max(VT,0) ** 0.5 * ST * dt**0.5* np.random.randn()
        VT += kappa * (theta - VT)*dt + sigma * max(VT,0) ** 0.5 * dt**0.5* np.random.randn()
    
    return [ST,VT]

'''PROBLEM (a) generating samples'''

N_list = [1,2,5,10,100,1000]; K = 1000
'storing the samples'
samples = []
for N in N_list:
    samples_ST = []; samples_VT = []
    for k in range(K):
        samples_ST.append(Euler_Heston(N)[0])
        samples_VT.append(Euler_Heston(N)[1])
    samples.append([samples_ST,samples_VT])
    
    
''' plotting'''

plt.figure(figsize=(10,5*len(N_list)))
for n in range(len(N_list)):
    plt.subplot(len(N_list),2,2*n + 1)
    'Distibution of ST'
    plt.hist(samples[n][0], bins = 20, range = (-50,250), fill = False, normed = True)
    plt.title("Distribution of S(T), N ="+ str(N_list[n])+ 
              ", (Average = " + str(round(np.mean(samples[n][0]),2))+ ")")
    plt.ylim( 0, 0.015 )
    plt.subplot(len(N_list),2,2*n + 2)
    'Distibution of VT'
    plt.hist(samples[n][1], bins = 20, range = (-1,1), fill = False, normed = True)
    plt.title("Distribution of V(T), N ="+ str(N_list[n])+ 
              ", (Average = " + str(round(np.mean(samples[n][1]),4))+ ")")
    plt.ylim( 0, 6 )

plt.show()



''' generating samples'''

N_list = [1,2,5,10,100,1000]; K_list = [100,500,1000,5000,10000]
estimations = [] #should be 3D list, 6 N's, 5 K's, and each K has K samples

#Assume we have 500 estimator of c(0)
Nsamples = 500

for N in N_list:
    estimations_N = []
    for K in K_list:
        estimations_K = []
        for i in range(Nsamples):
            S = 0
            for k in range(K):
                ST = Euler_Heston(N)[0]
                S += np.exp(-r*T) * max(ST - xi, 0)
            estimations_K.append(S/K)
        estimations_N.append(estimations_K)
        print('N =', N,'K =', K, ' finished')
        print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        
    estimations.append(estimations_N)
    
''' plotting'''

plt.figure(figsize=(5*len(K_list),5*len(N_list)))

for n in range(len(N_list)):
    
    for k in range(len(K_list)):
        
        plt.subplot(len(N_list),len(K_list) , n * len(K_list) + k + 1)
        
        plt.hist(estimations[n][k], bins = 20, range = (0,20), fill = False, normed = True)
        plt.title("N ="+ str(N_list[n])+ ", K = " + str(K_list[k]) + 
                  ", Mean =" + str(round(np.mean(estimations[n][k]),2)))
        plt.ylabel('Density')
        plt.xlabel('c(0)')
        plt.ylim( 0, 1 )

plt.show()



''' generating samples'''

K_list = [100,500,1000,5000,10000]

estimations = [] #should be 2D list, 5 N&K's and each K has K samples

Nsamples = 500

for K in K_list:
    samples = []
    for i in range(Nsamples):
        S = 0
        for k in range(K):
            ST = Euler_Heston(int(K**0.5))[0]
            S += np.exp(-r*T) * max(ST - xi, 0)
        samples.append(S/K)
    
    estimations.append(samples)
print(estimations)
    
''' plotting'''
plt.figure(figsize=(5,5*len(K_list)))
for i in range(len(K_list)): # i = 0,1,2,3,4
    
    plt.subplot(len(K_list),1, i+1)
    plt.hist(estimations[i], bins = 10, range = (5,15), fill = False, normed = True)
    plt.title("K ="+ str(K_list[i])+ ", N = " + str(int(K_list[i]**0.5)) + 
              ", Mean =" + str(round(np.mean(estimations[i]),2)))
    plt.ylabel('Density')
    plt.xlabel('Estimator of c(0)')
    plt.ylim( 0, 1 )

plt.show()

