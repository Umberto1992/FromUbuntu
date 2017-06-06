"""
Created on Thu May 18 10:29:59 2017

@author: umberto
"""

##########################################################################
#
# This script cut the dataset in test (circa 30%) and training (circa 70%)
# and save them in 2 different files. The image is also cutted in NxN smaller
# windows to be prepared to feed the Networks.
#
###########################################################################

import numpy as np

samdim = 224 # Dimension NxN of the sample

# Loading the cov mat that we want to cut in sub-samples
fullcov = np.load("img01Cov3by3S.npy").astype(np.int16)

# Here I read the informations about the size of the image
vectordim = np.size(fullcov[0,0,:])

############################################################################

# Here we extract the samples for the test

# I calculate here the dimension of the test (<=33% of the image) portion
testdimx = np.size(fullcov[0,:,0])/(samdim*3)
testdimy = np.size(fullcov[:,0,0])/samdim
testsamples = np.zeros(((testdimx*testdimy),samdim,samdim,vectordim)).astype(np.int32)              

# These for loops cut the image and put the samples in the new array
          
for i in range (testdimx):
    for j in range (testdimy):
        
        testsamples[i*testdimy+j,:,:,:] = fullcov[j*samdim:((j+1)*samdim),i*samdim:((i+1)*samdim)]
 
np.save("DataTest003by3Img01",testsamples)       

############################################################################

# Here we extract the samples for the training

# Calculate how many samples we can get from the remaining part of the image

traindimx = ((np.size(fullcov[0,:,0]) - (testdimx*samdim)) - samdim)/(samdim/2) + 1 # How many overlapped horizontal samples 
traindimy = (np.size(fullcov[:,0,0]) - samdim)/(samdim/2) + 1 # How many overlapped vertical samples
                   
trainsamples = np.zeros(((traindimx*traindimy), samdim, samdim, vectordim)).astype(np.int32)

# These for loops cut the image and put the samples in the new array

for i in range (traindimx):
    for j in range (traindimy):
        vert = np.floor((j/float(2))*samdim).astype(np.int16)
        vert1 = np.floor(((j/float(2))+1)*samdim).astype(np.int16)
        hor = np.floor((i/float(2))*samdim + (samdim*testdimx)).astype(np.int16)
        hor1 = np.floor((((i/float(2))+1)*samdim) + (samdim*testdimx)).astype(np.int16)
        trainsamples[i*traindimy+j,:,:,:] = fullcov[vert:vert1,hor:hor1,:]

np.save("DataTrain003by3Img01",trainsamples)        