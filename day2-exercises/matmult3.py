#!/usr/bin/python

# Program to multiply two matrices using numpy


import numpy as np

N = 250

# NxN matrix

X = np.random.randint(101, size=(N, N))
    


# Nx(N+1) matrix
Y = np.random.randint(101, size=(N, N+1))
    


#Multplying the matrices

# iterate through rows of X
result = np.matmul(X,Y)


print(result)
