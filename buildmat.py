"""
Created on Wed May  3 12:10:07 2017

@author: umberto
"""
######################################################
#
# This script creates a single array containing 3 layers 
# and calls the function to build covariance matrices, 
# the user has to specify which multi-look factor he wants to use
#
#######################################################

import numpy as np
import covariance as cov # Import of the function written by myself

# Load the signle layers here
layer_HH = np.load('IceImg02FullHH.npy')
layer_VV = np.load('IceImg02FullVV.npy')
layer_HVVH = np.load('IceImg02FullVH+HV.npy')

rows = np.size(layer_HH[0,:,0]) # N rows of the image
cols = np.size(layer_HH[0,0,:]) # N columns of the image

full_image = np.zeros((2,3,rows,cols)).astype(np.int32) # This matrix will collect all layers in one array

full_image[:,0,:,:] = layer_HH
full_image[:,1,:,:] = layer_HVVH
full_image[:,2,:,:] = layer_VV

L = 7 #multi-look factor
          
MatrixC = cov.covariance(full_image,L)

# Save the covariance matrix in a new file
np.save('IceImg02Cov7by7S', MatrixC)

    
    
    