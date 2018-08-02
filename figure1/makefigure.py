#!/usr/bin/python

from astropy.io import fits
from astropy.wcs import WCS
import montage_wrapper as montage
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.patches import Rectangle
import warnings
warnings.filterwarnings("ignore")

# rotate all to north up east left
print "rotating images..."

montage.mRotate("archive/use/FORS2.2015-12-22T06:58:44.396.fits","archive/use/FORS2.2015-12-22T06:58:44.396_rot.fits",rotation_angle=0.,ra=172.15083333333334,dec=-52.93458333333333)
montage.mRotate("archive/use/FORS2.2014-03-15T08:28:09.931.fits","archive/use/FORS2.2014-03-15T08:28:09.931_rot.fits",rotation_angle=0.)

montage.mRotate("archive/use/FORS2.2014-04-02T06:49:52.387.fits","archive/use/FORS2.2014-04-02T06:49:52.387_rot.fits",rotation_angle=0.)
montage.mRotate("archive/use/FORS2.2014-04-23T08:59:28.180.fits","archive/use/FORS2.2014-04-23T08:59:28.180_rot.fits",rotation_angle=0.)
montage.mRotate("archive/use/FORS2.2014-05-12T07:08:26.706.fits","archive/use/FORS2.2014-05-12T07:08:26.706_rot.fits",rotation_angle=0.)
montage.mRotate("archive/use/FORS2.2014-05-29T03:42:33.241.fits","archive/use/FORS2.2014-05-29T03:42:33.241_rot.fits",rotation_angle=0.)
montage.mRotate("archive/use/FORS2.2014-06-19T07:04:34.526.fits","archive/use/FORS2.2014-06-19T07:04:34.526_rot.fits",rotation_angle=0.)

# read the files
print "reading images..."

ngc6326 = fits.open("archive/use/FORS2.2014-03-15T08:28:09.931_rot.fits")
ngc6337 = fits.open("archive/use/FORS2.2014-04-02T06:49:52.387_rot.fits")
mpa1759 = fits.open("archive/use/FORS2.2014-04-23T08:59:28.180_rot.fits")
hen2283 = fits.open("archive/use/FORS2.2014-05-12T07:08:26.706_rot.fits")
pe19    = fits.open("archive/use/FORS2.2014-05-29T03:42:33.241_rot.fits")
hf22    = fits.open("archive/use/FORS2.2014-06-19T07:04:34.526_rot.fits")
fg1     = fits.open("archive/use/FORS2.2015-12-22T06:58:44.396_rot.fits")

# crop
print "cropping images..."

fg1[0].data = fg1[0].data[987:1228,818:1058]
w = WCS(fg1[0].header)
fg1[0].header.update(w[987:1227,818:1058].to_header())

stary=748
starx=1320

ngc6326[0].data = ngc6326[0].data[starx-119:starx+120,stary-119:stary+120]
w = WCS(ngc6326[0].header)
ngc6326[0].header.update(w[starx-119:starx+120,stary-119:stary+120].to_header())

stary=940
starx=909

ngc6337[0].data = ngc6337[0].data[starx-119:starx+120,stary-119:stary+120]
w = WCS(ngc6337[0].header)
ngc6337[0].header.update(w[starx-119:starx+120,stary-119:stary+120].to_header())

stary=937
starx=913

hf22[0].data = hf22[0].data[starx-119:starx+120,stary-119:stary+120]
w = WCS(hf22[0].header)
hf22[0].header.update(w[starx-119:starx+120,stary-119:stary+120].to_header())

stary=935
starx=926

hen2283[0].data = hen2283[0].data[starx-119:starx+120,stary-119:stary+120]
w = WCS(hen2283[0].header)
hen2283[0].header.update(w[starx-119:starx+120,stary-119:stary+120].to_header())

stary=936
starx=910

pe19[0].data = pe19[0].data[starx-119:starx+120,stary-119:stary+120]
w = WCS(pe19[0].header)
pe19[0].header.update(w[starx-119:starx+120,stary-119:stary+120].to_header())

stary=943
starx=927

mpa1759[0].data = mpa1759[0].data[starx-119:starx+120,stary-119:stary+120]
w = WCS(mpa1759[0].header)
mpa1759[0].header.update(w[starx-119:starx+120,stary-119:stary+120].to_header())

# setup

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 8}

matplotlib.rc('font', **font)

# plot
# all cutouts are 240x240
print "plotting fg1..."

plt.figure(1,figsize=(20,10))

f=plt.subplot(247,projection=WCS(fg1[0].header))
f.coords[0].set_major_formatter("hh:mm:ss")

f.imshow(fg1[0].data, cmap='gist_heat', vmin=200, vmax=5000)
f.set_title("Fg 1")
f.grid(color='grey', ls='solid')
r=Rectangle((149.5, -10.), 5.56, 280.,angle=14, edgecolor='yellow', facecolor='none')
f.add_patch(r)
#slit: 100,252,264,418 = 152, 154 = 76,77px
r=Rectangle((137.5, 40.), 5.56, 76, angle=14, edgecolor='blue', facecolor='none', hatch='///')
f.add_patch(r)
r=Rectangle((114.5, 130.), 5.56, 77, angle=14, edgecolor='blue', facecolor='none', hatch='///')
f.add_patch(r)

