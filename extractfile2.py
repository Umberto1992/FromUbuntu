#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 18:59:32 2017

@author: umberto
"""

from tifffile import TiffFile

filename = "//home/umberto/Downloads/RS2_20150725_043228_0004_FQ26_HHVVHVVH_SLC_410799_3946_11592432/imagery_VV.tif"

with TiffFile(filename) as tif:
    img = tif.asarray()
    
