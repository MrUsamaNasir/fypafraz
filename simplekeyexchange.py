#!usr/bin/env python

# Please note that where used % denotes the modulo operator

#As defined in section 2 of the paper a robust extractor takes in input
#an integer modulo q, a signal sigma defined in the 'signal' function and a prime number q

from random import *
import numpy

def robust_extractor(x, sigma, q):
    return (x + sigma*((q-1)/2)%q)%2

#b will determine what type of signal function you require, inputs are x as an integer mod q, q as a prime number and b (signal case)
def signal_functions(x, b, q):
    if b == 0:
        if x > -q/4 or x < q/4:
            return 0
        else:
            return 1
    elif b == 1:
        if x > -q/4 + 1 or x < q/4 + 1:
            return 0
        else:
            return 1

#This function makes an n x n matrix of integers mod q
def generate_matrix_M(n, q):

    #Declare a matrix here:
    M = numpy.zeros((n,n))

    #Build the matrix here:
    for i in range(0,n):
        for j in range(0,n):
            M[i][j] = randint(0,q-1)
    return M

def generate_gaussian_vector(n,q):
    alpha = (1/float(n))**3
    mu = 0 #page 5 of the paper
    sigma = alpha*q
    return numpy.random.normal(mu,sigma,n)

def main():
    print("This part of the program requires you to specify the public parameters:")
    n = int(input("Dimensions of M (must be an n x n) so please enter n: "))
    q = int(input("Please enter a prime number greater than 2, this is q: "))

    #M is a matrix of integers mod q and has dimensions n x n
    M = generate_matrix_M(n,q)
    eA = generate_gaussian_vector(n,q)
    sA = generate_gaussian_vector(n,q)
    

#initialisation
if __name__ == "__main__":
    main()