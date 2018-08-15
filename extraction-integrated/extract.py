from astropy.io import fits
import numpy as np
import scipy.signal
import sys
import glob
import math

# read FITS file and get useful keywords:

def getdata(filename, skywindows, nebularwindows, outputdir="python/"):

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

    outfile=outputdir+filename[0:-5]+"_1d.txt"
    np.savetxt(outfile,spectrum)

#    outfile=outputdir+filename[0:-5]+"_sky_fitted.fits"
#    hdu = fits.PrimaryHDU(sky)
#    hdu.writeto(outfile,clobber=True)

skywindows=(145,291,468,881)
nebularwindows=(310,355,365,410)
getdata("A41Blue_clean.fits",skywindows,nebularwindows)

# A41
skywindows=(10,110,770,900)
nebularwindows=(368,417)
getdata("A41Blue_clean.fits",skywindows,nebularwindows)
getdata("A41Red_clean.fits",skywindows,nebularwindows)

# A65
skywindows=(1,10,860,945)
nebularwindows=(364,624)
getdata("A65Blue_clean.fits",skywindows,nebularwindows)
getdata("A65Red_clean.fits",skywindows,nebularwindows)

# BMP1801
skywindows=(149,220,572,793)
nebularwindows=(290,430)
getdata("BMP1801Blue_clean.fits",skywindows,nebularwindows)

# Fg1
skywindows=(6,30,700,1000)
nebularwindows=(100,252,264,418)
getdata("Fg1Blue_clean.fits",skywindows,nebularwindows)
getdata("Fg1Red_clean.fits",skywindows,nebularwindows)

# H2-29
skywindows=(217,317,467,588)
nebularwindows=(342,381)
getdata("H2-29Blue_clean.fits",skywindows,nebularwindows)
getdata("H2-29Red_clean.fits",skywindows,nebularwindows)

# HaTr4
skywindows=(80,213,515,640)
nebularwindows=(361,465)
getdata("HaTr4Blue_clean.fits",skywindows,nebularwindows)
getdata("HaTr4Red_clean.fits",skywindows,nebularwindows)

# Hen2-11
skywindows=(18,100,670,800)
nebularwindows=(366,658)
getdata("Hen2-11Blue_clean.fits",skywindows,nebularwindows)
getdata("Hen2-11Red_clean.fits",skywindows,nebularwindows)

# Hen2-283
skywindows=(50,228,454,540)
nebularwindows=(346,378)
getdata("Hen2-283Blue_clean.fits",skywindows,nebularwindows)
getdata("Hen2-283Red_clean.fits",skywindows,nebularwindows)

# Hen2-428
skywindows=(40,260,500,740)
nebularwindows=(300,450)
getdata("Hen2-428Blue_clean.fits",skywindows,nebularwindows)
getdata("Hen2-428Red_clean.fits",skywindows,nebularwindows)

# Hf2-2
skywindows=(61,175,517,712)
nebularwindows=(298,436)
getdata("Hf2-2Blue_clean.fits",skywindows,nebularwindows)
getdata("Hf2-2Red_clean.fits",skywindows,nebularwindows)

# K1-2
skywindows=(15,100,700,822)
nebularwindows=(428,668)
getdata("K1-2Blue_clean.fits",skywindows,nebularwindows)
getdata("K1-2Red_clean.fits",skywindows,nebularwindows)

# K6-34
skywindows=(126,208,558,612)
nebularwindows=(332,384)
getdata("K6-34Blue_clean.fits",skywindows,nebularwindows)
getdata("K6-34Red_clean.fits",skywindows,nebularwindows)

# Lo16
skywindows=(44,100,600,820)
nebularwindows=(165,580)
getdata("Lo16Blue_clean.fits",skywindows,nebularwindows)
getdata("Lo16Red_clean.fits",skywindows,nebularwindows)

