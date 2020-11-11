Python scripts for computing neural maturity index (NMI)

Cai, W.; Duberg, K.; Padmanabhan, A.; Rehert, R.; Bradley, T.; Carron, V.; Menon, V. Hyperactivity insula-basal-ganglia pathway and adult-like maturity of global brain responses predict inhibitory control in children. 


*** Usage ***
python version: 2.7
python module: sys, numpy, pandas, nibabel, math and csv

There are two scripts in the folder: run_compute_nmi.py and compute_nmi_final.py

To run the script: python run_compute_nmi.py

This script takes three arguments: dataListFname, refDataFname, and maskFname 

dataListFname contains all the individual stats file names.

refDataFname is the reference adult group-level brain stats map thresholded. This reference map is thresholded (p<0.01, FDR corrected) and include both significantly activated and de-activated voxels.

maskFname is the grey matter mask. In this analysis, we excluded sensory and motor regions in the grey matter mask to avoid over- or under- estimation of activation map correlation due to simliar or different sensorimotor setting between different studies.

If you have questions about the usage and related issues, please write me an email: wdcai@stanford.edu

Happy computing!

Weidong Cai

2018-12-29
