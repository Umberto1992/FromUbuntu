"""
Created on Mon May  1 17:40:15 2017

@author: umberto
"""
######################################################################
#
# I use this script to average HV and VH layers and save in a new file
#
######################################################################
import numpy as np

# Load the file the layers we want to average here
layer_HV = np.load('IceImg02FullHV.npy')
layer_VH = np.load('IceImg02FullVH.npy')

final_layer = np.rint((layer_HV+layer_VH)/2)

int_layer = final_layer.astype(np.int16)

# Save the averaged layer in a new file
np.save('IceImg02FullVH+HV', int_layer)
