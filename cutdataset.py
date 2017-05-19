#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:29:59 2017

@author: umberto
"""

import numpy as np

samdim = 224 # DImension NxN of the sample

fullcov = np.load("img00Cov3by3S.npy").astype(np.int16)

vectordim = np.size(fullcov[0,0,:])

testdimx = np.size(fullcov[0,:,0])/(samdim*3)
testdimy = np.size(fullcov[:,0,0])/samdim

testsamples = np.zeros(((testdimx*testdimy),samdim,samdim,vectordim)).astype(np.int32)              
                  
for i in range (testdimx):
    for j in range (testdimy):
        
        testsamples[i*testdimy+j,:,:,:] = fullcov[j*samdim:((j+1)*samdim),i*samdim:((i+1)*samdim)]
 
np.save("DataTest003by3Img00",testsamples)       

traindimx = ((np.size(fullcov[0,:,0]) - (testdimx*samdim)) - samdim)/(samdim/2) + 1 # How many overlapped samples 
traindimy = (np.size(fullcov[:,0,0]) - samdim)/(samdim/2) + 1  #                
                   
trainsamples = np.zeros(((traindimx*traindimy), samdim, samdim, vectordim)).astype(np.int32)

for i in range (traindimx):
    for j in range (traindimy):
        vert = np.floor((j/float(2))*samdim).astype(np.int16)
        vert1 = np.floor(((j/float(2))+1)*samdim).astype(np.int16)
        hor = np.floor((i/float(2))*samdim + (samdim*testdimx)).astype(np.int16)
        hor1 = np.floor((((i/float(2))+1)*samdim) + (samdim*testdimx)).astype(np.int16)
        trainsamples[i*traindimy+j,:,:,:] = fullcov[vert:vert1,hor:hor1,:]

np.save("DataTrain003by3Img00",trainsamples)        