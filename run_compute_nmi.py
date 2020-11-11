from compute_nmi_final import compute_nmi

'''
This script computes neural maturity index (NMI), which is the spatial correlation between each individual activation map and a group-level activation map (reference)

dataListFname contains all the individual stats file names.

refDataFname is the reference adult group-level brain stats map thresholded. This reference map is thresholded (p<0.01, FDR corrected) and include both significantly activated and de-activated voxels.

maskFname is the grey matter mask. In this analysis, we excluded sensory and motor regions in the grey matter mask to avoid over- or under- estimation of activation map correlation due to simliar or different sensorimotor setting between different studies.

'''

dataListFname = ''
refDataFname = ''
maskFname = ''

compute_nmi(dataListFname, refDataFname, maskFname)

