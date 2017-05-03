#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 12:10:07 2017

@author: umberto
"""
import numpy as np

layer_HH = np.load('img00FullHH.npy')
layer_VV = np.load('img00FullVV.npy')
layer_HVVH = np.load('img00FullVH+HV.npy')

full_image = np.zeros((2,3,5687,4101)).astype(np.int16)

full_image[:,0,:,:] = layer_HH
full_image[:,1,:,:] = layer_HVVH
full_image[:,2,:,:] = layer_VV

full_image_con = full_image
full_image_con[1,:,:,:] = -full_image[1,:,:,:]

#for i in range(1):
    
    
    