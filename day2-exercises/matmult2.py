#!/usr/bin/python

# Program to multiply two matrices using numpy


import numpy as np

N = 250

# NxN matrix
X = 0
def createX(N):
    X = np.random.randint(101, size=(N, N))
    
    return X

# Nx(N+1) matrix
Y = 0
def createY(N):
    Y = np.random.randint(101, size=(N, N+1))
    
    return Y

#Multplying the matrices
result = 0
def createM(X,Y):
    # iterate through rows of X
    result = np.matmul(X,Y)
    
    return result
