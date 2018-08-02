This repository containts data reduction and analysis scripts, which should allow anyone who wants to do so to reproduce the results presented in Wesson et al. 2018 (arXiv: 1807.09272). If you try it and encounter any problems or discrepancies, please let me know.

# 1: Get the raw data

Get the raw data used in the paper from the ESO archive:

http://archive.eso.org/wdb/wdb/eso/sched_rep_arc/query?progid=093.D-0038(A)
http://archive.eso.org/wdb/wdb/eso/sched_rep_arc/query?progid=096.D-0080(A)

# 2: Reduce the data

Use ESO REFLEX

http://archive.eso.org/wdb/wdb/eso/sched_rep_arc/query?progid=096.D-0080(A)

# 3: Extract integrated and spatially resolved spectra

# 4: Measure and identify the emission lines

# 5: Analyse the line lists

# 6: Figures

* Figure 1 was generated from our acquisition images, using the script figure1/makefigure.py
* Figure 2 was made from the extracted 1D spectra generated in step 3, using the script figure2/plot_alfafits.sh.
* Figure 3: the script looks for a file containing the observed ratios and their uncertainties, prepared manually, and the tabulated line ratios which come with NEAT
* Figures 4-7 were made from the spatially extracted 1D spectra generated in step 3, using the script figure4/plot.sh 
* Figure 9 was made using a PHP script, not yet uploaded
* Figure 10 was made using scripts in the folder figure10/; "make && ./distrib && ./plot.prg" will compile the code, generate the synthetic distribution, and plot it together with the actual distribution which is in a file compiled by hand.

# 7: Tables
