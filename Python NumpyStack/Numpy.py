#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:26:24 2020

@author: ashishsharma
"""


import numpy as np

L = [1,2,3] #is a list

L.append(55)

L = L + [22] # to append element

for el in L:
    print(el)
    
A = np.array([1,2,3,4])  #is fixed array. 

A + [33] # to add 33 in all elements of array. 

A = A + np.array([2,4,1,4])

for e in A:
    print(e)
    
    
# mathematical operations on
#   Array does the operation on elements
#    list do the operation on itself.

L2 = []
    
for el in L:
   L2.append(el**2)
 
L2



# Dot product


Ar1 = np.array([2,4])
Ar2 = np.array([1,3])

dot = 0

for e,f in zip(Ar1,Ar2):
    dot += e*f
    
dot

#or

dot1 = 0

for i in range(len(Ar1)):
    dot1 += Ar1[i] * Ar2[i]
    
dot1

#or 

np.sum(Ar1*Ar2)

#or

(Ar1 * Ar2).sum()

#or

np.dot(Ar1,Ar2)

#or

Ar1.dot(Ar2)

#or 

Ar1 @ Ar2

np.linalg.norm(Ar1)

L = [[123,2342,123,432]]

print(L)

print(L[0][1])

Arr = np.array([[1,0],[1,99]])

print(Arr[:,0])

Arr.T

np.exp(Arr)
np.exp(L)


