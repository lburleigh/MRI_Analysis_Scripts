#!/usr/bin/env python
 
 
import glob
import os
import fnmatch
 
  
path = '/mnt/40TB-raid6/Experiments/FCTM_S/FCTM_S_Data/Analyses'
 
boldfiles = glob.glob('%s/1[0-9][0-9][0-9][0-9]/func/*task*.nii.gz'%(path))
 
for file in boldfiles:  
    print file
    os.system("fslnvols %s"%(file))

