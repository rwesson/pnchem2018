#!/usr/bin/python

from astropy.io import fits
import numpy as np
import scipy.signal
import sys
import glob
import math

# read FITS file and get useful keywords:

def getdata(filename, skywindows, nebularwindows, outputdir="python/final/NGC6337/spatial/"):

    print "extracting spectrum from "+filename

    hdulist = fits.open("clean/"+filename)
    getdata.data = hdulist[0].data
    header = hdulist[0].header
    getdata.crval = header["CRVAL1"]

    try:
        getdata.cd1_1 = header["CD1_1"]
    except:
        getdata.cd1_1 = header["CDELT1"]

    getdata.bin_y = header["HIERARCH ESO DET WIN1 BINY"]
    getdata.crpix = header["CRPIX1"]

    # define output spectrum size
    spectrum = np.zeros(shape=(getdata.data.shape[1],2))

    # calculate wavelengths
    spectrum[:,0] = [getdata.crval+(x-getdata.crpix+1)*getdata.cd1_1 for x in range(getdata.data.shape[1])]

    # fit polynomial to background in sky windows
    if len(skywindows)%2==1:
        print "sky windows not properly defined"
        sys.exit()      
    if len(nebularwindows)%2==1:
        print "nebular windows not properly defined"
        sys.exit()      

    sky=np.copy(getdata.data)

    sky[0:skywindows[0],:] = 0.
    sky[skywindows[1]:skywindows[2],:] = 0
    sky[skywindows[3]:,:] = 0

#    outfile=outputdir+filename[0:-5]+"_sky_windows.fits"
#    hdu = fits.PrimaryHDU(sky)
#    hdu.writeto(outfile,clobber=True)

    # median filter the sky with a kernel size 7x1

    sky=scipy.signal.medfilt(sky,(7,1))

    xrows = np.arange(sky.shape[0])
    x=np.append(np.arange(skywindows[0],skywindows[1]), np.arange(skywindows[2],skywindows[3]))

    for col in range(sky.shape[1]):
        y=sky[x,col]
        pfit = np.polyfit(x, y, 2) 
        sky[:,col] = np.polyval(pfit, xrows)

    skysub = getdata.data - sky

#    outfile=outputdir+filename[0:-5]+"_sky_subtracted.fits"
#    hdu = fits.PrimaryHDU(skysub)
#    hdu.writeto(outfile,clobber=True)

# remove data outside nebular windows

    start=0
    for i in range(0,len(nebularwindows),2):
        skysub[start:nebularwindows[i],:]=0.0
        start=nebularwindows[i+1]
    skysub[start:,:]=0.0

# sum up what is left

    spectrum[:,1] = np.sum(skysub,axis=0)

# trim ends

    spectrum = spectrum[20:-20]

# save to file

    outfile=outputdir+filename[0:-5]+"_"+"%03d"%(nebularwindows[0])+"_"+"%03d"%(nebularwindows[1])+"_1d.txt"
    np.savetxt(outfile,spectrum)

#    outfile=outputdir+filename[0:-5]+"_sky_fitted.fits"
#    hdu = fits.PrimaryHDU(sky)
#    hdu.writeto(outfile,clobber=True)

# NGC6337
skywindows=(22,70,738,934)
for x in (232,264,296,328,360,392,424,456,488):
    nebularwindows=(x,x+31)
    getdata("NGC6337Blue_clean.fits",skywindows,nebularwindows)
    getdata("NGC6337Red_clean.fits",skywindows,nebularwindows)