print "plotting hen2-283..."

f=plt.subplot(244,projection=WCS(hen2283[0].header))
f.coords[0].set_major_formatter("hh:mm:ss")
f.imshow(hen2283[0].data, cmap='gist_heat', vmin=200, vmax=5000, norm=LogNorm())
f.grid(color="grey",ls="solid")
f.set_title("Hen 2-283")
r=Rectangle((113., -10.), 5.56, 280.,edgecolor='yellow', facecolor='none')
f.add_patch(r)
# slit windows = 346,378 = 32 = 16px
r=Rectangle((113.,104.), 5.56, 16, edgecolor='blue', facecolor='none', hatch='///')
f.add_patch(r)

print "plotting hf2-2..."

f=plt.subplot(246,projection=WCS(hf22[0].header))
f.coords[0].set_major_formatter("hh:mm:ss")
f.imshow(hf22[0].data, cmap='gist_heat', vmin=200, vmax=1000)
f.grid(color="grey",ls="solid")
f.set_title("Hf 2-2")
r=Rectangle((113., -10.), 5.56, 280.,edgecolor='yellow', facecolor='none')
f.add_patch(r)
# slit windows 298,359,362,436 = 63px, 64px = 32
r=Rectangle((113., 80.), 5.56, 32., edgecolor='blue', facecolor='none', hatch='///')
f.add_patch(r)
r=Rectangle((113., 124.), 5.56, 32., edgecolor='blue', facecolor='none', hatch='///')
f.add_patch(r)

print "plotting mpa1759..."

f=plt.subplot(243,projection=WCS(mpa1759[0].header))
f.coords[0].set_major_formatter("hh:mm:ss")
f.imshow(mpa1759[0].data, cmap='gist_heat', vmin=200, vmax=2000)
f.grid(color="grey",ls="solid")
f.set_title("MPA 1759")
r=Rectangle((113., -10.), 5.56, 280.,edgecolor='yellow', facecolor='none')
f.add_patch(r)
# slit windows 330,353,368,395 = 23,27 = 12,14 with gap of 7
r=Rectangle((113., 96.), 5.56, 12., edgecolor='blue', facecolor='none', hatch='///')
f.add_patch(r)
r=Rectangle((113., 114.), 5.56, 14., edgecolor='blue', facecolor='none', hatch='///')
f.add_patch(r)

print "plotting ngc6326..."

f=plt.subplot(241,projection=WCS(ngc6326[0].header))
f.coords[0].set_major_formatter("hh:mm:ss")
f.imshow(ngc6326[0].data, cmap='gist_heat', vmin=200, vmax=20000)
f.grid(color="grey",ls="solid")
f.set_title("NGC 6326")
r=Rectangle((240., -10.), 5.56, 380.,angle=45,edgecolor='yellow', facecolor='none')
f.add_patch(r)
# slit window 283,447 = 164 = 82px
r=Rectangle((147.5, 82.), 5.56, 82., angle=45,edgecolor='blue', facecolor='none', hatch='---')
f.add_patch(r)

print "plotting ngc6337..."

f=plt.subplot(242,projection=WCS(ngc6337[0].header))
f.coords[0].set_major_formatter("hh:mm:ss")
f.imshow(ngc6337[0].data, cmap='gist_heat', vmin=200, vmax=5000)
f.grid(color="grey",ls="solid")
f.set_title("NGC 6337")
r=Rectangle((112., -10.), 5.56, 280.,edgecolor='yellow', facecolor='none')
f.add_patch(r)
# slit windows = 232,488 = 256
r=Rectangle((112.,20.), 5.56, 95, edgecolor='blue', facecolor='none', hatch='///')
f.add_patch(r)
r=Rectangle((112.,125.), 5.56, 95, edgecolor='blue', facecolor='none', hatch='///')
f.add_patch(r)

print "plotting pe1-9..."

f=plt.subplot(245,projection=WCS(pe19[0].header))
f.coords[0].set_major_formatter("hh:mm:ss")
f.imshow(pe19[0].data, cmap='gist_heat', vmin=200, vmax=1500)
f.grid(color="grey",ls="solid")
f.set_title("Pe 1-9")
f.set_xlabel("Right Ascension")
f.set_ylabel("Declination")
r=Rectangle((112., -10.), 5.56, 280.,edgecolor='yellow', facecolor='none')
f.add_patch(r)
# slit window = 325,397 = 72 = 36px
r=Rectangle((112.,102.), 5.56, 36, edgecolor='blue', facecolor='none', hatch='///')
f.add_patch(r)

print "saving..."

plt.savefig("images.png",bbox_inches='tight')
