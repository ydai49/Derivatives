#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:22:19 2020

@author: daiyu
"""

from math import *

def phi(x):
    #'Cumulative distribution function for the standard normal distribution'
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

def EuropeanOption(S=100,K=100,d=0,r=0,vol=0.3,tau=1) :
    
    d1, d2 = 0, 0

    def _d1():
        return (log(S/K)+(d-r+0.5*vol*vol)*tau)/(vol*sqrt(tau))
    
    
    def _d2():
        return (log(S/K)+(d-r-0.5*vol*vol)*tau)/(vol*sqrt(tau))
    
    def call():
        return S*exp(-d*tau)*phi(d1) - K*exp(-r*tau)*phi(d2)
    
    def put():
        return K*exp(-r*tau)*phi(-d2) - S*exp(-d*tau)*phi(-d1)
    
    def call_delta() :
        return exp(-d*tau)*phi(d1)
    
    def put_delta() :
        return -exp(-d*tau)*phi(-d1)

    def gamma() :
        return exp(-d*tau-0.5*d1*d1)/(S*vol*sqrt(6.2831852*tau))
    
    def vega() :
        return S*S*vol*tau*gamma()
     
    
    def option():
        nonlocal d1, d2
        d1 = _d1()
        d2 = _d2()
        print('d1=',d1,', d2=',d2)
            
    option.call = call
    option.put = put
    option.call_delta = call_delta
    option.put_delta = put_delta
    option.gamma = gamma
    option.vega = vega

    return option