"""
Created on Tue May 16 14:07:21 2017

@author: umberto
"""

##########################################################
#
# This script take in input a SAR image, composed by 3 layers (HH,VH+HV,VV),
# and a number which tells how large should be the multi-look window
# that will average the values of the covariance matrix over n^2 pixels.
# Building this covariance matrix we are assuming reflexion simmetry,
# it means that we we'll have 4 real values and 1 imaginary value.
# To make the algorithm simpler and faster, instead of implementing a  3x3 vector,
# we use a 5x1 vector with just the values that are not 0.
#
###########################################################

############################################################
#
# covariance(matrix, n_looks)
# Input:
#  - n_looks ---> multi-look factor
#  - matrix[a,b,c,d] ---> SAR image
#     - a: 2 elements vector, real and imaginary part
#     - b: quad-pol channels (HH,HV+VH,VV)
#     - c: image's rows
#     - d: image's columns
#
# Output:
#  - covmat[e,f,g] ---> covariance matrix
#       e: covariance matrix rows
#       f: covariace matrix columns
#       g: elements of cov elements for pixels after simmetry assumptions
#       g0,g1, g2 --> real parts of the diagonal
#       g3 --> real part of the other corners
#       g4 --> imaginary part of the other corners
#
###############################################

import numpy as np

def covariance(matrix, n_looks):
    
# Reading informations by the data sent to the function
    l_pixels = n_looks**2
    rows = np.floor(np.size(matrix[0,0,:,0])/n_looks).astype(np.int16)
    columns = np.floor(np.size(matrix[0,0,0,:])/n_looks).astype(np.int16)
    covmat = np.zeros((rows,columns,5)).astype(np.int64) #array which will go back to the main script
    counter = 0 #this is used just to display on the command windows the progression
    
    for i in range(rows):
        
        for iii in range(columns):
            
            for j in range (n_looks):
                
                for jjj in range (n_looks):
                    
                    # Loading values from the scattering vectors
                    a1 = matrix[0,0,n_looks*i+j,n_looks*iii+jjj]
                    a2 = matrix[0,1,n_looks*i+j,n_looks*iii+jjj]
                    a3 = matrix[0,2,n_looks*i+j,n_looks*iii+jjj]
                    b1 = matrix[1,0,n_looks*i+j,n_looks*iii+jjj]
                    b2 = matrix[1,1,n_looks*i+j,n_looks*iii+jjj]
                    b3 = matrix[1,2,n_looks*i+j,n_looks*iii+jjj]
                    
                    # Computation of necessary values
                    covmat[i,iii,0] += (a1**2 + b1**2)/l_pixels
                    covmat[i,iii,1] += (a2**2 + b2**2)/l_pixels
                    covmat[i,iii,2] += (a3**2 + b3**2)/l_pixels
                    covmat[i,iii,3] += (a1*a3 + b1*b3)/l_pixels
                    covmat[i,iii,4] += (a3*b1 - a1*b3)/l_pixels
            
        print('Iteration number:' + repr(counter))
        counter += 1
            
    
    return covmat