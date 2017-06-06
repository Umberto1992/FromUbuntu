##################################################
#
# Script to extract matrices from .tif files and 
# save them in a .npy file
#
##################################################
import gdal, gdalconst
import numpy as np


# This is the path of the .tif file which we want to extract
filename = "/home/umberto/Downloads/RS2_20110412_151525_0004_FQ20_HHVVHVVH_SLC_128082_1705_5221524/imagery_VV.tif"

# Read SAR image into Numpy Array
sarfile = gdal.Open(filename, gdalconst.GA_ReadOnly)
sarraster = sarfile.ReadAsArray()

# This command is saving the image on .npy file layer by layer 
np.save('IceImg02FullVV', sarraster)