# M2-19
skywindows=(216,284,410,526)
nebularwindows=(322,400)
getdata("M2-19Blue_clean.fits",skywindows,nebularwindows)
getdata("M2-19Red_clean.fits",skywindows,nebularwindows)

# M3-16
skywindows=(232,312,404,560)
nebularwindows=(329,392)
getdata("M3-16Blue_clean.fits",skywindows,nebularwindows)
getdata("M3-16Red_clean.fits",skywindows,nebularwindows)

# MPA1508
skywindows=(38,138,490,860)
nebularwindows=(330,353,368,395)
getdata("MPA1508Blue_clean.fits",skywindows,nebularwindows)
getdata("MPA1508Red_clean.fits",skywindows,nebularwindows)

# MPA1759
skywindows=(100,219,430,591)
nebularwindows=(322,397)
getdata("MPA1759Blue_clean.fits",skywindows,nebularwindows)
getdata("MPA1759Red_clean.fits",skywindows,nebularwindows)

# NGC2346
skywindows=(22,70,700,960)
nebularwindows=(290,350,370,450)
getdata("NGC2346Blue_clean.fits",skywindows,nebularwindows)
getdata("NGC2346Red_clean.fits",skywindows,nebularwindows)

# NGC6026
skywindows=(10,160,560,822)
nebularwindows=(374,520)
getdata("NGC6026Blue_clean.fits",skywindows,nebularwindows)
getdata("NGC6026Red_clean.fits",skywindows,nebularwindows)

# NGC6326
skywindows=(9,103,699,953)
nebularwindows=(283,447)
getdata("NGC6326Blue_clean.fits",skywindows,nebularwindows)
getdata("NGC6326Red_clean.fits",skywindows,nebularwindows)

# NGC6337
skywindows=(22,70,738,934)
nebularwindows=(366,466)
getdata("NGC6337Blue_clean.fits",skywindows,nebularwindows)
getdata("NGC6337Red_clean.fits",skywindows,nebularwindows)

# Pe1-9
skywindows=(189,297,685,755)
nebularwindows=(325,397)
getdata("Pe1-9Blue_clean.fits",skywindows,nebularwindows)
getdata("Pe1-9Red_clean.fits",skywindows,nebularwindows)

# PHR1756
skywindows=(25,290,550,674)
nebularwindows=(388,476)
getdata("PHR1756Blue_clean.fits",skywindows,nebularwindows)
getdata("PHR1756Red_clean.fits",skywindows,nebularwindows)

# PHR1804
skywindows=(62,230,580,760)
nebularwindows=(364,440)
getdata("PHR1804Blue_clean.fits",skywindows,nebularwindows)
getdata("PHR1804Red_clean.fits",skywindows,nebularwindows)

# PM1-23
skywindows=(20,250,500,760)
nebularwindows=(375,415)
getdata("PM1-23Blue_clean.fits",skywindows,nebularwindows)
getdata("PM1-23Red_clean.fits",skywindows,nebularwindows)

# PM1-23 new

nebularwindows=(370,410)
getdata("PM1-23Blue_clean.fits",skywindows,nebularwindows)

# Sp1
skywindows=(10,40,774,930)
nebularwindows=(426,506)
getdata("Sp1Blue_clean.fits",skywindows,nebularwindows)
getdata("Sp1Red_clean.fits",skywindows,nebularwindows)

# Sab41
skywindows=(14,70,550,750)
nebularwindows=(294,438)
getdata("Sab41Blue_clean.fits",skywindows,nebularwindows)
getdata("Sab41Red_clean.fits",skywindows,nebularwindows)

#PNG - blue and red in different positions
skywindows=(8,30,365,940)
nebularwindows=(53,99,110,167)
getdata("PNG2837-051_new_Blue_clean.fits",skywindows,nebularwindows)

skywindows=(8,30+136,365+136,1034)
nebularwindows=(53+136,99+136,110+136,167+136)
getdata("PNG2837-051_new_Red_clean.fits",skywindows,nebularwindows)
