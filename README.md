This repository containts data reduction and analysis scripts, which should allow anyone who wants to do so to reproduce the results presented in Wesson et al. 2018 (arXiv: 1807.09272). If you try it and encounter any problems or discrepancies, please let me know.

# 1: Get the raw data

Get the raw data used in the paper from the ESO archive:

http://archive.eso.org/wdb/wdb/eso/sched_rep_arc/query?progid=093.D-0038(A)
http://archive.eso.org/wdb/wdb/eso/sched_rep_arc/query?progid=096.D-0080(A)

# 2: Reduce the data

## We used STARLINK software to do the data reduction
## Cosmic ray cleaning was carried with both /bclean/ and this python implementation of /LAcosmic/: http://obswww.unige.ch/~tewes/cosmics_dot_py/

# 3: Extract integrated and spatially resolved spectra

Run the following scripts:

* extract-integrated/extract.py
* extraction-spatial/extract_fg1_final_spatial.py
* extraction-spatial/extract_hf2-2_final_spatial.py
* extraction-spatial/extract_ngc6326_final_spatial.py
* extraction-spatial/extract_ngc6337_final_spatial.py

# 4: Measure and identify the emission lines

Run ALFA on the blue spectra, take the measured H beta flux and run on the red spectra, normalising to that value. Scale as described in the paper. ALFA version 1.0.123 was used for the measurements presented in the paper - (revision g6d7fe4, https://github.com/rwesson/ALFA/tree/6d7fe4b94fcf3fb9686a12269e2e749a3f6565d5).

# 5: Analyse the line lists

Run NEAT on the combined line lists. Version 2.1.25 was used for the analysis presented in the paper (revision f86bb25, https://github.com/rwesson/NEAT/tree/f86bb251d8909ad41c07a67f712471a63cf1ee24)

# 6: Figures

* Figure 1 was generated from our acquisition images, using the script figure1/makefigure.py
* Figure 2 was made from the extracted 1D spectra generated in step 3, using the script figure2/plot_alfafits.sh.
* Figure 3: the script looks for a file containing the observed ratios and their uncertainties, prepared manually, and the tabulated line ratios which come with NEAT
* Figures 4-7 were made from the spatially extracted 1D spectra generated in step 3, using the script figure4/plot.sh 
* Figure 9 was made using a PHP script, not yet uploaded
* Figure 10 was made using scripts in the folder figure10/; "make && ./distrib && ./plot.prg" will compile the code, generate the synthetic distribution, and plot it together with the actual distribution which is in a file compiled by hand.
* Figure 11 was generated using the script figure11/plot_adf_period.sh. This script contains hard-coded values for adfs rather than inheriting values from step 5.
* Figure 12 was generated from lists of adfs and central star classifications from the literature. The script figure12/get.sh creates lists of adfs for various different types of nebula and central star classification; the script figure12/qqplot.R generates QQ plots.
