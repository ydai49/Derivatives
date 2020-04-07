#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:14:33 2020

@author: daiyu
"""
import math
import numpy as np
np.random.seed(1)

class barrier_option:
    def __init__(self,S, K, T, r, d,sigma,H):
        self.S, self.K, self.T, self.r, self.d , self.sigma, self.H= S, K, T, r, d, sigma,H
    
    def up_out_barrier_call(self,n=1000):
        """
        Option ceases to exist when stock price hit H+(S>H+) at any time befero Option Expiration
        n: Number of simulation path
        """
        np.random.seed(1)
        
        S, K, T, r, d, sigma,H = self.S, self.K, self.T, self.r, self.d , self.sigma, self.H
        
        # 252 option trading days in a year
        steps = T*252
        
        # set parameters for grid
        dt = 1/252
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
        Value_at_M = price_walk[:,-1]
        
        # Apply Barrier to simulater result: option continue to exist if S<H
        barrier_check = np.sum((price_walk<H),1)
        option_value = np.where(barrier_check==(steps+1),Value_at_M-K,0)
        # option intrinc value
        option_value = np.where(Value_at_M>K,option_value,0)
        print('In ',n,' times simulated process:')
        print((barrier_check == (steps+1)).sum(),' Option continues to exist')
        return option_value.mean()*np.exp(-r*T)
    
    def down_out_barrier_call(self,n=10000):
        """
        Option ceases to exist when stock price hit H+(S>H+) at any time befero Option Expiration
        n: Number of simulation path
        """
        np.random.seed(1)
        
        S, K, T, r, d, sigma,H = self.S, self.K, self.T, self.r, self.d , self.sigma, self.H
        
        # 252 option trading days in a year
        steps = T*252
        
        # set parameters for grid
        dt = 1/252
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
        Value_at_M = price_walk[:,-1]
        
        # Apply Barrier to simulater result: option continue to exist if S>H
        barrier_check = np.sum((price_walk>H),1)
        
        option_value = np.where(barrier_check==(steps+1),Value_at_M-K,0)
        # option intrinc value
        option_value = np.where(Value_at_M>K,option_value,0)
        print('In ',n,' times simulated process:')
        print((barrier_check == (steps+1)).sum(),' Option continues to exist')
        return option_value.mean()*np.exp(-r*T)