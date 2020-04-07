#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:13:26 2020

@author: daiyu
"""
import math
import numpy as np
np.random.seed(1)

class Monte_carlo:
    def __init__(self,S, K, T, r, d,sigma):
        self.S, self.K, self.T, self.r, self.d , self.sigma = S, K, T, r, d, sigma
    
    def option_pricing(self,Type='c'):
        """
        Option Pricing with lognormal model
        """
        S, K, T, r, d, sigma = self.S, self.K, self.T, self.r, self.d , self.sigma
        
        mu = (r-d-0.5*sigma**2)*T
        vol = sigma*np.sqrt(T)
        
        np.random.seed(1)
        
        Simu_S = S*np.random.lognormal(mean=mu,sigma = vol,size=10000)
        
        V_call = np.vectorize(lambda X: X-K if X>K else 0)
        
        V_put = np.vectorize(lambda X: K-X if X<K else 0)
        
        if Type=='c':
            return V_call(Simu_S).mean()*np.exp(-r*T)
        else:
            return V_put(Simu_S).mean()*np.exp(-r*T)
        
    
         
    def option_greeks(self,Type='c'):
        S, K, T, r, d, sigma = self.S, self.K, self.T, self.r, self.d , self.sigma
        
        delta = self.option_pricing2(S+1, K, T, r, d, sigma,Type)-self.option_pricing2(S, K, T, r, d, sigma,Type)
        gamma = self.option_pricing2(S+1, K, T, r, d, sigma,Type)+self.option_pricing2(S-1, K, T, r, d, sigma,Type)-2*self.option_pricing2(S, K, T, r, d, sigma,Type)
        t = 1/360
        theta = -(self.option_pricing2(S, K, T-t, r, d, sigma,Type)-self.option_pricing2(S, K, T, r, d, sigma,Type))/t
        rho = (self.option_pricing2(S, K, T, r+0.0001, d, sigma,Type) - self.option_pricing2(S, K, T, r, d, sigma,Type))/0.01
        vega = (self.option_pricing2(S, K, T, r, d, sigma+0.01,Type) - self.option_pricing2(S, K, T, r, d, sigma,Type))/0.01
        greeks ={}
        greeks['delta']=delta
        greeks['gamma']=gamma
        greeks['theta']=theta
        greeks['vage']=vega
        greeks['rho']=rho
        
        return greeks
    
    @staticmethod
    def option_pricing2(S, K, T, r, d, sigma,Type='c'):
        """
        Option Pricing with lognormal model
        """        
        mu = (r-d-0.5*sigma**2)*T
        vol = sigma*np.sqrt(T)
        
        np.random.seed(1)
        
        Simu_S = S*np.random.lognormal(mean=mu,sigma = vol,size=10000)
        
        V_call = np.vectorize(lambda X: X-K if X>K else 0)
        
        V_put = np.vectorize(lambda X: K-X if X<K else 0)
        
        if Type=='c':
            return V_call(Simu_S).mean()*np.exp(-r*T)
        else:
            return V_put(Simu_S).mean()*np.exp(-r*T)
    