#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 17:40:15 2017

@author: umberto
"""
#I use this script to average HV and VH layers and save in a new file

import numpy as np

layer_HV = np.load('img00FullHV.npy')
layer_VH = np.load('img00FullVH.npy')

final_layer = np.rint((layer_HV+layer_VH)/2)

int_layer = final_layer.astype(np.int16)

np.save('img00FullVH+HV', int_layer)
