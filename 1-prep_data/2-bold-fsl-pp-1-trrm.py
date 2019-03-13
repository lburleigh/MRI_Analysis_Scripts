#!/usr/bin/env python

# Script for removing first dummy volumes from functional EPI data
# Execute via:
# ipython bold-fsl-pp-1-trrm.py

import numpy as np
import os
import glob

## Study directory
studydir = '/mnt/40TB-raid6/Experiments/FCTM_S/FCTM_S_Data/Analyses'


## number of TRs to remove
trrm=3

## Find raw EPI nii files
subdirs=glob.glob('%s/1[0-9][0-9][0-9][0-9]/func/B_hab_[0-9].nii.gz'%(studydir))
#subdirs=glob.glob('%s/18301/func/A_hab_[0-9].nii.gz'%(studydir))

for s in np.arange(0,len(subdirs)):
	## Remove nii.gz
	cur_bold_no_nii = subdirs[s][:-7]
	print(cur_bold_no_nii)
	os.system("fslroi %s %s_trrm %i 300"%(cur_bold_no_nii, cur_bold_no_nii,trrm)) #save the newly trimmed files, add _trrm to the end of the file name
