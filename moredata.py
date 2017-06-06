#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 10:58:11 2017

@author: umberto
"""

###########################################################
#
# This script is useful to create more data, rotating and flipping 
# the orignal NxN images
#
#############################################################

import numpy as np

dataset = np.load('DataTrain003by3Img01.npy') #here I load the file we created in "cutdataset"

# Here I extract the information about the dimension of the array
samples = np.size(dataset[:,0,0,0])
cov_vector = np.size(dataset[0,0,0,:])
imagesize = np.size(dataset[0,:,0,0])
moredata = np.zeros((samples*8,imagesize,imagesize,cov_vector),dtype=np.int32)

# I copy all the elements of the previous dataset in the first fragment of the array
moredata[0:samples,:,:,:] = np.copy(dataset)

# Here I flip the original samples
for i in range(samples):
    
    for j in range(cov_vector):
        
        moredata[samples+i,:,:,j] = np.fliplr(dataset[i,:,:,j])
        
# Here I rotate 90 degrees the original image 
for i in range(samples):
    
    for j in range(cov_vector):
        
        moredata[samples*2+i,:,:,j] = np.rot90(dataset[i,:,:,j])
        
# Here I rotate 180 degrees the original image (by rotating the previous portion)         
for i in range(samples):
    
    for j in range(cov_vector):
        
        moredata[samples*3+i,:,:,j] = np.rot90(moredata[samples*2+i,:,:,j])
        
# Here I rotate 270 degrees the original image 
for i in range(samples):
    
    for j in range(cov_vector):
        
        moredata[samples*4+i,:,:,j] = np.rot90(moredata[samples*3+i,:,:,j])

# Here I rotate 90 degrees the flipped image
for i in range(samples):
    
    for j in range(cov_vector):
        
        moredata[samples*5+i,:,:,j] = np.rot90(moredata[samples+i,:,:,j])
        
# Here I rotate 180 degrees the flipped image        
for i in range(samples):
    
    for j in range(cov_vector):
        
        moredata[samples*6+i,:,:,j] = np.rot90(moredata[samples*5+i,:,:,j])
        
# Here I rotate 270 degrees the flipped image
for i in range(samples):
    
    for j in range(cov_vector):
        
        moredata[samples*7+i,:,:,j] = np.rot90(moredata[samples*6+i,:,:,j])
        

np.save('DataTest003by3Img01C', moredata)

        
        
        