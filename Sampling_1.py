# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 17:25:30 2017

@author: wuqianfan
"""

import numpy as np
import matplotlib.pyplot as plt
import time


# parameters
T = 1; s0 = 100; v0 = 0.12; kappa = 2; theta = 0.15; sigma = 0.8; r = 0
# Function for Euler
def ED_Heston(N):
    dt = T/N; ST = s0; VT = v0;
    for i in range(N):
        ST += r * ST * dt + max(VT,0)**0.5 * ST * dt**0.5 * np.random.randn()
        VT += kappa * (theta-VT) * dt + sigma * max(VT,0)**0.5 * dt**0.5 * np.random.randn()
    
    return [ST,VT]
    
K = [100,500,1000,5000,10000]
nsteps = [int(100**0.5),int(500**0.5),int(1000**0.5),int(5000**0.5),int(10000**0.5)]
epsilon = [70,90,100,110,130]
estimator = []
Estimator = []


# Calculate Estimator
for strike in epsilon:
    estimator = []
    for i in K:
        sum_estimator = 0

        for j in range(i):
            ST = ED_Heston(int(i**0.5))[0]
            sum_estimator += np.exp(-r*T) * max(ST-strike,0)
        estimator += [sum_estimator/i]
    Estimator += [estimator]
    
print(Estimator)

#Calculate Time 

t_time = []
for strike in epsilon:
    run = []
    for i in K:
        sum_estimator = 0
        start = time.time()
        for j in range(i):
        
            ST = ED_Heston(int(i**0.5))[0]
            sum_estimator += np.exp(-r*T) * max(ST-strike,0)
            
        end = time.time()
        run += [end - start]
    t_time += [run]
    
print(t_time)
        
correct_price = [32.70326,18.92499,13.984957, 10.263762,  5.5888102]  
        

        
    
     


        
