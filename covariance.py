#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:35:47 2017

@author: umberto
"""
import numpy as np

def covariance(matrix, n_looks):
    
    l_pixels = n_looks**2
    rows = np.floor(np.size(matrix[0,0,:,0])/n_looks)
    columns = np.floor(np.size(matrix[0,0,0,:])/n_looks)
    covmat = np.zeros((3,3,2,rows,columns))
    
    for i in range(rows):
        
        for iii in range(columns):
            
            covmat[0,0,0,i,iii] =
            covmat[0,0,1,i,iii] =
            covmat[1,0,0,i,iii] =
            
    
    return covmat