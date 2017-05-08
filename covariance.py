#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:35:47 2017

@author: umberto
"""
import numpy as np

def covariance(matrix, n_looks):
    
    l_pixels = n_looks**2
    rows = np.floor(np.size(matrix[0,0,:,0])/n_looks).astype(np.int16)
    columns = np.floor(np.size(matrix[0,0,0,:])/n_looks).astype(np.int16)
    covmat = np.zeros((3,3,2,rows,columns)).astype(np.int32)
    
    for i in range(rows):
        
        for iii in range(columns):
            
            for j in range (3):
                
                for jjj in range (3):
            
                    a1 = matrix[0,0,3*i+j,3*iii+jjj]
                    a2 = matrix[0,1,i+j,iii+jjj]
                    a3 = matrix[0,2,i+j,iii+jjj]
                    b1 = matrix[1,0,i+j,iii+jjj]
                    b2 = matrix[1,1,i+j,iii+jjj]
                    b3 = matrix[1,2,i+j,iii+jjj]
                    covmat[0,0,0,i,iii] += a1**2 + b1**2 
                    covmat[0,0,1,i,iii] += 0
                    covmat[0,1,0,i,iii] += a1*a2 + b1*b2
                    covmat[0,1,1,i,iii] += a2*b1 - a1*b2 
                    covmat[0,2,0,i,iii] += a1*a3 + b1*b3 
                    covmat[0,2,1,i,iii] += a3*b1 - a1*b3
                    covmat[1,0,0,i,iii] += a1*a2 + b1*b2
                    covmat[1,0,1,i,iii] += a1*b2 - a2*b1
                    covmat[1,1,0,i,iii] += a2**2 + b2**2
                    covmat[1,1,1,i,iii] += 0
                    covmat[1,2,0,i,iii] += a2*a3 + b2*b3
                    covmat[1,2,1,i,iii] += a3*b1 - a1*b3
                    covmat[2,0,0,i,iii] += a1*a2 + b1*b3
                    covmat[2,0,1,i,iii] += a1*b3 - a3*b1
                    covmat[2,1,0,i,iii] += a2*a3 + b2*b3
                    covmat[2,1,1,i,iii] += a2*b3 - a3*b2
                    covmat[2,2,0,i,iii] += a3**2 + b3**2
                    covmat[2,2,1,i,iii] += 0
            
            
            
    
    return covmat