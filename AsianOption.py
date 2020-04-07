#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:58:36 2020

@author: daiyu
"""

import math
import numpy as np
np.random.seed(1)

class Asian_option:
    def __init__(self,S, K, T, r, d,sigma):
        self.S, self.K, self.T, self.r, self.d , self.sigma =  S, K, T, r, d, sigma
    # Monte Carlo Method
    def Asian_call(self,n=100000):
 
        np.random.seed(1)
        
        S, K, T, r, d, sigma = self.S, self.K, self.T, self.r, self.d , self.sigma
        
        # delta_T = 1/12
        steps = int(T*12)
        
        # set parameters for grid
        dt = 1/12
        vol = sigma*np.sqrt(dt)
        mu = (r-d-0.5*sigma**2)*dt
        
        #generate random walk from lognormal model
        random = np.random.lognormal(mean=mu,sigma = vol,size=steps*n).reshape(n,steps)
        
        #Set intial value for simulation path
        init = np.ones([n,1])*S
        
        #Simulated path
        random_walk =  np.concatenate((init,random),axis=1)
        price_walk = np.cumprod(random_walk,axis=1)
        
        # Simulated stock price at maturity
        Ave_Value_at_M = (price_walk.sum(axis=1)-S)/steps
                
        # option intrinc value
        option_value = np.where(Ave_Value_at_M>K,Ave_Value_at_M-K,0)
        return option_value.mean()*np.exp(-r*T)
    
    def Asian_put(self,n=100000):
 
        np.random.seed(1)
        
        S, K, T, r, d, sigma = self.S, self.K, self.T, self.r, self.d , self.sigma
        
        # delta_T = 1/12
        steps = int(T*12)
        
        # set parameters for grid
        dt = 1/12
        vol = sigma*np.sqrt(dt)
        mu = (r-d-0.5*sigma**2)*dt
        
        #generate random walk from lognormal model
        random = np.random.lognormal(mean=mu,sigma = vol,size=steps*n).reshape(n,steps)
        
        #Set intial value for simulation path
        init = np.ones([n,1])*S
        
        #Simulated path
        random_walk =  np.concatenate((init,random),axis=1)
        price_walk = np.cumprod(random_walk,axis=1)
        
        # Simulated stock price at maturity
        Ave_Value_at_M = (price_walk.sum(axis=1)-S)/steps
                
        # option intrinc value
        option_value = np.where(Ave_Value_at_M<K,K-Ave_Value_at_M,0)
        return option_value.mean()*np.exp(-r*T)
    
    