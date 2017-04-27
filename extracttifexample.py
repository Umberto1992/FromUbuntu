# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-


import gdal, gdalconst
from scipy.cluster.vq import *
import matplotlib.pyplot as plt

# Read SAR image into Numpy Array
filename = "//home/umberto/Downloads/RS2_20150725_043228_0004_FQ26_HHVVHVVH_SLC_410799_3946_11592432/imagery_HH.tif"
sarfile = gdal.Open(filename, gdalconst.GA_ReadOnly)
sarraster = sarfile.ReadAsArray()