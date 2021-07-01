# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 15:42:10 2021

@author: Julija
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import re

#initial values :
# [a;b] interval,  n - points,  x_interp - point for interpolation

a = np.pi/12
b = np.pi/3
n = 2
x = np.empty([n+1,1])
y = np.empty([n+1,1])
x_interp = 0.6283

def f(x):
    return np.sin(x)
def f2(i):
    return ((y[i+1]-y[i])/(x[i+1]-x[i]))
def f3(i):
    return ((f2(i+1)-f2(i))/(x[i+2]-x[i]))
def M2(i):
    return 2*np.abs(f3(i))   
def assign_values(a,b,x,y,n):
    h = (b-a)/n
    for i in range (0,n+1):
        x[i] = a
        a = a + h
    for i in range (len(x)):    
        y[i] = f(x[i])
        print(x[i], "   ",y[i])

def linear_interpolation(x,y,x_given):
    for i in range(len(x)):
        if( x[i]<= x_given <= x[i+1]):
            print("Linear interpolation metrics: M2: ",formating(M2(i)),"Error: ", formating(0.125*M2(i)*(x[i+1]-x[i])**2))
            return ((y[i+1]-y[i])/(n-x[i]))*(n-x[i])+y[i]

def quadratic__interpolation(x,y,x_given):
    for i in range(len(x)):
        if(x[i] <= x_given <= x[i+1]):
            return (y[i]+f2(i)*(x_given-x[i])+f3(i)*(x_given-x[i])*(x_given-x[i+1]))

def visualization():
    plt.rcParams["figure.figsize"] = (7,2)
    plt.plot(x, y, '-o')
    plt.plot(x_interp, linear_result, 'o')
    plt.text(linear_result, x_interp + 0.01,  r"$Linear: %f$" %linear_result, ha='right')
    plt.plot(x_interp, quadratic_result, 'o')
    plt.text(quadratic_result, x_interp - 0.1,  r"$Quadratic: %f$" %quadratic_result, ha='left')
    plt.plot(x_interp, f(x_interp), 'r*')
    plt.text(f(x_interp) + 0.1, x_interp,  r"$Real: %f$" %f(x_interp), ha='left')
    
def formating(arr):
    return re.sub('[\[\]]', '', np.array_str(arr))

assign_values(a,b,x,y,n)
linear_result = linear_interpolation(x,y,x_interp)
quadratic_result = quadratic__interpolation(x,y,x_interp)
print('Linear interpolation result:     {} real error: {}'\
      .format(formating(linear_result),formating(abs(f(x_interp) - linear_result))))
print('Quadratic interpolation result:  {} real error: {}'\
      .format(formating(quadratic_result),formating(abs(f(x_interp) - quadratic_result))))
print('Real function result:            {:.8}'.format(f(x_interp)))

visualization()
