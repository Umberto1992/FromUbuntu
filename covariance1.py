#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 14:07:21 2017

@author: umberto
"""

import numpy as np

def covariance(matrix, n_looks):
    
    l_pixels = n_looks**2
    rows = np.floor(np.size(matrix[0,0,:,0])/n_looks).astype(np.int16)
    columns = np.floor(np.size(matrix[0,0,0,:])/n_looks).astype(np.int16)
    covmat = np.zeros((rows,columns,5)).astype(np.int64)
    counter = 0
    
    for i in range(rows):
        
        for iii in range(columns):
            
            for j in range (n_looks):
                
                for jjj in range (n_looks):
                    
                    a1 = matrix[0,0,n_looks*i+j,n_looks*iii+jjj]
                    a2 = matrix[0,1,n_looks*i+j,n_looks*iii+jjj]
                    a3 = matrix[0,2,n_looks*i+j,n_looks*iii+jjj]
                    b1 = matrix[1,0,n_looks*i+j,n_looks*iii+jjj]
                    b2 = matrix[1,1,n_looks*i+j,n_looks*iii+jjj]
                    b3 = matrix[1,2,n_looks*i+j,n_looks*iii+jjj]
                    covmat[i,iii,0] += (a1**2 + b1**2)/l_pixels
                    covmat[i,iii,1] += (a2**2 + b2**2)/l_pixels
                    covmat[i,iii,2] += (a3**2 + b3**2)/l_pixels
                    covmat[i,iii,3] += (a1*a3 + b1*b3)/l_pixels
                    covmat[i,iii,4] += (a3*b1 - a1*b3)/l_pixels
            
        print('Iteration number:' + repr(counter))
        counter += 1
            
    
    return covmat